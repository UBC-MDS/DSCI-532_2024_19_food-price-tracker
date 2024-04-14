# Milestone 3 Reflection

## 1. Improvements in Milestone 3

Based on the [feedback from Joel](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/77) and the Milestone 2 reflection, we've implemented several key enhancements to the dashboard in Milestone 3:

1. Addressed the problem that certain combinations of dropdown selections resulted in no data being displayed:  
  - Implemented data preprocessing steps that dynamically update the options available to a user based on their selected commodity or market
  - Ensured that empty graphs are avoided when commodities are not present in the selected markets.
 
2. Fixed the issue that Food Price Index and individual charts update asynchronously.  

3. Enhanced the visual and functional aspects of the dashboard:
  - Made the main Food Price Index charts more prominent compared to the individual commodity charts to emphasize their importance, and arranged the charts for individual commodities in a layout with two columns per row.
  - Polished the dashboard's title and sidebar for better clarity and impact.

## 2. Deviations from Our Initial Proposal

In our Milestone 1 Proposal, we planned to position a summary card to the right of every line chart. The primary goal of this card was to draw the audience's attention to key numbers before they read the chart. However, in this case, the audience would need to read from right to left across each row of the page. We realized that it is more intuitive for them to read purely from top to bottom of the entire page after making a selection in the sidebar. Therefore, we have adjusted our design for this reading pattern. Additionally, we added the captions "Overview" and "Commodities" to clearly distinguish between the role of the index and its detailed breakdown.

On the other hand, we had envisioned a "Geo View," where users could view a map of the country showing the latest commodity prices by region, facilitating regional price comparisons. This feature has not yet been implemented due to time constraints.


## 3. Limitations and Potential Future Improvements and Additions

1. Index and individual charts update slower than expected.
  - Potential improvements: Refactor plotting code and callbacks to ensure that API requests are minimized; streamline data handling to reduce computational overhead.
  
2. Current `Date` range selection feature is not convenient for choosing large date ranges.
  - Potential improvements: Update the selection tool to use "YYYY-MM" and/or "YYYY" formats instead of the "YYYY-MM-DD" format.


## 4. Inspiration from Peers (Challenging)

Inspired by other groups, we've enhanced the aesthetics of our dashboard. The dashboards of Groups 22, 20, and 16 are neat and user-friendly, and from them, we learned to make the header more prominent, organize components more neatly using cards, and make the overall color scheme more thematic. Finally, we began to implement the geo-chart view as many of our peers had success in it's ease of use and accessibility. While the chart is not fully implemented yet, the app framework to switch views and a placeholder chart is present.