from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import dash_daq as daq
import pandas as pd
from io import StringIO

from src.fetch_data import fetch_country_data, fetch_country_index
from src.plotting import *
from src.calc_index import *
from src.data_preprocess import get_clean_data

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
        'padding-left': 7,  # Padding left
        'padding-top': '0.5vh',  # Center vertically, while keeping objects constant when expanding
        'padding-bottom': '0.5vh',  # Center vertically, while keeping objects constant when expanding
        'min-height': '1vh',  # min-height to allow expansion
    }
)

# Side navigation bar
SIDEBAR_STYLE = {
    'background-color': '#e6e6e6',
    'padding': 15,  # Padding top,left,right,botoom
    'padding-top': 25,
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

content = dbc.Col([ 
    dbc.Row(id="index-area", children=[]),
    html.Hr(),
    dbc.Row(id="commodities-area", children=[], align="center"),
    html.Hr(),
    html.Br(),
    html.Footer(
        dcc.Markdown('''
        Food Price Tracker is developed by Celeste Zhao, John Shiu, Simon Frew, Tony Shum.  
        The application provides global food price visualization to enhance cross-sector collaboration on worldwide food-related challenges.  
        [`Link to the Github Repo`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/)  
        Dashboard latest update on ![release](https://img.shields.io/github/release-date/UBC-MDS/DSCI-532_2024_19_food-price-tracker)
        ''',
        style={'fontSize': 14})
    ),
])
# , style={
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
# })

# Layout (better default layout when using with bootstrap)
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([topbar]),
        dbc.Col([], md=3,)
    ], style={
        'backgroundColor': 'rgba(204, 85, 0, 0.8)',  # Color #CC5500 with 80% opacity
        'padding-top': '2vh',  # Center vertically, while keeping objects constant when expanding
        'padding-bottom': '2vh',  # Center vertically, while keeping objects constant when expanding
        'min-height': '10vh',  # min-height to allow expansion
    }),
    dbc.Row([
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
    ]),
], fluid=True)

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
        dbc.CardBody(
            [
                html.H5("Commodities Analysis", style={'fontWeight': 'bold'}),
                html.P("This section displays the price of individual commodities.", className="card-text"),
                *chart_plots
            ]
        ),
        style={
            'width': 'calc(100vw - 350px)', 
            'height': 'auto',
            'border': 'none',
            'border-radius': '0px',
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
#        dbc.CardHeader('Food Price Index Dashboard', style={'fontWeight': 'bold'}),
        dbc.CardBody([
            html.H5("Food Price Overview", style={'fontWeight': 'bold'}),
            html.P("This section displays the overall food price index based on selected parameters.", className="card-text"),
            dvc.Vega(spec=(index_figure).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%"}),
            dvc.Vega(spec=(index_line).to_dict(format="vega"), opt={'actions': False}, style={"width": "100%", "height": "220px"})
        ]),
        style={
            'width': 'calc(100vw - 350px)', 
            'height': 'auto',
            'border': 'none',
            'border-radius': '0px',
            'margin': '10px'
        }
    )

    return index_area, commodities_area
  
if __name__ == '__main__':
    app.run() 
