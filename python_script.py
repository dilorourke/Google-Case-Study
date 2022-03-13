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

