import numpy as np
import pandas as pd
import altair as alt
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

    # # Obtain Food Price Index data
    # price_index_data = generate_food_price_index_data(data, widget_date_range, widget_market_values)
    # widget_commodity_values = []
    #     "Food Price Index"
    # ] + widget_commodity_values

    # Generate latest average price and period-over-period change
    price_data = data[columns_to_keep]
    # price_data = pd.concat(
    #     [price_data, price_index_data],
    #     axis=0,
    #     ignore_index=True,
    # )
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
    price_data = price_data.set_index("date").groupby(
        ["commodity", "unit"]
    )
    price_summary = (
        price_data["usdprice"].apply(lambda x: x).reset_index()
    )
    price_summary["mom"] = (
        price_data["usdprice"]
        .apply(lambda x: x.pct_change(1))
        .reset_index()["usdprice"]
    )
    price_summary["yoy"] = (
        price_data["usdprice"]
        .apply(lambda x: x.pct_change(12))
        .reset_index()["usdprice"]
    )
    price_summary = (
        price_summary.groupby(["commodity", "unit"])
        .last()
        .reset_index()
    )

    # Generate Figure charts
    charts = []
    for item in widget_commodity_values:
        chart = (
            alt.Chart(
                price_summary[price_summary.commodity == item],
                title=alt.Title(
                    "Latest Average", align="right"
                ),
            )
            .mark_rect()
            .encode()
            .properties(width=180, height=180)
        )
        item_value = chart.mark_text(
            baseline="middle", dy=-5
        ).encode(
            text=alt.Text("usdprice:Q", format="$.2f"),
            size=alt.value(40),
        )
        item_title = (
            chart.mark_text(dy=-40, fontStyle="Italic")
            .encode(
                text="label:N",
                color=alt.value("black"),
                opacity=alt.value(0.7),
                size=alt.value(16),
            )
            .transform_calculate(
                label="datum.commodity + ' /' + datum.unit"
            )
        )
        mom_value = chart.mark_text(dy=20, align="left").encode(
            text=alt.Text("mom:Q", format="+.2%"),
            color=alt.condition(
                "datum.mom<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(16),
        )
        mom_title = chart.mark_text(
            dy=20, align="right"
        ).encode(
            text=alt.value("MoM  :"),
            color=alt.condition(
                "datum.mom<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(16),
        )
        yoy_value = chart.mark_text(dy=40, align="left").encode(
            text=alt.Text("yoy:Q", format="+.2%"),
            color=alt.condition(
                "datum.yoy<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(16),
        )
        yoy_title = chart.mark_text(
            dy=40, align="right"
        ).encode(
            text=alt.value("YoY  :"),
            color=alt.condition(
                "datum.yoy<0",
                alt.ColorValue("red"),
                alt.ColorValue("green"),
            ),
            size=alt.value(16),
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
        #charts.append(chart.interactive())
        charts.append(chart)

    return charts

def generate_line_chart_fpi(data, widget_date_range, widget_market_values):
    """
    Generates an interactive line chart visualizing the Food Price Index over time.

    This function filters the Food Price Index data based on the specified date range and market values. 
    It then creates an interactive Altair line chart with custom tooltip formatting, axis titles, and legend configuration. 
    The chart displays the Food Price Index on the y-axis and time on the x-axis, represented by years. 

    Parameters:
    - data (DataFrame): The source Pandas DataFrame containing the Food Price Index data.
    - widget_date_range (tuple): A tuple containing the start and end dates (inclusive) as strings in 'YYYY-MM-DD' format to filter the data by.
    - widget_market_values (list): A list of markets to include in the chart.

    Returns:
    - price_index_line_chart (alt.Chart): An Altair Chart object representing the line chart of the Food Price Index data.

    The `generate_food_price_index_data` function is called within to process the raw data, which is expected to be defined externally to this function.

    Example:
    >>> generate_line_chart_fpi(df, ('2011-01-01', '2022-01-01'), ['Osaka', 'Tokyo'])
    # Returns an Altair Chart object with the Food Price Index line chart.
    """

    # Obtain Food Price Index data
    price_index_data = generate_food_price_index_data(data, widget_date_range, widget_market_values)

    # Create a line chart for Food Price Index
    price_index_line_chart = alt.Chart(price_index_data).mark_line().encode(
        x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Year')),
        y=alt.Y('usdprice:Q', title='Food Price Index', scale=alt.Scale(zero=False)),
        color=alt.Color('market:N', legend=alt.Legend(title='Market')),
        tooltip=[
            alt.Tooltip('date:T', title='Time', format='%b, %Y'),
            alt.Tooltip('usdprice:Q', title='Value', format='.2f')
        ]
    ).properties(
        title=alt.TitleParams('Food Price Index')
    ).configure_axis(
            grid=False
    ).interactive()

    return price_index_line_chart

def generate_line_chart_commodities(data, widget_date_range, widget_market_values, widget_commodity_values):
    """
    Generates a list of interactive line charts, each representing the price trends of different commodities over time within specified marketplaces.

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
    >>> generate_line_chart_commodities(df, ('2011-01-01', '2022-01-01'), ['Osaka', 'Tokyo'], ['Rice', 'Milk'])
    # Returns a list of Altair Chart objects for 'Rice' and 'Milk' with specified configurations.
    """

    # Filter the data for the selected time period and markets
    commodities_data = data[
        data.date.between(widget_date_range[0], widget_date_range[1])
        & data.market.isin(widget_market_values)
    ]
    
    charts = []

    # Create charts for each of the commodity
    for commodity in widget_commodity_values:
        # Filter the data for the specific commodity
        commodity_data = commodities_data[commodities_data.commodity.isin([commodity])]
     
        # Create the chart
        chart = alt.Chart(commodity_data).mark_line().encode(
            x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Year')),
            y=alt.Y('usdprice:Q', title='Price in USD', scale=alt.Scale(zero=False)),
            color=alt.Color('market:N', legend=alt.Legend(title='Market')),
            tooltip=[
                alt.Tooltip('date:T', title='Time', format='%b, %Y'),
                alt.Tooltip('usdprice:Q', title='Price in USD', format='.2f')
            ]
        ).properties(
            title=alt.TitleParams(f'{commodity} Price')
        ) #.configure_axis(
        #    grid=False
        #) #.interactive()

        # Add the chart to the list of charts
        charts.append(chart)

    return charts

if __name__ == '__main__':
    pass
