# Milestone 1 Proposal: Food Price Tracker **(check 1000 word limit)**
Course project for DSCI 532 - Data Visualization II as a part of the UBC Master of Data Science program. 

Celeste Zhao, John Shiu, Simon Frew, Tony Shum


## 1. Motivation and purpose
We are a team of data scientists representing a food-focused NGO based in Canada (e.g., Food Banks Canada, TBC). 
Our mission is to provide accessible solutions for understanding and addressing global food price trends. 
Our newly developed tool, **FIXME: The Food Price Tracker** is designed to provide accessible yet comprehensive insights into these trends for a range of non-technical stakeholders, including public-sector policymakers and economists, NGO analysts, private-sector food suppliers, and the general public.

### Problem Statement
There is no denying that reliable food pricing information is essential for impactful decision-making across various sectors; such as informing food policies to combat shortages in disadvantaged regions, or optimizing business strategy to capitalize on lucrative markets and identify opportunities for growth. 
However, we observed a lack of open, easy-to-use online platforms that provide a comprehensive overview of global food price trends with resolution to regional levels. 
Primary challenges we observed included 1) scattered and unorganized regional data, which required technical expertise to navigate, and 2) that existing platforms are unintuitive and therefore difficult for non-technical stakeholders to utilize effectively in their daily operations.

In response to this challenge, we propose the development of an interactive, user-friendly data visualization platform for global trends in food prices with regional resolution. 
Our platform aims to empower stakeholders to extract insights and make informed decisions regarding food prices worldwide. 
Key features and use cases include:

1. Regional resolution of food prices, allowing policymakers to monitor and implement targeted preventive measures if needed.
2. Historic food price trends, enabling businesses to enhance planning and resource allocation strategies. 
3. Breakdowns by food category, providing specificity required for a given industry or to inform a focused intervention. 
4. Accessible food price index information for the general public, facilitating financial management and awareness of cost-of-living fluctuations.

By offering our platform, we aim to enhance collaboration across sectors to address food-related challenges on a global scale.

## 2. Description of the data
The dataset to be used in our project is the Global Food Prices dataset available on the open platform The Humanitarian Data Exchange (HDX) (https://data.humdata.org/dataset/global-wfp-food-prices). This dataset originates from the World Food Programme Price Database and encompasses recorded prices for food items such as maize, rice, beans, fish, and sugar. The price data spans 98 countries and approximately 3,000 markets, and its historical range extends back to 1992 for certain countries, although many countries have started reporting from 2003 onwards. The dataset is updated weekly but primarily comprises monthly data entries, and the data is organized by country due to its extensive volume.

For our visualization, we will focus on the subset converning the Japanese market and covering the time from 2011 to 2020. This subset contains around 1,180 records of food prices. Each record within the dataset has 14 variables:
- Date of the record: `date`.
- Market information: name - `market`; city or province of the market - `admin1`, `admin2`; geographical coordinates - `latitude`, `longitude`.
- Food item information: type and name - `category`, `commodity`; item unit - `unit` (e.g. 5kg).
- Details on pricing: type and flag - `pricetype` (e.g., retail, wholesale), `priceflag` (typically actual); price in local currency and its equivalent in USD - `currency`, `price`, `usdprice` (converted at the current exchange rate).

In addition to these existing variables, we will derive several new metrics to enhance our analysis:
- Annual average price: converting monthly price data for each food item into annual metrics to facilitate year-over-year comparisons.
- Food price growth rate: calculating the rate of price growth for each food item on a monthly or yearly basis, both sequentially and year-over-year.
- **(Optional) Ratio of food price to GNI (Gross National Income) per capita: dividing the price of a specific food item by the country's per capita income, allowing for international comparisons (data on GNI required).**

“There should be a clear link to how the dataset and the variables you describe will help you solve your target audience's problem.” (TBU)


## 3. Research questions and usage scenarios
Research questions and user stories are provided by sector below.

### Public Sector
Ms. Tiffany is an executive with the Ministry of Health, Labour and Welfare in Japan. 
Her role involves policy-making related to food supply, demand, and price dynamics. 
Her primary goal is to ensure that food prices across regions and major categories remain at acceptable levels to safeguard public well-being. 

#### User Story
- Ms. Tiffany navigates to the dashboard, which displays food price indices and food categories.
- She notices the price of rice nearing a threshold of concern and investigates.
- Ms. Tiffany focuses on rice and examines the 2-year trend. 
- She views the geospatial chart and to examine regional differences and sees that the Kansai region is higher than the national average.
- Ms. Tiffany proposes policy measures to combat this trend.
- She safeguards public well-being in the affected region through the use of our platform.

### Private Sector
Mr. Joel operates a business specializing in the supply and trade of cereals and tubers. 
He needs to analyze market trends and price data for these commodities to identify opportunities for profit.

#### User Story
- Mr. Joel logs into the dashboard and views key commodities: wheat, potatoes, and rice.
- He examines recent price trends to identify profitable commodities. 
- Mr. Joel increases the timeframe to visualize seasonal patterns, and sees the price of potatoes will increase in the coming months. He adjusts his strategy accordingly.
- Exploring the geospatial charts, he sees that demand is focused in a specific region. 
- Mr. Joel reallocates stock to capitalize on the high demand. 
- He improves financial returns and meets market demand via our platform. 

### General Public
Mr. Daniel is a concerned citizen who has noticed a steady increase in grocery prices in the last three years. 
He is unsure whether this is just due to his purchasing patterns, as relatives across the country have not expressed a similar sentiment. 
It is coming to the new year, and Mr. Daniel needs to identify whether his budget needs to be adjusted and whether it is worth contacting his local government about the issue. 

#### User Story 
- Mr. Daniel logs into the platform and searches for his country.
- He examines retrieved prices and extends the timeframe to include the last five years.
- He sees that food prices have indeed increased over the given timeframe.
- He transitions to a geospatial view, and in his relative's region, prices have not increased. 
- Mr. Daniel now can plan his budget for the upcoming year and resolves to contact his local governmental official to raise this issue.

## 4. App sketch and brief description
