# sqlalchemy-challenge

In preparation for a long holiday vacation in Honolulu, Hawaii, some climate analysis needs to be done on the area.

## Exploratory Climate Analysis

In Jupyter Notebook (climate.ipynb), preliminary queries were created to explore the data set. The Flask app (app_hi.py) uses these queries to return the API data. The query results for preciptaiotn levels by date for the dataset are plotted in a bar chart. A histogram show the temperature frequency for the last year of data.

## Using the API (app_hi.py)

The avaibale routes are:
* precipitation
* stations
* tobs (temperature)
* start date (temperature summary)
* start and end date (temperature summary)

The range of data is from 2010-01-01 to 2017-08-23.  

"Precipitaion" gives a list of the date and the percipition measuerment for that day.

"Stations" gives a list of all the measurement staions.

"TOBS" (temperature observation) gives a list of the date and temperature readings for the most active station (USC00519281, as identfied in the climate ananlysis) in the last year of data.

"Start date" will search from a given start date to the last entry in the data set and return the min, max, and avg temperatures in that time period. The seach criteria format is: year-month-day (e.g. 2012-03-09).

"Start and end date" will search from the start date to the end date and return the min, max, and avg temperatures in that time period. The seach criteria format is: year-month-day/year-month-day (e.g. 2012-03-09/2015-11-20).
