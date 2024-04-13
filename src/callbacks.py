# Script containing all callbacks relevant to app.py
# Includes plotting, widget values, data ingest and preprocessing

from dash import html, Input, Output, callback

import pandas as pd
import dash_vega_components as dvc
import dash_bootstrap_components as dbc
import dash_daq as daq


from src.fetch_data import fetch_country_data
from src.plotting import *
from src.calc_index import *
from src.data_preprocess import get_clean_data

from io import StringIO


@callback(
    [
        Output("date-range", "min_date_allowed"),
        Output("date-range", "max_date_allowed"),
        Output("date-range", "start_date"),
        Output("date-range", "end_date"),
        Output("commodities-dropdown", "options"),
        Output("commodities-dropdown", "value"),
        Output("markets-dropdown", "options"),
        Output("markets-dropdown", "value"),
        Output("country-dropdown", "options"),
    ],
    [Input("country-index", "data"), Input("country-data", "data")],
)
def update_widget_values(country_index_json, country_json):
    """
    Update widget options when a new country is selected.

    Parameters
    ----------
    country_index_json : str
        JSON string representing the index of the country data, used for populating country options.

    country_json : str
        JSON string representing the country data, used for extracting commodity, market, and date information.

    n_clicks : int
        The number of times the update button has been clicked (not used in the function, but required for callback).

    Returns
    -------
    tuple
        A tuple containing the minimum and maximum dates allowed, start and end dates,
        lists of commodity options and default commodity selection,
        lists of market options and default market selection, and country options list.
    """
    country_index = pd.read_json(StringIO(country_index_json), orient="split")

    country_data = pd.read_json(StringIO(country_json), orient="split")

    min_date_allowed = country_data.date.min()
    max_date_allowed = country_data.date.max()
    start_date = max(country_data.date.max() + pd.tseries.offsets.DateOffset(years=-2), country_data.date.min())
    end_date = country_data.date.max()

    commodities_options = country_data.commodity.value_counts().index.tolist()
    commodities_selection = commodities_options[:2]

    markets_options = country_data.market.value_counts().index.tolist()
    markets_selection = markets_options[:2]

    country_options = country_index.index.to_list()

    output = (
        min_date_allowed,
        max_date_allowed,
        start_date,
        end_date,
        commodities_options,
        commodities_selection,
        markets_options,
        markets_selection,
        country_options,
    )

    return output


@callback(
    Output("country-data", "data"),
    [Input("country-dropdown", "value"), Input("country-index", "data")],
)
def update_country_data(country, country_index):
    """
    Update country data from country widget selection

    Parameters
    ----------
    country : str
        string of selected country, e.g., "Japan"
    country_index : pd.DataFrame.to_json()
        JSONify'd version of a pd.DataFrame, the output of fetch_country_index()

    Returns
    -------
    json
        JSON version of dataframe of WFP data from the given country, retrieved from the HDX and minimially preprocessed.

    """
    data = fetch_country_data(country, country_index)
    data = get_clean_data(data)

    return data


@callback(
    [Output("index-area", "children"), Output("commodities-area", "children")],
    [
        Input("country-data", "data"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
        Input("commodities-dropdown", "value"),
        Input("markets-dropdown", "value"),
    ],
)
def update_index_commodities_area(
    country_json, start_date, end_date, commodities, markets
):
    """
    Generate and update the food price index figure and line charts for the selected parameters.

    Parameters
    ----------
    country_json : str
        JSON string representing the country data from which the food price index is generated.

    start_date : str or datetime
        The starting date for filtering the data used in the charts.

    end_date : str or datetime
        The ending date for filtering the data used in the charts.

    commodities : list
        A list of commodities to be included in the food price index calculation.

    markets : list
        A list of market names from which the data will be filtered to generate the charts.

    Returns
    -------
    dash_vega_components.Vega
        An object that combines the line and figure charts displaying the food price index
    list
        A list of dash_vega_components.Vega objects, each combining an area and a line chart for each commodity.

    """
    country_data = pd.read_json(StringIO(country_json), orient="split")

    ## Create commodities chart
    commodities_line = generate_line_chart(
        country_data, (start_date, end_date), markets, commodities
    )
    commodities_figure = generate_figure_chart(
        country_data, (start_date, end_date), markets, commodities
    )

    chart_plots = []
    tmp = []
    for i, (line, figure) in enumerate(zip(commodities_line, commodities_figure)):
        tmp.append(
            dbc.Col([
                dvc.Vega(spec=(figure).to_dict(format="vega"), opt={'actions': False}, style={'width': '100%'}),
                dvc.Vega(spec=(line).to_dict(format="vega"), opt={'actions': False}, style={'width': '100%', "height": "180px"}),
            ],
                md=6
            )
        )
        if i % 2 == 1:
            chart_plots.append(dbc.Row(tmp))
            chart_plots.append(dbc.Row(dbc.Col(html.Div(style={'height': '15px'}))))
            tmp = []

    if tmp:
        chart_plots.append(dbc.Row(tmp))

    # Use Card for Index Charts Layout
    commodities_area = dbc.Card(
        children=[
        dbc.CardHeader('Commodities', style={
            'fontWeight': 'bold',
            'background-color': 'rgba(221, 231, 193, 1)',
            'border-radius': '5px',
            'border-bottom': '0'
        }),
        dbc.CardBody(
            [
#                html.H5("Commodities", style={'fontWeight': 'bold'}),
#                html.P("This section displays the price of individual commodities.", className="card-text"),
                *chart_plots
            ]
        )],
        style={
            'width': 'calc(100vw - 350px)', 
            'height': 'auto',
            'border': 'none',
            'border-radius': '5px',
            'margin': '10px'
        }
    )

    ## Create Index Charts
    country_data = generate_food_price_index_data(country_data, markets, commodities)

    index_line = generate_line_chart(
        country_data, (start_date, end_date), markets, ["Food Price Index"]
    )[0]

    index_figure = generate_figure_chart(
        country_data, (start_date, end_date), markets, ["Food Price Index"]
    )[0]

    index_figure = index_figure.properties(
        title=alt.TitleParams(
            text="Food Price Index",
            fontSize=15,
            subtitle=[f"(Arithmetic mean of {', '.join(commodities)})"],
        )
    )

    # Use Card for Index Charts Layout
    index_area = dbc.Card(
        children=[
        dbc.CardHeader('Overview', style={
            'fontWeight': 'bold',
            'background-color': 'rgba(221, 231, 193, 1)',
            'border-radius': '5px',
            'border-bottom': '0'
        }),
        dbc.CardBody([
#            html.H5("Food Price Overview", style={'fontWeight': 'bold'}),
#            html.P("This section displays the overall food price index based on selected parameters.", className="card-text"),
            dvc.Vega(spec=(index_figure).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%"}),
            dvc.Vega(spec=(index_line).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%", "height": "220px"})
        ])
        ],
        style={
            'width': 'calc(100vw - 350px)', 
            'height': 'auto',
            'border': 'none',
            'border-radius': '5px',
            'margin': '10px',
            'padding-top': '10px'
        }
    )

    return index_area, commodities_area