# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Importing Packages
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import datetime

#Defining the data folder and creating a list of files in it using data_files
data_dir = r'C:\Users\Dillon\Documents\Coding Learning\Google Data Analytics Course\Google Data Analytics Capstone Complete a Case Study\Data\Fitabase Data 3.12.16-4.11.16'
data_files = os.listdir(data_dir)

#creating a dataframe from each file in the os dir
dailyActivity = pd.read_csv(data_dir + '\dailyActivity_merged.csv')

heartrate_seconds = pd.read_csv(data_dir + '\heartrate_seconds_merged.csv')
hourlyCalories = pd.read_csv(data_dir + '\hourlyCalories_merged.csv')
hourlyIntensities = pd.read_csv(data_dir + '\hourlyIntensities_merged.csv')
hourlySteps = pd.read_csv(data_dir + '\hourlySteps_merged.csv')
minuteCaloriesNarrow = pd.read_csv(data_dir + '\minuteCaloriesNarrow_merged.csv')
minuteIntensitiesNarrow = pd.read_csv(data_dir + '\minuteIntensitiesNarrow_merged.csv')
minuteMETsNarrow = pd.read_csv(data_dir + '\minuteMETsNarrow_merged.csv')
minuteSleep = pd.read_csv(data_dir + '\minuteSleep_merged.csv')
minuteStepsNarrow = pd.read_csv(data_dir + '\minuteStepsNarrow_merged.csv')
weightLogInfo = pd.read_csv(data_dir + '\weightLogInfo_merged.csv')

#print(dailyActivity.nunique(axis = 0))
#print(dailyActivity.Id.value_counts())

""" DATA CLEANING """
# Changing Column names
dailyActivity = dailyActivity.rename(columns = {"ActivityDate":"Date", })
#Changing data types
dailyActivity = dailyActivity.astype({'Id':str})
dailyActivity.Date = pd.to_datetime(dailyActivity.Date)

#Check how many unique IDs and Dates
print('Distinct IDs in dailyActivity: ', len(pd.unique(dailyActivity['Id'])))
print('Distinct Dates in dailyActivity: ', len(pd.unique(dailyActivity["Date"])))

#This will calculate the number of unique values in each column grouped by Id. i.e. count distinct dates, group by Id
daily_actchk = dailyActivity.groupby(['Id']).agg(['nunique'])

#Check for duplciate rows. If theres a duplicate row its value in the list will be True. If there's a dupe, our print will print True
print('Duplicate rows in data?: ', True in list(dailyActivity.duplicated()))


#pulling column of dates from df above
dates = list(daily_actchk.iloc[:, 0])
#pulling IDs from dailAct
IDs = list(pd.unique(dailyActivity['Id']))

#creating plot
fig = plt.figure()
ax = fig.add_axes([0,0,1,2])
x = IDs
y = list(daily_actchk.iloc[:, 0])
plt.barh(IDs, y, align='edge', color = 'green')
plt.xlabel("Days of Data")
plt.ylabel("User ID")
plt.title("Number of days that each user logged data")
plt.show()

#prints the avg number of logged days
print('Average number of days of data: ', int(np.around(np.average(dates), 0)))

"""
#Pulling days where no exercise was done
no_data_days = dailyActivity[dailyActivity.SedentaryMinutes == 1440 ]
no_data_days = no_data_days[no_data_days.TotalSteps == 0 ]
#Pulling days where there was exercise
data_days = dailyActivity
data_days = data_days[~data_days.isin(no_data_days)].dropna()
#dropping unnecessary columns
#data_days = data_days.filter(['Id', 'Date'])
#no_data_days = no_data_days.filter(['Id', 'Date'])
#counting number of no exercise days per person
#no_data_days = no_data_days.groupby(['Id']).agg(['count'])
#data_days = data_days.groupby(['Id']).agg(['count'])
"""
