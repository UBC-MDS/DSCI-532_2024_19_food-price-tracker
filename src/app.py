from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq

from src.cache_config import init_cache

# Initialize the app (using bootstrap theme)
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Food Price Tracker",
    suppress_callback_exceptions=True
)

init_cache(app.server)
import src.callbacks
from src.plotting import *
from src.data import *


# Top navigation bar
LOGO = "https://raw.githubusercontent.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/main/img/logo.png"
topbar = dbc.Row(
    [
        dbc.Col(html.Img(src=LOGO, height="80px"), md="auto", style={"padding-left":"4px"}),
        dbc.Col(
            html.H1(
                'Global Food Price Tracker',
                style={
                    'color': 'white',
                    'text-align': 'left',
                    'font-size': '40px'
                }
            ),
            md=8, align="center"
        )
    ]
)

# Side navigation bar
SIDEBAR_STYLE = {
    'background-color': 'rgba(230, 230, 230, 0.5)', 
    'padding': 15, 
    'padding-top': 30,
    'padding-bottom': 0,
    'height': 'calc(100vh - 88px)',
    "width": "18%",
    "max-width": "18%",
    'display': 'flex',
    'flex-direction': 'column',
    "justify-content": "space-between"
}

sidebar = dbc.Col([
    dbc.Stack([
        dbc.Row([
            dbc.Col(html.Label("Enable Geo-View:"), width=9),        
            dbc.Col(daq.BooleanSwitch(
                        id='geo-toggle',
                        on=False,
                        color='#72b7b2'
                    ), width=3)
        ]),
        html.Hr(),
        html.Div([dbc.Row([
            dbc.Col(html.Label("Country")),
        ]),
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id="country-dropdown",
                value="Japan",
                multi=False,
                placeholder="Select a country...",
                style={'width': '100%'}
            )),
        ])]),
        html.Div([dbc.Row([
            dbc.Col(html.Label("Date Range")),
        ]),
        dbc.Row([
            dbc.Col(dcc.RangeSlider(
                id="date-range",
                updatemode='mouseup',
                dots=False,
                marks=None,
                tooltip={"placement": "bottom", 
                         "always_visible": True, 
                         'transform': 'dateParser'},
            )),
        ])]),
        html.Div([dbc.Row([
            dbc.Col(html.Label("Commodities")),
        ]),
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id="commodities-dropdown",
                multi=True,
                placeholder="Select commodities...",
                style={'width': '100%'}
            )),
        ])]),
        html.Div([dbc.Row([
            dbc.Col(html.Label("Markets")),
        ]),
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id="markets-dropdown",
                multi=True,
                placeholder="Select markets...",
                style={'width': '100%'}
            )),
        ])])
    ], gap=3),
    html.Footer(
                dcc.Markdown('''
                Supporting decision makers with accessible global food-price visualizations.

                Celeste Zhao, John Shiu, Simon Frew, Tony Shum
                             
                [![GitHub repo](https://img.shields.io/badge/-GitHub-grey?style=flat&logo=github)](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker)
                [![GitHub release](https://img.shields.io/github/release/UBC-MDS/DSCI-532_2024_19_food-price-tracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/releases)
                ![GitHub release date](https://img.shields.io/github/release-date/UBC-MDS/DSCI-532_2024_19_food-price-tracker)
                ''',
                style={'fontSize': 14})
            )
        ],
    style=SIDEBAR_STYLE
)

content = dbc.Col(
    id = "content-area",
    children=[
                dbc.Row(id="index-area", children=[], style={"width":"100%", "padding":"0px", "margin":"0px"}),
                dbc.Row(id="commodities-area", children=[], align="center", style={"width":"100%", "padding":"0px", "margin":"0px"})
        ],
    style={"width":"100%", "padding":0, "margin":0}
)

# Layout (better default layout when using with bootstrap)
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([topbar]),
        dbc.Col([], md=3,)
    ], style={
        'backgroundColor': 'rgba(204, 85, 0, 0.6)',  # Color #CC5500 with 60% opacity
        'padding-top': '4px',  # Center vertically, while keeping objects constant when expanding
        'padding-bottom': '4px',  # Center vertically, while keeping objects constant when expanding
        'height': '88px',  # min-height to allow expansion
    }),
    dbc.Row([
        sidebar,
        dbc.Col(
            html.Div([
                content,
                html.Div([
                    html.Hr(),
                    html.Footer(
                        html.Em(
                            "Glossary:    MoM - month-over-month percentage change.    YoY - year-over-year percentage change.",
                            style={'fontSize': 14, "margin-bottom":"0"}
                            ), 
                    )
                ])
                ],
            style={'height': 'calc(100vh - 88px)', 'width': '100%', 'padding': '15px', 'margin': '0', "justify-content": "space-between", 'display': 'flex', 'flex-direction': 'column',}),
            style={"overflow":"auto", "margin": 0, "padding": 0, "width": "100%"})
    ]),
        dcc.Store(
            id="country-index",
            data=fetch_country_index(),
            storage_type="session"
        ),
        dcc.Store(
            id="country-data",
            storage_type="session"
        ), 
        dcc.Store(
            id = "widget-state",
            storage_type="session"
        ),
        dcc.Store(
            id = "commodities-charts",
            storage_type="session"
        )
], fluid=True)

  
if __name__ == '__main__':
    app.run() 
