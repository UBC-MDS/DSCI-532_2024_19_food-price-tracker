# Milestone 4 Reflection

## 1. Improvements Since Milestone 3

Based on the peer reviews and the Milestone 3 reflection, we've implemented several key enhancements to the dashboard in Milestone 4:

1. Geo view: 
- Added geo-view plot, where prices are placed spatially by region to facilitate single-time-point regional price comparisons.

2. `Date` range selection: 
- Changed the `Date` range selection tool into a slider with custom tooltip to improve date range selection.

3. [Performance Improvement](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/105)
- Country data is cached once fetched and preprocessed, reducing time to change between countries.
- Redundant filtering or slow operations replaced by vectorized or memoized processes (e.g., replacing `numpy.apply`).
- Dynamic charting of commodities was implemented by storing and retrieving the current charts and if applicable, reusing existing charts. This significantly reduced processing time in the basic view.
- As the data is fetched in real-time and cached instead of long-term storage, binary format might not be applicable for the improvement as [commented by Joel](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/105) 

5. [Other fixes and touch-ups](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/106)
- Implemented warnings and disable charts when no commodities or markets were selected to improve user experience. 
- Widgets are disabled and loading message shown when fetching data, reducing erroneous inputs or confusion. 
- The country names in the dropdown menu were sorted alphabetically as per peer comment.
- A glossary and video tutorial were added to the dashboard, and documents (e.g. README) were updated with new GIFs and video tutorial links. 

6. Application transparency:
- Docstrings are included for every function.
- Clear comments are included for large code blocks to explain their functionality within the functions.

## 2. Limitations and Potential Future Improvements

- Country data is fetched in real-time and is still slow even with caching and memoization. It is recommended that a server-side cron-job is implemented to fetch data and store locally for efficient retrieval during dashboard use. Not implemented due to time constraints and technical limitations of render.com. 
- Data quality suffered from country to country, and more nuanced filtering is required. 9 countries with best data quality were selected as the pilot countries in our prototype. 
- Data processing could be more centralized and generalized to improve charting time, but this will be challenging to implement given the dynamic nature of our data.
- The geo-chart is still somewhat limited, and interactivity was constrained by Altair and time. We would seek to improve its performance and visual aesthetic in subsequent revisions. 
- Moreover, more test cases can be added to ensure the accuracy of the functions used.

## 3. Useful Insights, Material, or Feedback for Our Dashboard Development

It's very important to consider the problem from the users' perspective and listen to the users' feedback. Overall, we find our dashboard to describe data well and is positioned to generalize to many countries.
