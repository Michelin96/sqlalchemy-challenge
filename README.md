# sqlalchemy-challenge

In preparation for a long holiday vacation in Honolulu, Hawaii, some climate analysis needs to be done on the area.

## Exploratory Climate Analysis Process

Using SQLAlchemy's automatic base mapping, two database classes were found in the Resources/hawaii.sqlite file: measurement and station. The __dict__ oject was applied to a query of the first row in each class to determine the keys and values that will create table columns and data. Next, the inspector was run on the columns to check their data types.

A preliminary query was run to get the date of the last data point of precipitation data. Selecting all of the data from the measurement table ordered by the date in decending order gave the result 2017-08-23. This date was used to calculate the last 12 months of precipitaton data.
