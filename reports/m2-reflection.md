# Milestone 2 Reflection (500 word limit)

## 1. Features Implemented in Milestone 2 Dashboard

Our dashboard now supports displaying food prices for selected conditions, including time, country, markets, and commodities. The dashboard is composed of a sidebar for user input and a data display section.

### 1. Sidebar
Users can select the country, time range, specific commodities, and markets they wish to view.
- `Country` dropdown: Allows users to choose the country they are interested in.
- `Date` selection: Enables selection of the time range for data viewing.
- `Commodities` dropdown: Users can select the range of commodities to be examined.
- `Markets` dropdown: Allows for the selection of specific markets.
- View toggle (future update): Switches to a map perspective "Geo view".
- `Manual Trigger`: Runs the dashboard based on selected conditions.

### 2. Data Display
Displays food price information based on selected conditions.
- **Food price index summary card**: Shows the average value, Month-over-Month change rate, and Year-over-Year change rate of the Food Price Index across all selected commodities within the chosen time and market range.
- **Food price index line chart**: Displays the Food Price Index values over time across different markets based on selected conditions.
- **Individual commodity summary card**: Below a separator, this shows the average price, Month-over-Month change rate, and Year-over-Year change rate of USD prices for each commodity within the selected time and market range.
- **Individual commodity line charts**: Displays the USD prices over time for each commodity across different markets based on selected conditions.

## 2. Features in Proposal Yet To Be Done

In our Milestone 1 Proposal, we planned a "Geo View", where users would see a map of the country with latest commodity prices by region, enabling regional price comparisons. This has not yet been implemented due to time constraints.  

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