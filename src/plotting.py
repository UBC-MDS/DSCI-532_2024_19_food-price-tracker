import numpy as np
import pandas as pd
import altair as alt
alt.data_transformers.enable('vegafusion')

def generate_food_price_index_data(data, widget_date_range, widget_market_values):
    """
    Generate food price index data based on the input data, date range, and market values.

    Parameters
    ----------
    data : pandas.DataFrame
        Input food price data.
    widget_date_range : tuple
        A tuple containing the start and end dates for filtering the data.
    widget_market_values : list
        A list of market used to filter the data.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the food price index data with columns: date, market, latitude, longitude, commodity, unit, usdprice.

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
    >>> generate_food_price_index_data(data, widget_date_range, widget_market_values)
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
    food_price_index_dict = {
        "Rice": 0.156,
        "Radish": 0.23,
        "Sugar": 0.036,
    }

    # Generate Food Price Index Data
    price_index_data = data[columns_to_keep]
    price_index_data = price_index_data[
        price_index_data.date.between(
            widget_date_range[0], widget_date_range[1]
        )
        & (price_index_data.market.isin(widget_market_values))
    ]
    price_index_data["index_weight"] = price_index_data[
        "commodity"
    ].apply(
        lambda x: food_price_index_dict[x]
        if x in food_price_index_dict
        else np.nan
    )
    price_index_data["usdprice"] = (
        price_index_data["usdprice"]
        * price_index_data["index_weight"]
    )
    price_index_data["commodity"] = "Food Price Index"
    price_index_data["unit"] = "PPL"
    price_index_data = price_index_data.dropna()
    price_index_data = (
        price_index_data.groupby(columns_to_keep[:-1])
        .agg({"usdprice": "sum", "index_weight": "count"})
        .reset_index()
    )
    price_index_data = price_index_data[
        price_index_data.index_weight
        == len(food_price_index_dict)
    ].drop(columns=["index_weight"])

    return price_index_data

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

    # Obtain Food Price Index data
    price_index_data = generate_food_price_index_data(data, widget_date_range, widget_market_values)
    widget_commodity_values = [
        "Food Price Index"
    ] + widget_commodity_values

    # Generate latest average price and period-over-period change
    price_data = data[columns_to_keep]
    price_data = pd.concat(
        [price_data, price_index_data],
        axis=0,
        ignore_index=True,
    )
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
        charts.append(chart.interactive())

    return charts

if __name__ == '__main__':
    pass