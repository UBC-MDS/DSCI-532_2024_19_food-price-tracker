from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import dash_daq as daq
import pandas as pd
from io import StringIO

from src.fetch_data import fetch_country_data, fetch_country_index
from src.plotting import *
from src.calc_index import *

# Initialize the app (using bootstrap theme)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) # need to manually refresh it
server = app.server

# Side navigation bar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "30rem",
    "padding": "2rem 1rem",
    "background-color": "#f0f0f0",
}

sidebar = html.Div(
    [
        html.H2("Food Price Tracker", className="display-10"),
        html.Hr(),
        daq.ToggleSwitch(
            id='chart-type-toggle',
            value=False
        ),
        html.Br(),

        html.P("Country"),
        dcc.Dropdown(
            id='country-dropdown',
            value="Japan",
            multi=False,
            placeholder='Select a country...'
        ),
        html.Br(),

        html.P("Date"),
        dcc.DatePickerRange(
            id="date-range",
            start_date_placeholder_text = "Start",
            end_date_placeholder_text = "End",
            updatemode = "singledate"
        ),
        html.Br(),

        html.Br(),
        html.P("Commodities"),
        dcc.Dropdown(
            id='commodities-dropdown',
            multi=True,
            placeholder='Select commodities...'
        ),
        html.Br(),

        html.P("Markets"),
        dcc.Dropdown(
            id='markets-dropdown',
            multi=True,
            placeholder='Select markets...'
        ),
        html.Br(),
        html.Button('Manual Trigger', id='manual-trigger-button', n_clicks=0)
    ],
    style=SIDEBAR_STYLE,
)

# Layout (better default layout when using with bootstrap)
content = dbc.Container([
    dbc.Row(id="index-area", children=[]),
    html.Hr(),
    dbc.Row(id="commodities-area", children=[], align="center"),
    html.Hr(),
    html.Footer(
        dcc.Markdown('''
        Food Price Tracker is developed by Celeste Zhao, John Shiu, Simon Frew, Tony Shum.  
        The application provides global food price visualization to enhance cross-sector collaboration on worldwide food-related challenges.  
        [`Link to the Github Repo`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/)  
        Dashboard latest update on ![release](https://img.shields.io/github/release-date/UBC-MDS/DSCI-532_2024_19_food-price-tracker)
        ''',
        style={'fontSize': 14})
    ),
], style={
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
})

app.layout = html.Div([
    sidebar, 
    content,
    dcc.Store(
        id="country-index",
        data=fetch_country_index(),
        storage_type="session"
    ),
    dcc.Store(
        id="country-data",
        storage_type="session"
    )
])

# # Server side callbacks/reactivity
# @callback(
# 	Output(‘output_area’, ‘children’), # and then put it into children argument of the output_area
# 	Input(input_widget’, ‘value’) # take the value from the value argument of the input_widget
# )
# def update_output(input_value):
# 	return input_value

# Run the app/dashboard

### Server-side testing

@callback(
    [Output("date-range", "min_date_allowed"),
     Output("date-range", "max_date_allowed"),
     Output("date-range", "start_date"),
     Output("date-range", "end_date"),

     Output("commodities-dropdown", "options"),
     Output("commodities-dropdown", "value"),

     Output("markets-dropdown", "options"),
     Output("markets-dropdown", "value"),

     Output("country-dropdown", "options")],
    [Input("country-index", "data"), Input("country-data", "data"), Input("manual-trigger-button", "n_clicks")]
)
def update_widget_values(country_index_json, country_json, n_clicks):
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
    country_index = pd.read_json(StringIO(country_index_json) , orient='split')

    country_data = pd.read_json(StringIO(country_json), orient='split')

    min_date_allowed = country_data.date.min()
    max_date_allowed = country_data.date.max()
    start_date = country_data.date.max() + pd.tseries.offsets.DateOffset(years=-2)
    end_date = country_data.date.max()

    commodities_options = country_data.commodity.unique().tolist()
    commodities_selection = commodities_options[:2]

    markets_options = country_data.market.unique().tolist()
    markets_selection = markets_options[:2]

    country_options = country_index.index.to_list()

    output = (
        min_date_allowed, max_date_allowed,
        start_date, end_date,
        commodities_options,
        commodities_selection,
        markets_options,
        markets_selection,
        country_options
    )

    return output

@callback(
    Output("country-data", "data"),
    [Input("country-dropdown", "value"), Input("country-index", "data")]
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

    return fetch_country_data(country, country_index)

@callback(
    Output("index-area", "children"),
    [
        Input("country-data", "data"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
        Input("commodities-dropdown", "value"),
        Input("markets-dropdown", "value"),
    ]
)
def update_index_area(country_json, start_date, end_date, commodities, markets):
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
        
    """
    country_data = pd.read_json(StringIO(country_json), orient='split')
    country_data = generate_food_price_index_data(country_data, markets, commodities)
    
    line = generate_line_chart(
        country_data, 
        (start_date, end_date), 
        markets,
        ["Food Price Index"]
    )[0]
    line = line.properties(
        title=alt.TitleParams(
            "Food Price Index",
            subtitle=[f"(Arithmetic mean of {', '.join(commodities)})"]
        )
    )
    
    figure = generate_figure_chart(
        country_data, 
        (start_date, end_date), 
        markets,
        ["Food Price Index"]
    )[0]
    
    return dvc.Vega(spec=(figure | line).to_dict(format="vega"), style={'width': '60%'})


@callback(
    Output("commodities-area", "children"),
    [
        Input("country-data", "data"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
        Input("commodities-dropdown", "value"),
        Input("markets-dropdown", "value"),
    ]
)
def update_commodities_area(country_json, start_date, end_date, commodities, markets):
    """
    Generate and update the figure and line charts for the selected commodities and markets over a given date range.

    Parameters
    ----------
    country_json : str
        JSON string representing the country data, used to generate charts for specified commodities and markets.
        
    start_date : str or datetime
        The starting date for filtering the data used in the charts.
        
    end_date : str or datetime
        The ending date for filtering the data used in the charts.
        
    commodities : list
        A list of commodities for which the charts will be generated.
        
    markets : list
        A list of market names from which the data will be filtered to generate the charts.

    Returns
    -------
    list
        A list of dash_vega_components.Vega objects, each combining an area and a line chart for each commodity.
        
    """
    country_data = pd.read_json(StringIO(country_json), orient='split')
    
    line_charts = generate_line_chart(
        country_data, 
        (start_date, end_date), 
        markets,
        commodities
    )
    figure_charts = generate_figure_chart(
        country_data, 
        (start_date, end_date), 
        markets,
        commodities
    )

    chart_plots = [
        dvc.Vega(spec=(figure | line).to_dict(format="vega"), style={'width': '60%'})
        for line, figure in zip(line_charts, figure_charts)
    ]
    
    return chart_plots
    
if __name__ == '__main__':
    app.run(debug=True) # the debug mode will add a button at the bottom right of the web
