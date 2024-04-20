# Script containing all callbacks relevant to app.py
# Includes plotting, widget values, data ingest and preprocessing

from dash import html, Input, Output, callback

import pandas as pd
import dash_vega_components as dvc
import dash_bootstrap_components as dbc
import dash_daq as daq

from src.data import *
from src.plotting import *
from src.utils import convert_date

from io import StringIO


@callback(
    Output("content-area", "children"), 
    [
        Input("geo-toggle", "on"), 
    ]
)
def toggle_chart_view(toggle = False): 
    """Toggle between geo and chart views 

    Parameters
    ----------
    toggle : bool
        True: enable geo-area chart. False: enable typical commodities chart.

    Returns
    -------
    dbc.Row
        dbc elements corresponding to geo or typical charts. 
    """
    if toggle: 
        return [
                dbc.Row(id="geo-area", children=[], style={"width":"100%", "padding":"0px", "margin":"0px"}),
                dbc.Row(id="index-area", children=[]),
                dbc.Row(id="commodities-area", children=[])

        ]
    
    else: 
        return [
                dbc.Row(id="index-area", children=[], style={"width":"100%", "padding":"0px", "margin":"0px"}),
                dbc.Row(id="commodities-area", children=[], align="center", style={"width":"100%", "padding":"0px", "margin":"0px"}),
                dbc.Row(id="geo-area", children=[])
        ]



@callback(
    [
        Output("date-range", "min"),
        Output("date-range", "max"),
        Output("date-range", "step"),
        Output("date-range", "value"),
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

    min_date_allowed = convert_date(country_data.date.min(), 'label')
    max_date_allowed = convert_date(country_data.date.max(), 'label')
    start_date = convert_date(max(country_data.date.max() + pd.tseries.offsets.DateOffset(years=-2), country_data.date.min()), 'label')
    end_date = convert_date(country_data.date.max(), 'label')
    date_step = 1/12
    date_range = [start_date, end_date]

    commodities_options = country_data.commodity.value_counts().index.tolist()
    commodities_selection = commodities_options[:2]

    markets_options = country_data.market.value_counts().index.tolist()
    markets_selection = markets_options[:2]

    country_options = sorted(country_index.index.to_list())

    output = (
        min_date_allowed,
        max_date_allowed,
        date_step,
        date_range,
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
    Output("date-range-label", "children"),
    Input("geo-toggle", "on")
)
def update_date_range_label(toggle):
    """
    Update the label of a date range component based on the state of a toggle.

    Parameters
    ----------
    toggle : bool
        The state of the toggle. If `True`, the label indicates that only the end date
        matters. If `False`, the label simply shows "Date Range".

    Returns
    -------
    list
        A list containing a single dbc.Col element with the updated html.Label as its child.
    """

    if toggle:
        return [
            dbc.Col(html.Label("Date Range (only end date matters)")),
        ]
    else:
        return [
            dbc.Col(html.Label("Date Range")),
        ]

@callback(
    [Output("geo-area", "children")],
    [
        Input("country-data", "data"),
        Input("date-range", "value"),
        Input("commodities-dropdown", "value"),
        Input("markets-dropdown", "value"),
        Input("geo-toggle", "on"),
        Input("country-dropdown", "value")
    ],    
)
def update_geo_area(
    country_json, date_range, commodities, markets, toggle, country
):
    """
    Generate and update the geo chart for the selected parameters.

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

    toggle : bool
        True: enable geo-area chart. False: enable typical commodities chart.

    Returns
    -------
    dash_vega_components.Vega
        An object that combines the line and figure charts displaying the food price index
    list
        A list of dash_vega_components.Vega objects, each combining an area and a line chart for each commodity.
    """
    if toggle == False:
        return [html.Label("")]

    country_data = pd.read_json(StringIO(country_json), orient="split")

    ## Create Index Charts
    country_data = generate_food_price_index_data(country_data, markets, commodities)

    start_date = convert_date(date_range[0], 'datetime')
    end_date = convert_date(date_range[1], 'datetime')

    # Plot Geo Chart
    geo_chart = generate_geo_chart(country_data, (start_date, end_date), markets, ["Food Price Index"], country)

    geo_chart = geo_chart.properties(
        title=alt.TitleParams(
            text="Geo View of Latest Food Price Index",
            fontSize=15,
            subtitle=[f"(Arithmetic mean of {', '.join(commodities)})"],
        )
    )

    # Use Card for Index Charts Layout
    geo_area = dbc.Card(
        children=[
        dbc.CardHeader('Geo View', style={
            'fontWeight': 'bold',
            'background-color': 'rgba(221, 231, 193, 1)',
            'border-radius': '5px',
            'border-bottom': '0'
        }),
        dbc.CardBody([
            dvc.Vega(spec=(geo_chart).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%", "height": "auto"}),
        ])
        ],
        style={
            'width': '100%', 
            'height': 'auto',
            'border': 'none',
            'border-radius': '5px',
            "padding":"0px",

            # 'margin': '10px',
            # 'padding-top': '10px'
        }
    )

    return [geo_area]









@callback(
    [Output("index-area", "children"), Output("commodities-area", "children")],
    [
        Input("country-data", "data"),
        Input("date-range", "value"),
        Input("commodities-dropdown", "value"),
        Input("markets-dropdown", "value"),
        Input("geo-toggle", "on"),
    ],
)
def update_index_commodities_area(
    country_json, date_range, commodities, markets, toggle
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
    
    toggle : bool
        True: enable geo-area chart. False: enable typical commodities chart.

    Returns
    -------
    dash_vega_components.Vega
        An object that combines the line and figure charts displaying the food price index
    list
        A list of dash_vega_components.Vega objects, each combining an area and a line chart for each commodity.

    """
    if toggle: 
        return [html.Label("")], [html.Label("")]

    
    country_data = pd.read_json(StringIO(country_json), orient="split")

    start_date = convert_date(date_range[0], 'datetime')
    end_date = convert_date(date_range[1], 'datetime')

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
            'border-bottom': '0',
            'border-radius': '5px',
        }),
        dbc.CardBody(
            [
#                html.H5("Commodities", style={'fontWeight': 'bold'}),
#                html.P("This section displays the price of individual commodities.", className="card-text"),
                *chart_plots
            ]
        )],
        style={
            'width': '100%', 
            'height': 'auto',
            'border': 'none',
            'margin': '0px',
            "padding":"0px",
            'border-radius': '5px',
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
            'border-bottom': '0',
            'border-radius': '5px',
        }),
        dbc.CardBody([
#            html.H5("Food Price Overview", style={'fontWeight': 'bold'}),
#            html.P("This section displays the overall food price index based on selected parameters.", className="card-text"),
            dvc.Vega(spec=(index_figure).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%"}),
            dvc.Vega(spec=(index_line).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%", "height": "220px"})
        ])
        ],
        style={
            'width':"100%",
            'height': 'auto',
            'border': 'none',
            'margin': '0px',
            "padding":"0px",
            'border-radius': '5px',
        }
    )

    return index_area, commodities_area
