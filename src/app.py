from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd

from fetch_data import fetch_country_data, fetch_country_index

# Initialize the app (using bootstrap theme)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) # need to manually refresh it
server = app.server

# Side navigation bar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
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
        	options=[],
            multi=False, 
    	    placeholder='Select a country...'
        ),
        html.Br(),
        
        html.P("Date"),
        html.Br(),

        html.P("Commodities"),
        dcc.Dropdown(
        	id='commodities-dropdown',
        	options=[],
            multi=True, 
    	    placeholder='Select commodities...'
        ),
        html.Br(),

        html.P("Markets"),
        dcc.Dropdown(
            id='commodities-dropdown',
        	options=[],
            multi=True,
            placeholder='Select markets...'
        ),
        html.Br(),
    ],
    style=SIDEBAR_STYLE,
)

# Layout (better default layout when using with bootstrap)
content = dbc.Container([
	html.Br(),
    dcc.Slider(min=0, max=5, value=2, step=1), # dcc has different objects
    dcc.RangeSlider(min=0, max=5, value=[2, 4], tooltip={'always_visible': True, 'placement': 'bottom'}), 
    dcc.Dropdown(
    	options=['New York DCity', 'Montreal', 'San Francisco'],
    	multi=True, # allow selecting New York City and Montreal at the same time
    	placeholder='Select a city...'
    ),
    dcc.Input(id='input_widget'),  # to be connected in the callbacks
    html.Div(id='output_area')      # to be connected in the callbacks
], style={
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
})

app.layout = html.Div(
    [sidebar, content,
     dcc.Store(
         id="country-index", 
         data=fetch_country_index(), 
         storage_type="session"
         ),
     dcc.Store(
         id="country-data", 
         data=fetch_country_data(), 
         storage_type="session"
         )]
)

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
    [Input("country-dropdown", "value"), Input("country-index", "data")],
    Output("country-data", "data")
)
def update_country_data(country, country_index): 
    """Update country data from country widget selection

    Parameters
    ----------
    country : str
        string of selected country, e.g., "Japan"
    country_index : pd.DataFrame.to_json()
        JSONify'd version of a pd.DataFrame, the output of fetch_country_index()

    Returns
    -------
    country_json : pd.DataFrame.to_json()
        JSON version of dataframe of WFP data from the given country, retrieved from the HDX and minimially preprocessed.

    """

    return fetch_country_data(country, country_index).to_json()


def update_widget_values():
    """_summary_
    """
    pass

if __name__ == '__main__':
    app.run(debug=True) # the debug mode will add a button at the bottom right of the web
