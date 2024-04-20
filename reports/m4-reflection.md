# Milestone 4 Reflection

## 1. Improvements Since Milestone 3

Based on the peer reviews and the Milestone 3 reflection, we've implemented several key enhancements to the dashboard in Milestone 4:

1. Data loading and plotting speed: 
- The speed of the charts update have been accelerated by implementing memoization for country data preprocessing, generating dynamic commodity charts, storing previous widget / chart state, etc.
- Loading message and widget freeze are implemented to notify user for clear understanding and prevent unexpected user action during the process.

2. Geo view: 
- We have added the Geo view in our dashboard, where users could view a map of the country showing the latest commodity prices by region, facilitating regional price comparisons.

3. `Date` range selection: 
- We have changed the `Date` range selection tool into a slider, for easier large date range selection.

4. [Performance Improvement](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/105)
- The country data is cached once pulled through API, which is later used when the previous visited country is visited again. This saves the API call and the processing time for fetching the data via the API and increase the efficiency.
- The computation time is further reduced during the data transformation by removing redundant filtering or slow of the data, e.g. replacing `numpy.apply` with similar functions.
- As the data is fetched in real-time and cached instead of long-term storage, binary format might not be applicable for the improvement as [commented by Joel](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/105) 

5. [Other fixes and touch-ups](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/issues/106)
- User warning was implemented when no commodities or markets were selected and exception handling was developed to remove the charts instead of plotting charts with errors.
- The country names in the dropdown menu were sorted alphabetically as per peer comment.
- Glossary of domain-specifc terms were added in the footer on the dashboard and documents were (e.g. README) revised with short demostration GIF and full demostration video for better user understanding and experience.

6. Application transparency:
- Docstrings are included for every functions, with a description of the function and parameters, and the expected output.
- Clear comments are included for large code blocks to explain their functionality within the functions.

## 2. Limitations and Potential Future Improvements

- Currently, we would request the country's API to fetch real-time data every time the user selects a new country the first time. We are aware that there is still room for improvement to reduce computational overhead for higher efficiency, for example, regularly fetching data using a cron job at regular intervals and storing the data locally instead of fetching  data in real-time. However, due to the time constraint of the project, it would not be implemented in Milestone 4.
- Due to the variation of data among countries, different data quality issues were found which requires significant amount of time for data wrangling. 10 countries with best data quality were selected as the pilot countries in our prototype to demostrate the functionality of our dashboard without error casued by data quality issue.
- Moreover, more test cases can be added to ensure the accuracy of the functions used.

## 3. Useful Insights, Material, or Feedback for Our Dashboard Development

It's very important to consider the problem from the users' perspective and listen to the users' feedback. We received many useful feedback from peer reviews, such as annotating the meaning of glossaries, making widgets easier to use, adding a tutorial, etc. The feedback makes our dashboard more user friendly.