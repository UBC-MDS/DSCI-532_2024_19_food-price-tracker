# Milestone 3 Reflection

## 1. Improvements in Milestone 3

Based on the feedback from Joel and the Milestone 2 reflection, we've implemented several key enhancements to the dashboard in Milestone 3:

1. Addressed the problem that certain combinations of dropdown selections resulted in no data being displayed:
- Implemented data preprocessing steps that dynamically update the options available to a user based on their selected commodity or market
- Ensured that empty graphs are avoided when commodities are not present in the selected markets.
2. Fixed the issue that Food Price Index and individual charts update asynchronously.
3. Enhanced the visual and functional aspects of the dashboard:
- Made the main Food Price Index charts more prominent compared to the individual commodity charts to emphasize their importance, and arranged the charts for individual commodities in a layout with two columns per row.
- Polished the dashboard's title and sidebar for better clarity and impact.

## 2. Features in Proposal Yet To Be Done

In our Milestone 1 Proposal, we planned a "Geo View", where users would see a map of the country with latest commodity prices by region, enabling regional price comparisons. This has not yet been implemented due to time constraints.

***Any Features Not Working Well???***

## 3. Limitations and Potential Future Improvements and Additions

1. Index and individual charts update slower than expected.
- Potential improvements: Refactor plotting code and callbacks to ensure that API requests are minimized; streamline data handling to reduce computational overhead.
2. There are inconsistencies in index performance due to missing data in some commodities.
- Potential improvements: Excluded commodities with significant gap in their temporal data (less than 50% of the period), focusing on those with more complete data.
3. Current `Date` range selection feature is not convenient for choosing large date ranges.
- Potential improvements: Update the selection tool to use "YYYY-MM" and/or "YYYY" formats instead of the "YYYY-MM-DD" format.






*Reflection from M2 (to be deleted)*

## 3. Features Not Working Well and Limitations of Current Dashboard

We have identified the following limitations in the current dashboard.
1. The `Date` range selection tool is not well-suited to large date ranges.
2. Empty graphs occur when commodities do not exist in selected markets.
3. Index and individual charts update slower than expected.
4. Index and individual charts update out of sync, worsening user experience.
5. Current summary card layouts can overflow if names are particularly long.
6. Missing data in some commodities lead to inconsistent index performance.

## 4. Potential Future Improvements and Additions

The following solutions are proposed to above limitations and will be implemented in subsequent milestones.
1. Update the `Date` range selection tool to use `YYYY-MM` and/or `YYYY` formats instead of `YYYY-MM-DD`.
2. Add data preprocessing steps that update a user's options depending on commodity or market selection.
3. Refactor plotting code and callbacks to ensure that API requests are minimized. Trim dataframes to reduce computational overhead.
4. Link callback functions for index and individual charts so they are displayed at the same time.
5. Investigate bootstrapped or altair-based alternative implementations of summary cards.
6. Remove commodities that have significant amounts of missing temporal data.