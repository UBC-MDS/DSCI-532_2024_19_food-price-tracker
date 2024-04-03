from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_daq as daq

# Initialize the app (using bootstrap theme)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) # need to manually refresh it

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
            id='my-toggle-switch',
            value=False
        ),
        html.Br(),
        
        html.P("Country"),
        dcc.Dropdown(
        	options=['Japan'],
        ),
        html.Br(),
        
        html.P("Date"),
        html.Br(),

        html.P("Commodities"),
        dcc.Dropdown(
        	options=['Japan'],
            multi=True,
        ),
        html.Br(),

        html.P("Markets"),
        dcc.Dropdown(
        	options=['Japan'],
            multi=True,
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

app.layout = html.Div([sidebar, content])

# # Server side callbacks/reactivity
# @callback(
# 	Output(‘output_area’, ‘children’), # and then put it into children argument of the output_area
# 	Input(input_widget’, ‘value’) # take the value from the value argument of the input_widget
# )
# def update_output(input_value):
# 	return input_value

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True) # the debug mode will add a button at the bottom right of the web
