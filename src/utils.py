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