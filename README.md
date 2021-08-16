# **Surfs_Up**

## Overview of the analysis: 

The goal of the Surfs_Up analysis is to provide an investor with valuable insight into the weather patterns of a specific location on Oahu, Hawaii to determine the sustainability of a business year-round. Using programming skills we offered information about trends and patterns needed to make a well informed decision. 

Software: SQLite, SQLAlchemy, Flask, Python and Jupyter Notebook.  

Data Source: [Hawaii.sqlite](https://github.com/chocoplace/surfs_up/blob/main/hawaii.sqlite), [Climate_analysis](https://github.com/chocoplace/surfs_up/blob/main/climate_analysis.ipynb), [App.py](https://github.com/chocoplace/surfs_up/blob/main/app.py). 

### Results:

To have a better idea of the trends on temperatures, we developed the base code for June and December since these are the most pivotal months. The code can be found here: [SurfsUp_challenge](https://github.com/chocoplace/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

From the results of June and December we can conclude that the weather in Oahu is persistent, it shows minimal but significant differences on the following:
 - Mean: By 3.902589 degrees between the average temperature of June and December. 
 - Min: By 8 degrees between the minimum (smallest) temperature of June and December. In December the min temperature is 56 degrees, great for tourists from cold weather. 
 - Max: By 2 degrees between the max (largest) temperature of June and December. In December the max temperature is 83 degrees, great for tourists from cold weather
 - Standard deviation (Std) of December is 3.745920 slightly different from June. 

Plase check image for referece: 

June Temperature 

![June Temperature](https://github.com/chocoplace/surfs_up/blob/main/Resources/June%20Temps.png)

December Temperature 

![December Temperature](https://github.com/chocoplace/surfs_up/blob/main/Resources/December%20Temps.png)

Additional comments: 

 - The results conclude the location of Oahu has a privileged weather for the business success. The weather trend has not significantly changed and can be a great destination for tourists from cold weather. 
 - The initial request had a relation between weather and sales of ice cream, the client will need to create a marketing strategy to utilize the information provided in this analysis. The sales will be based on the tourist profile and demographics since the weather variables are in favor.
 - The code can be refactor to be used as the baseline to determine the temperature of the remaining months of the year if needed by the client. To apply the code change the month and the month number in the following example “december_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==12).all()”.
 - To help provide a better insight for the client and have a better sense of the weather in the area. The analysis offers two additional queries related to the precipitation since raining can be crucial for ice cream sales. The additional code can be found here: [SurfsUp_challenge](https://github.com/chocoplace/surfs_up/blob/main/SurfsUp_Challenge.ipynb)
 - Here are the results for the additional queries: 

June Precipitation 

![June Precip](https://github.com/chocoplace/surfs_up/blob/main/Resources/June%20Precip.png)

December Precipitation

![December Precip](https://github.com/chocoplace/surfs_up/blob/main/Resources/December%20Precip.png)

End 
