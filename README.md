# sqlalchemy-challenge

In preparation for a long holiday vacation in Honolulu, Hawaii, some climate analysis needs to be done on the area.

## Exploratory Climate Analysis Process

Using SQLAlchemy's automatic base mapping, two database classes were found in the Resources/hawaii.sqlite file: measurement and station. The __dict__ oject was applied to a query of the first row in each class to determine the keys and values that will create table columns and data. Next, the inspector was run on the columns to check their data types.

A preliminary query was run to get the date of the last data point of precipitation data. Selecting all of the data from the measurement table ordered by the date in decending order gave the result 2017-08-23. This date was used to calculate the last 12 months of precipitaton data.

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
