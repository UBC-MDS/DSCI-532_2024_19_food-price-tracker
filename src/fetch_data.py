# Simon Frew, 2024
# Script to fetch and preprocess data for food_price_tracker
import country_converter as coco
import pandas as pd

from hdx.utilities.easy_logging import setup_logging
from hdx.api.configuration import Configuration
from hdx.data.dataset import Dataset

cc = coco.CountryConverter()


def fetch_country_index(): 
    """Fetch country index and preprocess into dataframe. 

    Returns
    -------
    country_index_df : pd.DataFrame
        DataFrame that contains all countries in the WFP dataset, and their corresponding HDX entries.
        Metadata such as URL, Start / End Dates, are included
    """

    cc = coco.CountryConverter()
    Configuration.create(hdx_site="prod", user_agent="DSCI-532_2024_19_food-price-tracker", hdx_read_only=True)

    country_index_df = pd.read_csv(
        Dataset.read_from_hdx("global-wfp-food-prices").get_resource(0)["url"], 
        parse_dates=["start_date", "end_date"], 
        header=0, 
        skiprows=[1]
    )

    country_index_df = country_index_df.assign(
        country = cc.pandas_convert(
            series = country_index_df.countryiso3, 
            to = "name_short"
        ), 
        hdx_identifier = country_index_df.url.str.rsplit("/", n=1).str[1]
    ).set_index("country")

    return country_index_df


def fetch_country_data(country = "Japan", country_index_df = fetch_country_index_df()): 
    """Fetch and preprocess data from HDX (https://data.humdata.org/)
    Dynamically load the corresponding country dataset and preprocess.

    Parameters
    ----------
    country : str, optional
        The country of which data should be recieved. Must be within the HDX and country_index_df. By default "Japan"
    country_index_df : pd.DataFrame, optional
        Index dataset from "global-wfp-food-prices" in the HDX, the output from fetch_country_index_df(). By default, the output from fetch_country_index_df().

    Returns
    -------
    country_df : pd.DataFrame
        Dataframe of WFP data from the given country, retrieved from the HDX and minimially preprocessed. 
    """

    Configuration.create(hdx_site="prod", user_agent="DSCI-532_2024_19_food-price-tracker", hdx_read_only=True)

    country_index_df.loc[country, "hdx_identifier"]

    return country_df


if __name__ == "__main__": 
    country_index_df = fetch_country_index()
    print(country_index_df.head())

    country_df = fetch_country_data("Japan", country_index_df)
    print(country_df)

