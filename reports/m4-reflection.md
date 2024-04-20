# Milestone 4 Reflection

## 1. Improvements Since Milestone 3

Based on the peer reviews and the Milestone 3 reflection, we've implemented several key enhancements to the dashboard in Milestone 4:

1. Data loading and plotting speed: We have accelerated the speed of the charts update by implementing memoization for country data preprocessing, generating dynamic commodity charts, storing previous widget / chart state, etc.

2. Geo view: We have added the Geo view in our dashboard, where users could view a map of the country showing the latest commodity prices by region, facilitating regional price comparisons.

3. `Date` range selection: We have changed the `Date` range selection tool into a slider, for easier large date range selection.

4. Other fixes and touch-ups:
- Fixed the issue that commodities and markets widgets should handle when there is no chart.
- Made the country names in the dropdown menu sorted alphabetically.
- Added the notes on the dashboard and refined the docs (e.g. README) for better user understanding and usage.

5. Application transparency:
- Docstrings are included for every functions, with a description of the function and parameters, and the expected output.
- Clear comments are included for large code blocks to explain their functionality within the functions.

## 2. Limitations and Potential Future Improvements

Currently, every time we select a new country, we request the country's API in real time. A potential improvement in the future is to store data locally and automatically update the latest data from the web request API at regular intervals, to further reduce computational overhead and accelerate data loading speed. Moreover, more test cases can be added to ensure the accuracy of the functions used.

## 3. Useful Insights, Material, or Feedback for Our Dashboard Development

It's very important to consider the problem from the users' perspective and listen to the users' feedback. We received many useful feedback from peer reviews, such as annotating the meaning of glossaries, making widgets easier to use, adding a tutorial, etc. The feedback makes our dashboard more user friendly.