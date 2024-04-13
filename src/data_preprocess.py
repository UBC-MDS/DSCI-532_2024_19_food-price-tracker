import pandas as pd
from io import StringIO
import itertools

def filter_major_data(data, date_abundance_threshold=0.5, market_abundance_threshold=0.7):
    """
    Filter major data based on specified thresholds for date and market abundance.

    Parameters
    ----------
    data : pandas.DataFrame
        Input food price raw data.
    date_abundance_threshold : float, optional
        The threshold percentage of data existence for each (commodity, market) pair relative to the full duration length. Defaults to 0.5.
    market_abundance_threshold : float, optional
         The threshold percentage of markets where data of a commodity exists, relative to the total number of markets. Defaults to 0.7.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing major data filtered based on the specified thresholds.

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

    clean_data_df = data

    # Rule 0 - Deduplication on unit and (date, commodity, market)
    map_df = (
        clean_data_df.groupby(["commodity", "unit"])
        .agg({"unit": "count"})
        .groupby(["commodity"])
        .idxmax()
    )
    map_df["unit"] = map_df["unit"].apply(lambda x: x[1])
    map_df = map_df.reset_index()
    clean_data_df = clean_data_df.merge(
        map_df, how="inner", on=["commodity", "unit"]
    )
    clean_data_df = (
        clean_data_df[columns_to_keep]
        .groupby(columns_to_keep[:-1])
        .first(["usdprice"])
        .reset_index()
    )

    # Rule 1 - data existence for each (commodity, market) pair relative to the full duration length >= x%
    num_date = clean_data_df["date"].nunique()
    map_df = (
        clean_data_df.groupby(["market", "commodity"]).agg(
            {"usdprice": "count"}
        )
        >= date_abundance_threshold * num_date
    )
    map_df = map_df.rename(columns={"usdprice": "is_kept"})
    clean_data_df = clean_data_df.merge(
        map_df, how="left", on=["market", "commodity"]
    )
    clean_data_df = clean_data_df[
        clean_data_df["is_kept"] == True
    ].drop(columns=["is_kept"])

    # Rule 2 - data of a commodity exists, relative to the total number of markets >= x%
    num_market = clean_data_df["market"].nunique()
    map_df = (
        clean_data_df.groupby(["commodity"]).agg(
            {"market": "nunique"}
        )
        >= market_abundance_threshold * num_market
    )
    map_df = map_df.rename(columns={"market": "is_kept"})
    clean_data_df = clean_data_df.merge(
        map_df, how="left", on=["commodity"]
    )
    clean_data_df = clean_data_df[
        clean_data_df["is_kept"] == True
    ].drop(columns=["is_kept"])

    return clean_data_df

def fill_missing_data(data, method="forward"):
    """
    Fills missing values in the USD price column based on specified method.

    Parameters
    ----------
    data : pandas.DataFrame
        Input food price raw data.
    method : str, optional
        Method to fill missing values. Default is "forward" (forward fill).

    Returns
    -------
    pandas.DataFrame
        A DataFrame with missing values filled based on the specified method.

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

    # Generate dataframe with full combinations of factors
    full_data_df = pd.DataFrame(
        itertools.product(
            # pd.date_range(data["date"].min(), data["date"].max(), freq='MS') + pd.DateOffset(days=14),
            data["date"].unique(),
            data["market"].unique(),
            data["commodity"].unique(),
        ),
        columns=["date", "market", "commodity"],
    )

    # Fill the missing value per (date, commodity, market)
    full_data_df = full_data_df.merge(
        data, how="left", on=["date", "market", "commodity"]
    )
    if method == "forward":
        full_data_df = full_data_df.merge(
            full_data_df.groupby(
                ["market", "commodity"]
            ).ffill(),
            how="inner",
            left_index=True,
            right_index=True,
            suffixes=("_drop", None),
        )
    full_data_df = full_data_df[columns_to_keep].dropna(
        subset=["usdprice"], axis=0
    )

    return full_data_df

def get_clean_data(data_json):
    """
    Returns JSON data containing cleaned data.

    Parameters
    ----------
    data_json : str
        JSON string containing raw data.

    Returns
    -------
    str
        JSON string containing cleaned major data.
    """

    data_df = pd.read_json(StringIO(data_json), orient='split')
    data_df = filter_major_data(data_df)
    data_df = fill_missing_data(data_df)

    return data_df.to_json(date_format='iso', orient='split')

if __name__ == "__main__":
    pass