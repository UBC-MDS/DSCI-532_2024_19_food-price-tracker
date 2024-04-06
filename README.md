# Food Price Tracker

[![GitHub issues](https://img.shields.io/github/issues/UBC-MDS/DSCI-532_2024_19_food-price-tracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/DSCI-532_2024_19_food-price-tracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commits/main)
[![GitHub release](https://img.shields.io/github/release/UBC-MDS/DSCI-532_2024_19_food-price-tracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/releases)

![logo](https://raw.githubusercontent.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/img/logo.png)
*Created by DALL.E*

## Welcome

Thank you for visiting the Food Price Tracker project repository!
The project aims to provide an intuitive, interactive data visualization platform for drawing food price insights and enhancing cross-sector collaboration to address worldwide food-related challenges.
We invite you to utilize our Food Price Tracker and welcome any contributions towards its enhancement.

## Motivation and Purpose

Access to reliable food pricing information is crucial for informed decision-making in public policymaking and business strategy. However, we observed a lack of open, easy-to-use online platforms providing comprehensive global trends of food price with regional details. Key challenges identified include 1) scattered and unorganized regional data requiring technical expertise to navigate, and 2) existing platforms being unintuitive for non-technical stakeholders for effective daily use.

To address this, we have developed this interactive platform for global food price trends with regional resolution. Our platform aims to empower stakeholders with insights for informed decision-making on food prices worldwide. We wish to enhance collaboration across sectors to address food-related challenges on a global scale.

## Contributors

Celeste Zhao, John Shiu, Simon Frew, Tony Shum

## Usage - For Users

### Website Link

Food Price Tracker can be accessed through the following link: (https://dsci-532-2024-19-food-price-tracker.onrender.com/)

The dashboard is composed of a sidebar for user input and a data display section. In the sidebar, you can select the country, time range, specific commodities, and markets you wish to view. In the data display section, you can see the actual and average value, Month-over-Month and Year-over-Year change rates of the overall Food Price Index as well as of each commodity.

### Usage Demonstration

***put the gif link***

### Need Support?

If you want to report a problem or give an suggestion, we would love for you to [open an issue](../../issues) at this github repository and we will get on to it in a timely manner.

## Usage - For Developers

### Installation For Local Developing

1. Clone this repository to your computer.

```bash
 git clone https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker
```
```bash
 cd DSCI-532_2024_19_food-price-tracker/
```

2. Install the conda environment.

```bash
 conda env create -f environment.yml
```

3. Activate the installed environment.

```bash
 conda activate food_price_tracker
```

4. Start the dashboard.

```bash
 python -m src.app
```

### Contributing

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`food_price_tracker` was created by Celeste Zhao, John Shiu, Simon Frew, Tony Shum. It is licensed under the terms of the MIT license and the Attribution 4.0 International (CC BY 4.0 LEGAL CODE).
