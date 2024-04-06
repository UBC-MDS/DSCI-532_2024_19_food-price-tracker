# Milestone 2 Reflection (500 words limit)

## 1. Features Implemented in Milestone 2 Dashboard

Our dashboard now supports displaying food prices for selected conditions, including time, country, markets, and commodities. The dashboard is composed of a sidebar for user input and a data display section.

1. Sidebar: Users can select the country, time range, specific commodities, and markets they wish to view.
- `Country` dropdown: Allows users to choose the country they are interested in.
- `Date` selection: Enables selection of the time range for data viewing.
- `Commodities` dropdown: Users can select the range of commodities to be examined.
- `Markets` dropdown: Allows for the selection of specific markets.
- View toggle (future update): Switches to a map perspective "Geo view".
- `Manual Trigger`: Runs the dashboard based on selected conditions.

2. Data Display Section: Displays food price information based on selected conditions.
- Food price index tracking chart: Shows the average value, Month-over-Month change rate, and Year-over-Year change rate of the Food Price Index across all selected commodities within the chosen time and market range.
- Food price index line chart: Displays the Food Price Index values over time across different markets based on selected conditions.
- Individual commodity tracking charts: Below a separator, this shows the average price, Month-over-Month change rate, and Year-over-Year change rate of USD prices for each commodity within the selected time and market range.
- Individual commodity line charts: Displays the USD prices over time for each commodity across different markets based on selected conditions.

## 2. Features in Proposal Yet To Be Done

In our Milestone 1 Proposal, we planed to implement a toggle to switch from the current view to a "Geo view". In the Geo view, users would see a country map with the latest prices from various markets for specific commodities on a given date, enabling regional price comparisons. However, due to the substantial workload and limited time, this feature has not yet been implemented.

## 3. Features Not Working Well and Limitations of Current Dashboard

We have identified the following features as not working well by far:
1. Refreshing is not triggered when only the start date is adjusted in the `Date` selection.
2. The `Date` selection tool is not very convenient to use when selecting a wide time range.
3. Empty default graphs are caused by the absence of some commodities in certain markets.
4. Charts update relatively slowly, and different charts do not update simultaneously.

## 4. Potential Future Improvements and Additions

We plan to make the following attempts in the next week:
1. We will improve the selection and update issues of `Date` by including a hierarchy of dates in the date widget to encompass both yyyy and yyyy-mm formats.
2. For the issue of empty graphs caused by the non-existence of commodities in some markets, we will try to resolve by adding a hierarchy to the widgets.
3. We will explore ways to accelerate chart updates and resolve the issue of asynchronous updates.