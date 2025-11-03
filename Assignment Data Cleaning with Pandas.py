# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:31:52 2025

@author: El-Wattaneya
"""

# -*- coding: utf-8 -*-

#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Importing Data
flights_data = pd.read_csv('C:\\Users\\El-Wattaneya\\Desktop\\Assignment\\flights.csv')
flights_data.head(10)

weather_data_pd = pd.read_csv('C:\\Users\\El-Wattaneya\\Desktop\\Assignment\\weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data

#Question 1 How many flights were there from JFK to SLC? Int
#q_1 
# Filtering the DataFrame for rows where 'origin' is 'JFK' AND 'dest' is 'SLC'
# Then, using len() to count the number of rows in the filtered result
q_1 = len(flights_data[(flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')])
print("Q1 - Number of flights from JFK to SLC:", q_1)


#Question 2 How many airlines fly to SLC? Should be int
#q_2 
# Using .loc to select rows where 'dest' is 'SLC' and then grabbing just the 'carrier' column
# .nunique() counts the number of unique values in that column
q_2 = flights_data.loc[flights_data['dest'] == 'SLC', 'carrier'].nunique()
print("Q2 - Number of airlines flying to SLC:", q_2)


#Question 3 What is the average arrival delay for flights to RDU? float
#q_3
# Filtering for flights where 'dest' is 'RDU', selecting the 'arr_delay' column
# .mean() calculates the average of all values in that selected column
q_3 = flights_data.loc[flights_data['dest'] == 'RDU', 'arr_delay'].mean()
print("Q3 - Average arrival delay for flights to RDU:", q_3)


#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
#q_4
# First, create a new DataFrame containing only flights destined for 'SEA' 
sea_flights = flights_data[flights_data['dest'] == 'SEA']
# From 'sea_flights', filter for rows where 'origin' is in the list ['LGA', 'JFK'] and count them
# Divide this count by the total number of flights to SEA (len(sea_flights))
q_4 = len(sea_flights[sea_flights['origin'].isin(['LGA', 'JFK'])]) / len(sea_flights)
print("Q4 - Proportion of flights to SEA from LGA and JFK:", q_4)


#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
#q_5 
# Create a new 'date' column by converting date parts to string and joining with '/'
# axis=1 applies the join row-by-row
flights_data['date'] = flights_data[['year', 'month', 'day']].astype(str).agg('/'.join, axis=1)
# Group the DataFrame by the new 'date' column and calculate the mean 'dep_delay' for each date
avg_dep_delay = flights_data.groupby('date')['dep_delay'].mean()
# .idxmax() finds the index (the date) with the highest mean delay
# .max() finds the highest mean delay value itself
q_5 = avg_dep_delay.idxmax(), avg_dep_delay.max()
print("Q5 - Date with largest avg departure delay:", q_5)


#Question 6 Which date has the largest average arrival delay? pd slice with date and float
#q_6 
# reusing the 'date' column from Q5 that is already created
# Group by 'date' and find the mean 'arr_delay' for each date
avg_arr_delay = flights_data.groupby('date')['arr_delay'].mean()
# Find the date (.idxmax()) and value (.max()) for the largest average arrival delay
q_6 = avg_arr_delay.idxmax(), avg_arr_delay.max()
print("Q6 - Date with largest avg arrival delay:", q_6)


#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
#q_7
# Create a 'speed' column. 'air_time' is divided by 60 to convert minutes to hours
flights_data['speed'] = flights_data['distance'] / (flights_data['air_time'] / 60)
# Start filtering: first, select flights with 'origin' in ['LGA', 'JFK']
fastest = flights_data.loc[flights_data['origin'].isin(['LGA', 'JFK'])]
# Next, filter the result for flights where 'year' is 2013
fastest = fastest.loc[fastest['year'] == 2013]
# Find the index of the row with the maximum 'speed' using .idxmax()
# Use .loc[] to select the entire row (as a Series) for that fastest flight
fastest = fastest.loc[fastest['speed'].idxmax()]
# Select just the 'tailnum' and 'speed' from the fastest flight's row
q_7 = fastest[['tailnum', 'speed']]
print("Q7 - Fastest flight departing LGA or JFK:", q_7)


#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
#q_8 
# .fillna(0) replaces all NaN (Not a Number) values in the entire DataFrame with 0
q_8 = weather_data_pd.fillna(0)
print("Q8 - Weather data with NaNs replaced by 0:")
print(q_8.head())


#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
#q_9 
# Create a boolean Series (True/False) where the 'month' is 2
feb_idx = weather_data_pd['month'] == 2
# Summing a boolean Series counts the 'True' values (since True=1 and False=0)
q_9 = feb_idx.sum()
print("Q9 - Observations made in February:", q_9)


#Question 10 What was the mean for humidity in February? Float
#q_10
# Reusing the 'feb_idx' boolean mask to filter the DataFrame
# Select the 'humid' column from the filtered rows and calculate its .mean()
q_10 = weather_data_pd.loc[feb_idx, 'humid'].mean()
print("Q10 - Mean humidity in February:", q_10)


#Question 11 What was the std for humidity in February? Float
#q_11
# Reuse 'feb_idx' again to filter for February rows
# Select the 'humid' column and calculate its standard deviation (.std())
q_11 = weather_data_pd.loc[feb_idx, 'humid'].std()
print("Q11 - Standard deviation of humidity in February:", q_11)


