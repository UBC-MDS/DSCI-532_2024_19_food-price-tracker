# Milestone 4 Reflection

## 1. Improvements Since Milestone 3

Based on the peer reviews and the Milestone 3 reflection, we've implemented several key enhancements to the dashboard in Milestone 4:

1. Data loading and plotting speed: We have accelerated the speed of the charts update by implementing memoization for country data preprocessing, generating dynamic commodity charts, storing previous widget / chart state, etc.

2. Geo view: We have added the Geo view in our dashboard, where users could view a map of the country showing the latest commodity prices by region, facilitating regional price comparisons.

3. `Date` range selection: We have changed the `Date` range selection tool into a slider, for easier large date range selection.

4. [Performance Improvement](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/105)
- The country data is cached once pulled through API, which is later used when the previous visited country is visited again. This saves the API call and the processing time for fetching the data via the API and increase the efficiency.
- The computation time is further reduced during the data transformation by removing redundant filtering or slow of the data, e.g. replacing `numpy.apply` with similar functions.
- As the data is fetched in real-time and cached instead of long-term storage, binary format might not be applicable for the improvement as [commented by Joel](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/105) 

5. [Other fixes and touch-ups](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/106)
- Fixed the issue that commodities and markets widgets should handle when there is no chart.
- Made the country names in the dropdown menu sorted alphabetically.
- Added the notes on the dashboard and refined the docs (e.g. README) for better user understanding and usage.

6. Application transparency:
- Docstrings are included for every functions, with a description of the function and parameters, and the expected output.
- Clear comments are included for large code blocks to explain their functionality within the functions.

## 2. Limitations and Potential Future Improvements

Currently, we would request the country's API to fetch real-time data every time the user selects a new country the first time. We are aware that there is still room for improvement to reduce computational overhead for higher efficiency, for example, regularly fetching data using a cron job at regular intervals and storing the data locally instead of fetching  data in real-time. However, due to the time constraint of the project, it would not be implemented in Milestone 4.

Moreover, more test cases can be added to ensure the accuracy of the functions used.

## 3. Useful Insights, Material, or Feedback for Our Dashboard Development

It's very important to consider the problem from the users' perspective and listen to the users' feedback. We received many useful feedback from peer reviews, such as annotating the meaning of glossaries, making widgets easier to use, adding a tutorial, etc. The feedback makes our dashboard more user friendly.