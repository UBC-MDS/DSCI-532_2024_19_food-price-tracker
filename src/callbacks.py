# Script containing all callbacks relevant to app.py
# Includes plotting, widget values, data ingest and preprocessing

from dash import html, Input, Output, State, callback

import jsonpickle
import pandas as pd
import dash_vega_components as dvc
import dash_bootstrap_components as dbc
import dash_daq as daq

from dash.exceptions import PreventUpdate
from src.data import *
from src.plotting import *
from src.utils import convert_date, compile_widget_state, compare_widget_state

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
        return dbc.Col(id="geo-area")
    
    else: 
        return [
                dbc.Row(id="index-area", children=[], style={"width":"100%", "padding":"0px", "margin":"0px"}),
                dbc.Row(id="commodities-area", children=[], align="center", style={"width":"100%", "padding":"0px", "margin":"0px"})
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
        Output("widget-state", "data")
    ],
    [Input("country-index", "data"), Input("country-data", "data"), 
     State("geo-toggle", "on"), State("country-dropdown", "value")],
)
def update_widget_values(country_index_json, country_json, toggle, country):
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

    toggle : bool
        True: enable geo-area chart. False: enable typical commodities chart.

    country : str
        string of selected country, e.g., "Japan"
    
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
        compile_widget_state(
            None, 
            None, 
            None,
            None, 
            None
        )
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
    [Output("geo-area", "children"), Output("widget-state", "data", allow_duplicate=True)],
    [
        State("country-data", "data"),
        State("date-range", "value"),
        State("commodities-dropdown", "value"),
        State("markets-dropdown", "value"),
        Input("geo-toggle", "on"),
        State("date-range", "value"),
        State("country-dropdown", "value")
    ],
    prevent_initial_call=True
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
    current_widget_state = compile_widget_state(
        toggle, 
        country, 
        date_range,
        commodities,
        markets
    )

    if toggle == False: 
        raise PreventUpdate 
    
    country_data = pd.read_json(StringIO(country_json), orient="split")


    ## Create Index Charts
    country_data = generate_food_price_index_data(country_data, markets, commodities)

    start_date = convert_date(date_range[0], 'datetime')
    end_date = convert_date(date_range[1], 'datetime')

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
            dvc.Vega(spec=(index_figure).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%"}),
            dvc.Vega(spec=(index_line).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%", "height": "220px"})
        ])
        ],
        style={
            'width': '100%', 
            'height': 'auto',
            'border': 'none',
            'border-radius': '5px',
            "padding":"0px",
            'padding-top': '10px'
        }
    )

    return [index_area], current_widget_state


@callback(
    [Output("index-area", "children"), Output("commodities-area", "children"),
     Output("widget-state", "data", allow_duplicate=True), Output("commodities-charts", "data")],
    [
        Input("country-data", "data"),
        Input("date-range", "value"),
        Input("commodities-dropdown", "value"),
        Input("markets-dropdown", "value"),
        Input("geo-toggle", "on"),
        State("country-dropdown", "value"),
        State("widget-state", "data"),
        State("commodities-charts", "data")
    ],
    prevent_initial_call=True
)
def update_index_commodities_area(
    country_json, date_range, commodities, markets, toggle, country, prior_widget_state, commodities_children
):
    """
    Generate and update the food price index figure and line charts for the selected parameters.

    Parameters
    ----------
    country_json : str
        JSON string representing the country data from which the food price index is generated.

    date_range : tuple of str or datetime
        The starting and ending date in a tuple for filtering the data used in the charts.

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
    current_widget_state = compile_widget_state(
        toggle, 
        country, 
        date_range,
        commodities,
        markets
    )

    # check for breaking states
    if toggle: 
        raise PreventUpdate 
    
    if not commodities or not markets: 
        alert = dbc.Alert(
            dbc.Row(
                [
                    dbc.Col(html.H3("!"), width="auto"),
                    dbc.Col(html.Div(style={'border-left': '2px solid', 'height': '40px'}), width="auto"), 
                    dbc.Col(html.P("Please select a commodity and / or a market", className="ml-3", style={"margin-bottom":"0"}), width=True) 
                ], align="center", justify="center", className="g-3",
                
            ),
            color="warning"
        )
        return alert, [], current_widget_state, jsonpickle.encode([])

    country_data = pd.read_json(StringIO(country_json), orient="split")

    start_date = convert_date(date_range[0], 'datetime')
    end_date = convert_date(date_range[1], 'datetime')

    ## Create commodities chart

    # check if prior charts can be reused
    existing_commodities_map = {}
    if (
        current_widget_state["country"] == prior_widget_state["country"] and
        current_widget_state["date_range"] == prior_widget_state["date_range"] and 
        set(current_widget_state["markets"]) == set(prior_widget_state["markets"])
    ): 
        value_state = compare_widget_state(current_widget_state, prior_widget_state, field="commodities")

        # find existing commodities and extract
        commodities_children = jsonpickle.decode(commodities_children)
        
        if commodities_children: 
            for i in np.arange(0, len(commodities_children.children[1].children), 2): 
                for child_chart in commodities_children.children[1].children[i].children: 
                    existing_commodities_map[child_chart.id] = child_chart
    else: 
        value_state = {commodity_name: "new" for commodity_name in commodities}

    # generate new charts
    new_commodities = [key for key, value in value_state.items() if value == 'new']
    if new_commodities: 
        new_commodities_line_map = dict(zip(
            new_commodities,
            generate_line_chart(
                country_data, (start_date, end_date), markets, new_commodities
            )
        ))
        new_commodities_figure_map = dict(zip(
            new_commodities,
            generate_figure_chart(
                country_data, (start_date, end_date), markets, new_commodities
            )
        ))

    # lay out commodity charts in grid
    chart_plots = []
    tmp = []
    for i, (commodity_name, state) in enumerate(value_state.items()):
        if state == "new":
            tmp.append(
                dbc.Col([
                        dvc.Vega(spec=(new_commodities_figure_map[commodity_name]).to_dict(format="vega"), opt={'actions': False}, style={'width': '100%'}),
                        dvc.Vega(spec=(new_commodities_line_map[commodity_name]).to_dict(format="vega"), opt={'actions': False}, style={'width': '100%', "height": "180px"}),
                    ],
                        md=6, 
                        id = commodity_name
                    )
                )
        elif state == "exists":
            tmp.append(
                existing_commodities_map[commodity_name]
            )
        if i % 2 == 1:
                chart_plots.append(dbc.Row(tmp))
                chart_plots.append(dbc.Row(dbc.Col(html.Div(style={'height': '15px'}))))
                tmp = []

    if tmp:
        chart_plots.append(dbc.Row(tmp))

    # create Card layout for commodities
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

    return index_area, commodities_area, current_widget_state, jsonpickle.encode(commodities_area)