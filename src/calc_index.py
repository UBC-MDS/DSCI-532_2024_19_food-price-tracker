import numpy as np
import pandas as pd

def generate_food_price_index_data(data, widget_market_values, widget_commodity_values):
    """
    FIXME: add docstring
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



# def generate_food_price_index_data(data, widget_date_range, widget_market_values):
#     """
#     Generate food price index data based on the input data, date range, and market values.

#     Parameters
#     ----------
#     data : pandas.DataFrame
#         Input food price data.
#     widget_date_range : tuple
#         A tuple containing the start and end dates for filtering the data.
#     widget_market_values : list
#         A list of market used to filter the data.

#     Returns
#     -------
#     pandas.DataFrame
#         DataFrame containing the food price index data with columns: date, market, latitude, longitude, commodity, unit, usdprice.

#     Examples
#     --------
#     >>> import pandas as pd
#     >>> data = pd.DataFrame({
#     ...     'date': ['2022-01-01', '2022-01-01', '2022-01-02'],
#     ...     'market': ['A', 'B', 'A'],
#     ...     'latitude': [1, 2, 1],
#     ...     'longitude': [1, 2, 1],
#     ...     'commodity': ['Rice', 'Radish', 'Sugar'],
#     ...     'unit': ['kg', 'kg', 'kg'],
#     ...     'usdprice': [1.0, 2.0, 3.0]
#     ... })
#     >>> widget_date_range = ('2022-01-01', '2022-01-02')
#     >>> widget_market_values = ['A', 'B']
#     >>> generate_food_price_index_data(data, widget_date_range, widget_market_values)
#     """

#     # Default Info
#     columns_to_keep = [
#         "date",
#         "market",
#         "latitude",
#         "longitude",
#         "commodity",
#         "unit",
#         "usdprice",
#     ]
#     food_price_index_dict = {
#         "Rice": 0.156,
#         "Radish": 0.23,
#         "Sugar": 0.036,
#     }

#     # Generate Food Price Index Data
#     price_index_data = data[columns_to_keep]
#     price_index_data = price_index_data[
#         price_index_data.date.between(
#             widget_date_range[0], widget_date_range[1]
#         )
#         & (price_index_data.market.isin(widget_market_values))
#     ]
#     price_index_data["index_weight"] = price_index_data[
#         "commodity"
#     ].apply(
#         lambda x: food_price_index_dict[x]
#         if x in food_price_index_dict
#         else np.nan
#     )
#     price_index_data["usdprice"] = (
#         price_index_data["usdprice"]
#         * price_index_data["index_weight"]
#     )
#     price_index_data["commodity"] = "Food Price Index"
#     price_index_data["unit"] = "PPL"
#     price_index_data = price_index_data.dropna()
#     price_index_data = (
#         price_index_data.groupby(columns_to_keep[:-1])
#         .agg({"usdprice": "sum", "index_weight": "count"})
#         .reset_index()
#     )
#     price_index_data = price_index_data[
#         price_index_data.index_weight
#         == len(food_price_index_dict)
#     ].drop(columns=["index_weight"])

#     return price_index_data