from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq

import src.callbacks
from src.data import *
from src.plotting import *


# Initialize the app (using bootstrap theme)
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Food Price Tracker"
)
server = app.server

# Top navigation bar
LOGO = "https://raw.githubusercontent.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/main/img/logo.png"
topbar = dbc.Row(
    [
        dbc.Col(html.Img(src=LOGO, height="80px"), md="auto"),
        dbc.Col(
            html.H1(
                'Global Food Price Tracker',
                style={
                    'color': 'white',
                    'text-align': 'left',
                    'font-size': '48px'
                }
            ),
            md=8, align="center"
        ),
        dbc.Col(
            []
        , md=2, align="center"
        ) # FIXME: to add button
    ], 
    style={
        'padding-left': '7px',  # Padding left
        'padding-top': '3px',  # Center vertically, while keeping objects constant when expanding
        'padding-bottom': '3px',  # Center vertically, while keeping objects constant when expanding
        'min-height': '1vh',  # min-height to allow expansion
    }
)

# Side navigation bar
SIDEBAR_STYLE = {
    'background-color': 'rgba(230, 230, 230, 0.5)',  # Color #e6e6e6 with 50% opacity
    'padding': 15,  # Padding top,left,right,botoom
    'padding-top': 28,
    'padding-bottom': 0,  # Remove bottom padding for footer
    'height': '200vh',  # vh = "viewport height" = 90% of the window height
    "width": "320px",
    'display': 'flex',  # Allow children to be aligned to bottom
    'flex-direction': 'column',  # Allow for children to be aligned to bottom
}

sidebar = dbc.Col(
    [
        html.P("Country"),
        dcc.Dropdown(
            id="country-dropdown",
            value="Japan",
            multi=False,
            placeholder="Select a country...",
            style={'width': '100%'}
        ),
        html.Br(),
        html.P("Date Range"),
        dcc.DatePickerRange(
            id="date-range",
            start_date_placeholder_text="Start",
            end_date_placeholder_text="End",
            updatemode="singledate",
            style={'width': '100%'}
        ),
        html.Br(),
        html.P("Commodities"),
        dcc.Dropdown(
            id="commodities-dropdown", 
            multi=True, 
            placeholder="Select commodities...",
            style={'width': '100%'}
        ),
        html.Br(),
        html.P("Markets"),
        dcc.Dropdown(
            id="markets-dropdown", 
            multi=True, 
            placeholder="Select markets...",
            style={'width': '100%'}
        ),
        html.Br(),
        html.Br(),
        daq.BooleanSwitch(
            id='geo-toggle',
            on=False,
            label={'label': 'Geo Mode (TBU)', 'style': {'color': '#CC5500', 'font-weight': 'bold'}},
            color='#72b7b2'
        )
    ],
    md=2,
    style=SIDEBAR_STYLE
)

content = dbc.Col(
    id = "content-area",
    children=[
                dbc.Row(id="index-area", children=[]),
                dbc.Row(id="commodities-area", children=[], align="center")
            ])

# Layout (better default layout when using with bootstrap)
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([topbar]),
        dbc.Col([], md=3,)
    ], style={
        'backgroundColor': 'rgba(204, 85, 0, 0.6)',  # Color #CC5500 with 60% opacity
        'padding-top': '2vh',  # Center vertically, while keeping objects constant when expanding
        'padding-bottom': '2vh',  # Center vertically, while keeping objects constant when expanding
        'min-height': '10vh',  # min-height to allow expansion
    }),
    dbc.Row([
        sidebar,
        dbc.Col([
            content, 
            html.Hr(),
            html.Footer(
                dcc.Markdown('''
                Food Price Tracker is developed by Celeste Zhao, John Shiu, Simon Frew, Tony Shum.  
                The application provides global food price visualization to enhance cross-sector collaboration on worldwide food-related challenges.  
                [`Link to the Github Repo`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/)  
                Dashboard latest update on ![release](https://img.shields.io/github/release-date/UBC-MDS/DSCI-532_2024_19_food-price-tracker)
                ''',
                style={'fontSize': 14})
            )
        ]),
        dcc.Store(
            id="country-index",
            data=fetch_country_index(),
            storage_type="session"
        ),
        dcc.Store(
            id="country-data",
            storage_type="session"
        )
    ]),
], fluid=True)

  
if __name__ == '__main__':
    app.run() 
