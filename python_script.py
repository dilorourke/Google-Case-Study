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

#Defining the data folder and creating a list of files in it using data_files
data_dir = r'C:\Users\Dillon\Documents\Coding Learning\Google Data Analytics Course\Google Data Analytics Capstone Complete a Case Study\Data\Fitabase Data 3.12.16-4.11.16'
data_files = os.listdir(data_dir)

#creating a dataframe from each file in the os dir
dailyActivity = pd.read_csv(data_dir + '\dailyActivity_merged.csv')
#heartrate_seconds = pd.read_csv(data_dir + '\heartrate_seconds_merged.csv')
#hourlyCalories = pd.read_csv(data_dir + '\hourlyCalories_merged.csv')
#hourlyIntensities = pd.read_csv(data_dir + '\hourlyIntensities_merged.csv')
#hourlySteps = pd.read_csv(data_dir + '\hourlySteps_merged.csv')
#minuteCaloriesNarrow = pd.read_csv(data_dir + '\minuteCaloriesNarrow_merged.csv')
#minuteIntensitiesNarrow = pd.read_csv(data_dir + '\minuteIntensitiesNarrow_merged.csv')
#minuteMETsNarrow = pd.read_csv(data_dir + '\minuteMETsNarrow_merged.csv')
#minuteSleep = pd.read_csv(data_dir + '\minuteSleep_merged.csv')
#minuteStepsNarrow = pd.read_csv(data_dir + '\minuteStepsNarrow_merged.csv')
#weightLogInfo = pd.read_csv(data_dir + '\weightLogInfo_merged.csv')

#print(dailyActivity.nunique(axis = 0))
#print(dailyActivity.Id.value_counts())

print('daily Act IDs: ', len(pd.unique(dailyActivity['Id'])))
#print('heartrate sec IDs: ', len(pd.unique(heartrate_seconds['Id'])))
print('daily Act Dates: ', len(pd.unique(dailyActivity['ActivityDate'])))

daily_actchk = dailyActivity.groupby(['Id']).agg(['nunique'])

dates = list(daily_actchk.iloc[:, 0])
IDs = list(pd.unique(dailyActivity['Id']))

IDss = list()
for i in IDs:
    IDss.append(str(i)) 
fig = plt.figure()
ax = fig.add_axes([0,0,1,2])
x = IDss
y = dates
plt.barh(IDss, y, align='edge', color = 'green')
plt.xlabel("Days of Data")
plt.ylabel("User ID")
plt.title("Number of days that each user logged data")
plt.show()

print('Average number of days of data: ', int(np.around(np.average(dates), 0)))