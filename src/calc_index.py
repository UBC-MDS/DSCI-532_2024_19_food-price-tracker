import numpy as np
import pandas as pd

def generate_food_price_index_data(data, widget_market_values, widget_commodity_values):
    """
    Generate food price index data based on the selected markets and commodities.

    Parameters
    ----------
    data : pandas.DataFrame
        The dataset containing price information for various commodities across different markets.
        
    widget_market_values : list
        A list of selected market names to filter the data.
        
    widget_commodity_values : list
        A list of selected commodity names to include in the food price index calculation.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the original data appended with the calculated food price index
        for the selected markets and commodities. 

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
    >>> widget_market_values = ['A', 'B']
    >>> widget_commodity_values = ['Rice', 'Radish', 'Sugar']
    >>> generate_food_price_index_data(data, widget_market_values, widget_commodity_values)
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
    
    # Generate Food Price Index Data
    price_data = data[columns_to_keep]
    price_data = price_data[
        (price_data.commodity.isin(widget_commodity_values))
        & (price_data.market.isin(widget_market_values))
    ]

    # Calculate index (formula: arithmetic average of the index by date and market)
    index = (
        price_data.groupby(
            ["date", "market", "latitude", "longitude"]
        ).agg({
            "usdprice": "mean"
        })
    ).reset_index()

    # Aggregate price index back to the price data
    index['commodity'] = "Food Price Index"
    index["unit"] = "PPL"
    price_data = pd.concat((price_data, index), axis=0)

    return price_data
