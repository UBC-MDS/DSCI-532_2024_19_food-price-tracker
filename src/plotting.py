import numpy as np
import pandas as pd
import altair as alt
import geopandas as gpd
from vega_datasets import data
from iso3166 import countries
alt.data_transformers.enable('vegafusion')

def generate_figure_chart(data, widget_date_range, widget_market_values, widget_commodity_values):
    """
    Generate figure charts displaying the latest average price and period-over-period change for specified commodities.

    Parameters
    ----------
    data : pandas.DataFrame
        Input food price data.
    widget_date_range : tuple
        A tuple containing the start and end dates for filtering the data.
    widget_market_values : list
        A list of market used to filter the data.
    widget_commodity_values : list
        A list of commodities for which figure charts will be generated.

    Returns
    -------
    list of altair.Chart
        A list of Altair figure charts displaying the latest average price and period-over-period change.

    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     'date': ['2022-01-01', '2022-01-01', '2022-01-02'],
    ...     'market': ['A', 'B', 'A'],
    ...     'latitude': [1, 2, 1],
    ...     'longitude': [1, 2, 1],
    ...     'commodity': ['Rice', 'Radish', 'Sugar'],
    ...     'unit': ['kg', 'kg', 'kg'],
    ...     'usdprice': [1.0, 2.0, 3.0]
    ... })
    >>> widget_date_range = ('2022-01-01', '2022-01-02')
    >>> widget_market_values = ['A', 'B']
    >>> widget_commodity_values = ['Rice', 'Radish', 'Sugar']
    >>> generate_figure_chart(data, widget_date_range, widget_market_values, widget_commodity_values)
    """

    # Default Info
    columns_to_keep = [
        "date",
        "market",
        "latitude",
        "longitude",
        "commodity",
        "unit",
        "usdprice",
    ]

    # Generate latest average price and period-over-period change
    price_data = data[columns_to_keep]
    price_data = price_data[
        price_data.date.between(
            widget_date_range[0], widget_date_range[1]
        )
        & (price_data.commodity.isin(widget_commodity_values))
        & (price_data.market.isin(widget_market_values))
    ]
    price_data = (
        price_data.groupby(["date", "commodity", "unit"])
        .agg({"usdprice": "mean"})
        .reset_index()
    )
    price_pivot = price_data.pivot_table(
        index="date", 
        columns=["commodity", "unit"], 
        values="usdprice"
    )

    price_summary = price_pivot.pct_change(1).iloc[-1].rename("mom").to_frame().reset_index()
    price_summary["yoy"] = price_pivot.pct_change(12).iloc[-1].values 
    price_summary["usdprice"] = price_pivot.iloc[-1].values
    price_summary["date"] = price_pivot.index[-1]

    # Generate Figure charts
    charts = []
    for item in widget_commodity_values:
        # Calculate the title
        data_filtered = price_summary[price_summary.commodity == item]
        title_text = data_filtered.iloc[0]['commodity'] + ' /' + data_filtered.iloc[0]['unit']
        
        chart = (
            alt.Chart(
                data_filtered,
                title=alt.Title(
                    text=title_text, align="center", fontSize=15
                ),
                width='container'
            )
            .mark_rect()
            .encode()
            .properties(height=30)
        )

        item_title = chart.mark_text(
            align='right', baseline='middle', dx=-100
        ).encode(
            text=alt.value("Latest Average: "),
            color=alt.value("black"),
            opacity=alt.value(0.8),
            size=alt.value(14),
        )
        
        item_value = chart.mark_text(
            align='right', baseline='middle', dx=-30
        ).encode(
            text=alt.Text("usdprice:Q", format="$.2f"),
            size=alt.value(18),
        )
        
        mom_value = chart.mark_text(
            dx=70, align="left", baseline='middle'
        ).encode(
            text=alt.Text("mom:Q", format="+.2%"),
            color=alt.condition(
                "datum.mom<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(14),
        )
        mom_title = chart.mark_text(
            dx=30, align="left", baseline='middle'
        ).encode(
            text=alt.value("*MoM:  "),
            color=alt.condition(
                "datum.mom<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(14),
        )
        yoy_value = chart.mark_text(
            dx=175, align="left", baseline='middle'
        ).encode(
            text=alt.Text("yoy:Q", format="+.2%"),
            color=alt.condition(
                "datum.yoy<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(14),
        )
        yoy_title = chart.mark_text(
            dx=140, align="left", baseline='middle'
        ).encode(
            text=alt.value("*YoY:  "),
            color=alt.condition(
                "datum.yoy<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(14),
        )
        chart = chart.encode(
            color=alt.value("lightgray"), opacity=alt.value(0.2)
        )
        chart += (
            item_value
            + item_title
            + mom_value
            + mom_title
            + yoy_value
            + yoy_title
        )
        charts.append(chart)

    return charts

def generate_line_chart(data, widget_date_range, widget_market_values, widget_commodity_values):
    """
    Generates a list of line charts, each representing the price trends of different commodities over time within specified marketplaces.

    The function filters the input data based on a given date range and a list of market values. 
    It then iterates through a list of commodities, creating an individual line chart for each one that visualizes its price trend in USD.

    Parameters
    ----------
    data : pd.DataFrame
        A Pandas DataFrame containing the commodities data including dates, markets, and prices.
        
    widget_date_range : tuple
        A tuple of two strings ('YYYY-MM-DD', 'YYYY-MM-DD') representing the start and end dates for filtering the data.
        
    widget_market_values : list of str)
        A list of string values representing the markets to include in the chart.
    
    widget_commodity_values : list of str)
        A list of string values representing the commodities for which the line charts will be generated.

    Returns:
    list of alt.Chart
        A list containing Altair Chart objects, each representing a line chart for a specific commodity.
        Each chart visualizes the price trend for a specific commodity across all specified markets over the given time period. 
        The y-axis shows the price in USD, and the x-axis shows time by year. 

    Example:
    >>> generate_line_chart(df, ('2011-01-01', '2022-01-01'), ['Osaka', 'Tokyo'], ['Rice', 'Milk'])
    # Returns a list of Altair Chart objects for 'Rice' and 'Milk' with specified configurations.
    """

    # Filter the data for the selected time period and markets
    commodities_data = data[
        data.date.between(widget_date_range[0], widget_date_range[1])
        & data.market.isin(widget_market_values)
    ].copy()
    commodities_data['date'] = commodities_data['date'].dt.to_period("M").dt.to_timestamp()
    
    charts = []

    # Change the default color scheme of Altair
    custom_color_scheme = ['#f58518', '#72b7b2', '#eeca3b', '#e45756', '#9d755d', 
                           '#54a24b', '#b279a2', '#4c78a8', '#ff9da6', '#bab0ac']
    custom_color_scale = alt.Scale(range=custom_color_scheme)

    # Create charts for each of the commodity
    for commodity in widget_commodity_values:
        # Filter the data for the specific commodity
        commodity_data = commodities_data[commodities_data.commodity.isin([commodity])]
     
        # Create the chart
        chart = alt.Chart(commodity_data, width='container', height='container').mark_line(
            size=3,
            interpolate='monotone', 
            point=alt.OverlayMarkDef(shape='circle', size=50, filled=True)
        ).encode(
            x=alt.X('date:T', axis=alt.Axis(format='%Y-%m', title='Time')),
            y=alt.Y('usdprice:Q', title='Price in USD', scale=alt.Scale(zero=False)),
            color=alt.Color('market:N', legend=alt.Legend(title='Market'), scale=custom_color_scale),
            tooltip=[
                alt.Tooltip('date:T', title='Time', format='%Y-%m'),
                alt.Tooltip('usdprice:Q', title='Price in USD', format='.2f')
            ]
#        ).properties(
#            title=alt.TitleParams(f'{commodity} Price')
        ).configure_view(
            strokeWidth=0,
#            fill='#f5f5f5'
        ).configure_axisX(
            grid=False
        ).configure_axisY(
            grid=False
        )

        # Add the chart to the list of charts
        charts.append(chart)

    return charts

def plot_country_cities(country_id, price_summary):
    """
    Generates a geographic visualization combining a country map and market points.

    This function uses Altair to plot a map of a specified country identified by its ID.
    Overlaid on the map are points representing market locations, which are provided
    in a DataFrame. Each point is marked in red and sized to stand out, with tooltips
    displaying the market name.

    Parameters:
    -----------
    country_id : int
        The unique identifier for the country which corresponds to the 'id' in the
        TopoJSON used by the function. This ID is used to filter the map to the 
        specific country.
        
    price_summary : pandas.DataFrame
        A DataFrame containing the necessary data to plot the market points on the map.
        This DataFrame must include 'latitude' and 'longitude' columns for positioning
        the points, and a 'market' column for tooltips.

    Returns:
    --------
    altair.vegalite.v4.api.LayerChart
        An Altair LayerChart object that combines a geographical map of the specified
        country and the market points. The map is shaded in light gray with white
        borders, and the market points are highlighted in red.
    """

    # Plot country map as background
    world = alt.topo_feature(data.world_110m.url, 'countries')

    country_map = alt.Chart(world, width='container', height=500).transform_filter(
        (alt.datum.id == country_id)
    )

    background = country_map.mark_geoshape(
        fill='lightgray',
        stroke='white'
    )

    # Process data
    price_summary['label'] = price_summary.apply(
        lambda row: f"{row['market']} {row['usdprice']:.2f}", axis=1
    )
    max_usdprice = price_summary['usdprice'].max()
    price_summary = price_summary.to_dict(orient='records')
    
    # Plot market points
    markets = alt.Chart(alt.Data(values=price_summary)).mark_point(
        filled=True,
        size=200
    ).encode(
        latitude='latitude:Q',
        longitude='longitude:Q',
        color=alt.Color('usdprice:Q', title='Index', scale=alt.Scale(domain=[0, max_usdprice], scheme='reds')),
        tooltip=[
            alt.Tooltip('market:N', title='Market'),
            alt.Tooltip('date:T', title='Time', format='%Y-%m'),
            alt.Tooltip('usdprice:Q', title='Index', format='.2f')
        ]
    )

    text = markets.mark_text(
        align='left',
        baseline='middle',
        dx=12,
        fontSize=12
    ).encode(
        text='label:N',
        longitude='longitude:Q',
        latitude='latitude:Q'
    )

    markets_final = alt.layer(markets, text)

    return background + markets_final

def generate_geo_chart(data, widget_date_range, widget_market_values, widget_commodity_values, country):
    """
    Generates a geographical visualization of market data within a specified country
    for a given date range, market, and commodity filters.

    This function processes input data to compute the average price of commodities
    at different markets within a country and plots these as points on a geographic map
    of the country. Each point's size and color can indicate different attributes or
    summaries of the data.

    Parameters:
    -----------
    data : pandas.DataFrame
        A DataFrame containing detailed market data including dates, market locations,
        commodity information, pricing, etc.
        
    widget_date_range : tuple
        A tuple containing start and end dates (inclusive) to filter the data. Expected
        format is (start_date, end_date) where both are either string formats that
        pandas can recognize as dates or pandas.Timestamp objects.
        
    widget_market_values : list
        A list of market names to filter the data. Only data corresponding to these
        markets will be considered.
        
    widget_commodity_values : list
        A list of commodities to filter the data. The function will calculate average
        prices only for the commodities specified in this list.
        
    country : str
        The name of the country for which the geographical chart is to be generated.
        This should be a valid country name as recognized by the `iso3166` library.

    Returns:
    --------
    altair.vegalite.v4.api.LayerChart
        An Altair LayerChart object that plots the average prices of commodities as
        points on the geographic map of the specified country. The points are placed
        according to the latitude and longitude of the markets.
    """
    
    # Default Info
    columns_to_keep = [
        "date",
        "market",
        "latitude",
        "longitude",
        "commodity",
        "unit",
        "usdprice",
    ]

    # Generate latest average price
    price_data = data[columns_to_keep]
    price_data = price_data[
        price_data.date.between(
            widget_date_range[0], widget_date_range[1]
        )
        & (price_data.commodity.isin(widget_commodity_values))
        & (price_data.market.isin(widget_market_values))
    ]
    price_data = (
        price_data.groupby(["date", "market", "latitude", "longitude"])
        .agg({"usdprice": "mean"})
        .reset_index()
    )
    price_data = price_data.set_index("date").groupby(
        ["market", "latitude", "longitude"]
    )
    price_summary = (
        price_data["usdprice"].apply(lambda x: x).reset_index()
    )
    price_summary = (
        price_summary.groupby(["market", "latitude", "longitude"])
        .last()
        .reset_index()
    )

    # Generate Geo chart
    country_id = int(countries.get(country).numeric)
    geo_chart = plot_country_cities(country_id, price_summary)
    
    return geo_chart


if __name__ == '__main__':
    pass
