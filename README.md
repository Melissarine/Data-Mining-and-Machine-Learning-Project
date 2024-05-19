# Data-Mining-and-Machine-Learning-Project
Determining the Air Quality for Beijing

Introduction:

My project's focus was on predicting the Air Quality Index (AQI) for a city in Beijing (Shunyi) using the AQI of four neighboring cities AQI (Changping, Huairou, Nongzhanguan, Tiantan). This project is a great example of how data science can be applied to environmental aspects. If this model of predicting the AQI of a city with the neighboring city was good in estimating, then it could be applied to real life situations where we can predict the Air Quality Index for a city where the air quality monitoring station is shut down or don’t work. 

City 1: Huairou, City 2: Nongzhanguan, City 3: Tiantan, City 4: Changping, City 5: Shunyi 


Data Collection and Preprocessing:

The air quality data set is from Kaggle. Using the data from 5 cities in Beijing (Changping, Huairou, Nongzhanguan, Tiantan, Shunyi) which has the record of the air quality from 2013 to 2017. Initially it had 18 columns year, month, day, hour, PM2.5, PM10, SO2, NO2, CO, O3, Temperature, Pressure, Dew Point Temp, RAIN, wind direction, and Wind speed (per minute). AQI for the five cities in separate excel sheets, so I combined them into one dataset by appending to the row side. 

The first step in the data cleaning process was to have a column of the air quality index. The calculate the air quality index by using the standard way used in the airnow.govenement website. Source (14th page of this document from the Airnow government website). 

I altered the units of the dataset using the table provided in the government. Then I used the AQI formula and calculated the AQI index for the entire dataset.  

Next, I created a Date and Time column for the data using the year, month, day, and hour combining them into one Date and Time column.  

To handle the missing values in the dataset I used the Moving average to fill in the NA values with the average of the closer values. 

Now the data is ready for the implementation of the Timeseries model.  

 

A table of numbers and a number of areas

Description automatically generated with medium confidence 
