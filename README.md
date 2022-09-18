# covid19analyze
https://covid19analyze.herokuapp.com/

The project featured scrapping data across various websites, refining and cleaning the gathered data, analyzing the data, adding features to support the analysis and lastly adding a frontend to it and deploying the dashboard.
1. Data Scrapping: It was done using BeautifulSoup4 library in python which was used to parse tables to gather data across various domains from different websites eg. https://www.worldometers.info/coronavirus/, https://data.worldbank.org/indicator, etc. and store it in form of a CSV.
2. Data cleaning: It was done using Pandas, a popular library in Python for manipulating and analyzing data. Data was bifurcated then combined, sorted as per need and filled in for incomplete data.
3. Data analysis: The dataset created in the previous step was further analyzed by plotting different types of graphs for various columns/rows of the dataset and finding out correlations then eliminating the outliers and selecting a range. The final dataset was generated after this which would be used to provide analysis.
4. Providing insights and plotting graphs to support them: Plotly, Matplotlib and Seaborn libraries were used to plot graphs eg: scatter plots, regression plot and time series graphs using the final dataset and provide meaningful analysis for the same.
5. Adding a frontend and deploying the dashboard: html, css, flask were used for this purpose and the dashboard app was deployed on heroku.
