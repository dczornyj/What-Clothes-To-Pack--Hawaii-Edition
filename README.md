# What Clothes Should I pack?- Hawaii

It's been a strenuous last couple of months at work and you decide to preliminarily start planning a future vacation to Hawaii. Upon the first week of thinking about the trip, you check your wardrobe to make sure you have a raincoat as you have become aware that it rains quite often in Hawaii. This thought then spurs you to investigate further into how the temperature and precipitation levels varied within the past year in order to plan for what to expect and what clothes to pack depending on what part of the year you take your vacation there. Use the sql lite database that is found within this repository to analyze the climate conditions in Hawaii. 

## Initial Exploration

-Find the most recent date in the data set.

-Print the summary statistics for the precipitation data.

-Design a query to calculate the total number of stations in the dataset.

-Design a query to find the most active stations (i.e. which stations have the most rows?).

-List the stations and observation counts in descending order.

-Which station id has the highest number of observations?

-Using the most active station id, calculate the lowest, highest, and average temperature.

## Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.


  * List all dates and the amount of precipitation that was recorded.

  * Return a JSON list of stations from the dataset.

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  # Screenshots
  
![sql alchemy imports](https://user-images.githubusercontent.com/101612220/202082472-592a0007-4e87-4bae-8751-0d72ca385aea.png)


![sqlalchemy mostrecent](https://user-images.githubusercontent.com/101612220/202082537-dd91b556-3f93-4dac-8203-ec7a96d5f0b3.png)

-Precipitation (inches vs. Date)
![sqlalchemy precipbar](https://user-images.githubusercontent.com/101612220/202082564-a645516a-cdf3-428f-8246-7da6c3e8cf31.png)

-Hawaii Climate Summary Statistics
![sqlalchemy sumstats](https://user-images.githubusercontent.com/101612220/202082583-43cbd0f5-5c04-4a5c-9c7a-dbf24f635a37.png)

-List of Climate Stations
![sqlalchemy list stations](https://user-images.githubusercontent.com/101612220/202082642-0279429c-e210-4dd6-9ffc-df14ae3aaaf8.png)

-Binning for Histogram
![sqlalchemy binning4his](https://user-images.githubusercontent.com/101612220/202082677-6b00dffa-0ec5-4598-9837-01725757f147.png)

-Number of Days vs. Temperature Histogram
![sqlalchemy challenge histo](https://user-images.githubusercontent.com/101612220/202082007-c9f6f8b9-6b1e-4128-ae54-ffdc44a2a32a.png)




© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
