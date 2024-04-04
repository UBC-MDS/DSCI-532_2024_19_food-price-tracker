import pandas as pd
import country_converter as coco

from hdx.api.configuration import Configuration
from hdx.data.dataset import Dataset


# create HDX configuration
Configuration.create(
    hdx_site="prod",
    user_agent="DSCI-532_2024_19_food-price-tracker",
    hdx_read_only=True,
)


def fetch_country_index():
    """Fetch country index and preprocess into dataframe.

    Returns
    -------
    country_index_df : pd.DataFrame.to_json()
        JSON version of dataframe that contains all countries in the WFP dataset, and their corresponding HDX entries.
        Metadata such as URL, Start / End Dates, are included

    Examples
    --------
    >>> country_index = fetch_country_index()
    """

    cc = coco.CountryConverter()

    country_index_df = pd.read_csv(
        Dataset.read_from_hdx("global-wfp-food-prices").get_resource(0)["url"],
        parse_dates=["start_date", "end_date"],
        header=0,
        skiprows=[1],
    )

    country_index_df = country_index_df.assign(
        country=cc.pandas_convert(series=country_index_df.countryiso3, to="name_short"),
        hdx_identifier=country_index_df.url.str.rsplit("/", n=1).str[1],
    ).set_index("country")

    return country_index_df.to_json(date_format='iso', orient='split')


def fetch_country_data(country="Japan", country_index_json=fetch_country_index()):
    """Fetch and preprocess data from HDX (https://data.humdata.org/)
    Dynamically load the corresponding country dataset and preprocess.

    Parameters
    ----------
    country : str, optional
        The country of which data should be recieved. Must be within the HDX and country_index_df. By default "Japan"
    country_index_json : pd.DataFrame, optional
        Index dataset from "global-wfp-food-prices" in the HDX, the output from fetch_country_index_df(). By default, the output from fetch_country_index_df().

    Returns
    -------
    country_json : pd.DataFrame.to_json()
        JSON version of dataframe of WFP data from the given country, retrieved from the HDX and minimially preprocessed.

    Examples
    --------
    >>> country_json = fetch_country_data("Japan")
    """

    columns_to_keep = [
        "date",
        "market",
        "latitude",
        "longitude",
        "commodity",
        "unit",
        "usdprice",
    ]

    country_index_df = pd.read_json(country_index_json, orient='split')

    country_df = pd.read_csv(
        Dataset.read_from_hdx(
            country_index_df.loc[country, "hdx_identifier"]
        ).get_resource(0)["url"],
        parse_dates=["date"],
        header=0,
        skiprows=[1],
    )[columns_to_keep]

    return country_df.to_json(date_format='iso', orient='split')


if __name__ == "__main__":
    pass
