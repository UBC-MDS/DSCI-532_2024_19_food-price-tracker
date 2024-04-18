import pandas as pd

def convert_date(input, target='label'):
    """
    Converts date between label and datetime formats.

    Parameters
    ----------
    input_date : datetime or float
        Input date to be converted.
    target : str
        Target format for conversion, either 'label' for label format or 'datetime' for datetime format. Default is 'label'.

    Returns
    -------
    float or Timestamp
        Converted date in the specified format.

    """
    if target == 'label':
        year = input.year
        month = input.month
        output = year + (month-1)/12
    elif target == 'datetime':
        year = int(input // 1)
        month = round((input % 1)*12 + 1)
        day = 15
        output = pd.to_datetime(f'{year}/{month}/{day}')

    return output
    
def compile_widget_state(
        toggle=None,
        country=None, 
        date_range=None, 
        commodities=None, 
        markets=None
):
    """
    Record the state of widget so dynamic charting can be achieved. 
    
    Parameters
    ----------
    toggle : bool
        True: enable geo-area chart. False: enable typical commodities chart.

    country : str
        string of selected country, e.g., "Japan"

    date_range : tuple of str or datetime
        The starting and ending date in a tuple for filtering the data used in the charts.

    commodities : list
        A list of commodities to be included in the food price index calculation.

    markets : list
        A list of market names from which the data will be filtered to generate the charts.
    

    Returns
    -------
    dict
        dict of widget-state compiled from input variables
    """
    widget_state = {
        "toggle": toggle, 
        "country": country, 
        "date_range": date_range, 
        "commodities": commodities,
        "markets": markets
    }
    
    return widget_state
