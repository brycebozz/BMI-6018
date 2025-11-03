import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Importing Data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()

#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data
#Question 1 How many flights were there from JFK to SLC? Int
flights_data_JFK2SLC = len(flights_data[((flights_data['origin'] == "JFK") & (flights_data['dest'] == "SLC"))])
print(type(flights_data_JFK2SLC)) #confirming if value is integer
print(f"There were {flights_data_JFK2SLC} flights from JFK to SLC") #printing Q1 Answer

#Question 2 How many airlines fly to SLC? Should be int
SLC_flights = flights_data[flights_data['dest'] == 'SLC']
number_of_airports2SLC = len(SLC_flights["origin"].unique())
print(number_of_airports2SLC) #printing question 2 answer
print(f'confirming type of answer for Q2 {type(number_of_airports2SLC)}')
#Question 3 What is the average arrival delay for flights to RDU? float
RDU_delay = flights_data[flights_data['dest'] == 'RDU']
RDU_delay_mean = int(RDU_delay['arr_delay'].mean())
print(RDU_delay_mean) #printing answer to question 3
print(f'q3 type is {type(RDU_delay_mean)}') #confirming if answer is float
#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
SEA_flights = flights_data[flights_data['dest'] == 'SEA']
SEA_flights_total = len(flights_data[flights_data['dest'] == 'SEA'])
SEA_flights_prop = (len(flights_data[((flights_data['origin'] == "JFK") & (flights_data['dest'] == "SEA"))]) + len(flights_data[((flights_data['origin'] == "LGA") & (flights_data['dest'] == "SEA"))])) / SEA_flights_total
print(SEA_flights_prop) #Printing answer to question 4
print(f'q4 type is {type(SEA_flights_prop)}') #confirming if answer is float
#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data['date'] = flights_data['year'].astype(str) + '-' + flights_data['month'].astype(str) + '-' + flights_data['day'].astype(str)
average_depart_delay = flights_data.groupby(['date'])['dep_delay'].mean().reset_index() #groups data by data and finds the mean of each date and resetindex turns what i did into a data frame
max_average_depart_delay = average_depart_delay.loc[average_depart_delay['dep_delay'].idxmax()]
print(f'The date with the largest average departure delay and the depature delay as well is {max_average_depart_delay}')# This is answer to question 5. print gives the date and arrival delay time of the largest average depart delay

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
average_arrival_delay = flights_data.groupby(['date'])['arr_delay'].mean().reset_index()
max_average_arrival_delay = average_arrival_delay.loc[average_arrival_delay['arr_delay'].idxmax()]
print(f'The date with the largest average arrival delay and the arrival delay as well is {max_average_arrival_delay}') # This is the answer to question 6. print gives the date and arrival delay time of the largest average arrival delay
#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
#flight_dist = flights_data.loc[((flights_data['origin'] != 'EWR') & (flights_data['distance']))]
#flight_airtime = flights_data.loc[((flights_data['origin'] != 'EWR') & (flights_data['air_time']))]
flights_data['speed'] = flights_data['distance'] / flights_data['air_time']
flights_LGA_JFK = flights_data.loc[(flights_data['origin'] != 'EWR')]
print(f'The fastest flight from JFK or LGA and its speed is {flights_LGA_JFK.loc[flights_LGA_JFK['speed'].idxmax(), ['tailnum', 'speed']]}') # This is the answer to question 7 .idxmax()finds the max of the speed and the ['tailnum', 'speed'] print the speed and tailnumber.
#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
print(weather_data_pd) #shows NANs
weather_data_pd = weather_data_pd.fillna(0) #had weather_data_pd = what i wrote so the data frame would be updated. fillna replaces all NaNs with 0
print(weather_data_pd) #shows NaNs are filled
weather_data_np = weather_data_pd.to_numpy() #updates numpy to have nan values to be 0 to have it align with what we did for the pandas.
#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
Feb_observations = (weather_data_np[:, 3] == 2) #this will be used for questions 9-11. [:, 3] means all rows and the 3rd column which is month.
No_Feb_observations = int(Feb_observations.sum()) #converting to integer to
print(type(No_Feb_observations)) #confirming if integer
print(f'There are {No_Feb_observations} Feburary observations') #printed answer to question 9
#Question 10 What was the mean for humidity in February? Float
humid_mean_Feb = float(weather_data_np[Feb_observations, 8].mean())
print(f'The mean for humiditiy infeburary is {humid_mean_Feb}') #Heres the printed answer
print(type(humid_mean_Feb)) #confirming the type for Q10
#Question 11 What was the std for humidity in February? Float
humid_std_Feb = float(weather_data_np[Feb_observations, 8].std())
print(f'The std for humidity in Feburary is {humid_std_Feb}') #printed answer for question 11
print(type(humid_std_Feb)) #confirming type for question11