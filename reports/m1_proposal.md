# Milestone 1 Proposal: Food Price Tracker
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
TODO


## 3. Research questions and useage scenarios
Research questions and user stories are provided by sector below.

### Public Sector
Ms. Tiffany is an executive with the Ministry of Health, Labour and Welfare in Japan. 
Her role involves policy-making related to food supply, demand, and price dynamics. 
Her primary goal is to ensure that food prices across regions and major categories remain at acceptable levels to safeguard public well-being. 
In response to concerning trends in available data, she seeks to draft policy or recommend immediate interventions for the government to enact.

#### User Story
- When Ms. Tiffany accesses our platform and lands on the dashboard, she immediately sees the overview of current food price index and the price levels of major food categories displayed.
- She notices that the price of rice is nearing a governmental threshold of concern and decides to investigate further.
- Ms. Tiffany selects the rice category and adjusts the time period to view recent 2-year price trends. 
She identifies a slight upward trend in rice prices over the past month that arouses her concern.
- To understand if this trend is national or regional, she views the geospatial chart provided illustrating rice price distributions across regions. 
She observes that prices in Kansai region are significantly higher than the national average.
- Ms. Tiffany shares her findings and conclusions with stakeholders and proposes policy measures to lower rice prices in the affected region. 
She also notifies relavent departments to consider emergency aid operations to address any immediate food demand concerns before her policy normalizes rice prices.
- She safeguards public well-being in the affected region through the use of our platform.

### Private Sector
Mr. Joel operates a business specializing in the supply and trade of cereals and tubers. 
He needs to analyze market trends and price data for these commodities to identify mismatches in supply and demand, seeking to optimize profit margins. 
He wants to use food price data analysis to detect profitable opportunities and adjust his business operations to increase returns.

#### User Story
- Mr. Joel logs into the data platform and sets up his dashboard to display trend charts for his key commodities like wheat, potatoes, and rice.
- He examines the price trends over selected time frames to spot any significant uptrend or downtrend, and determines the profitable commodities his business should focus on.
- Mr. Joel adjusts the time frame of the charts to identify seasonal patterns of the prices of commodities, and notices a seasonal upward trend for the price of potatoes in the coming months. 
He decides to import more potato and allocates more space in his warehouse for the stock.
- Mr. Joel then explores the geospatial charts, which show the regional price distribution for his main products, identifying areas with higher price levels that indicate a demand surplus.
- Based on the findings, he considers reallocating his stock to regions where he can sell at higher prices and plans his logistics to align with these insights.
- He achieves a higher return on his food business and solves demand mismatch through the use of our platform.

### General Public
Mr. Daniel is a concerned citizen who has noticed a steady increase in grocery prices in the last three years. 
He is unsure whether this is just due to his purchasing patterns, as relatives across the country have not expressed a similar sentiment. 
It is coming to the new year, and Mr. Daniel needs to identify whether his budget needs to be adjusted, and whether it is worth contacting his local government about the issue. 

#### User Story 
- Mr. Daniel logs into the platform and searches for his country.
- He examines retrieved prices and extends the timeframe to include the last five years, attempting to ascertain whether food prices have truly increased. 
- He sees that food prices have indeed increased over the given timeframe, and appear to be increasing faster in recent months. 
- While this is concerning to him, Mr. Daniel is confused that his relatives across the country have not experienced the same thing. 
- He transitions to a geospatial view, which breaks his country into its constituent regions. 
The five-year trend is now highlighted by region. 
- From this, it is evident that his relatives are also correct - the price trends in their region have not increased significantly over the last five years. 
- Mr. Daniel has a complete understanding of regional trends in food prices, knows how best to plan his budget for the upcoming year, and resolves to contact his local governmental official to raise this issue.

## 4. App sketch and brief description