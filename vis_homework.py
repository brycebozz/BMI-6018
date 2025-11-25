# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''

#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''

print(covid_df.columns) #used to find what the columns are. Dates are set as columns. dates are start at column 11.
date_columns = covid_df.columns[11:]
utah_counties = covid_df[covid_df['Province_State'] == 'Utah'] #This will be made so only utah counties are found
 #I went through each of the columns until I found counties since counties wasnt labeled. This also gives me a list of all the counties
special_county = utah_counties[utah_counties['Admin2'] == 'Salt Lake'] #Chose Salt Lake since it's my home county
dates = pd.to_datetime(date_columns, format = '%m/%d/%y') #conveerts it to date time data
plt.figure(figsize = (12, 8))
plt.plot(dates, utah_counties[date_columns].T, color = 'lightgrey', linewidth = 1) #got the too many dimensions error looked it up and found out i could use .T which would flip it solving the issue.
plt.plot(dates, special_county[date_columns].T, color = 'blue', linewidth = 1, label = 'Salt Lake')
plt.title('Covid cases in Utah counties over time')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend()
plt.show()

#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''
def max_county(state):
    max_case = covid_df[covid_df['Province_State'] == state]
    final_max = max_case[date_columns].max()
    return final_max

florida_counties = covid_df[covid_df['Province_State'] == 'Florida']
florida_max = florida_counties[date_columns].max()
utah_max = utah_counties[date_columns].max()
plt.figure(figsize = (12, 8))
plt.plot(dates, florida_max, color = 'red', linewidth = 1, label = 'Florida')
plt.plot(dates, utah_max, color = 'Blue', linewidth = 1, label= 'Utah')
plt.title('Max cases in Florida and Utah counties over time')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend()
plt.show()

#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''
diffplot = []
previous_total = None
for x in special_county[date_columns]:
    daily_value = special_county[x].iloc[0]
    if previous_total is None:
        diffplot.append(0)
    else:
        diffplot.append(daily_value - previous_total)
    previous_total = daily_value
fig, ax1 = plt.subplots()
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Cases', color='blue')
ax1.plot(dates, special_county[date_columns].T, color = 'blue', linewidth = 1, label= 'Total Cases')
ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
color = 'tab:red'
ax2.set_ylabel('Daily Cases', color=color)
ax2.plot(dates, diffplot, color = 'red', linewidth = 1, label = 'Daily cases')
plt.title('Running total of cases and Daily Cases in Salt Lake County Utah')
fig.tight_layout()
plt.show()



#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''
counties = utah_counties['Admin2']
final_total = utah_counties[date_columns[-1]] #the final total would be the total for the final day
fig, ax = plt.subplots()
ax.set_xlabel('Utah')
ax.set_ylabel('Total Cases')
bottom = np.zeros(1)
for boolean, plot in zip(counties, final_total): #zip stiches two things together so it assigns each county name with each total number
    p = ax.bar(0, plot, label=boolean, bottom=bottom)
    bottom += plot #every time we do a plot it adds wbere we are in current


ax.set_title("Final total in each Utah county")
ax.legend(fontsize='xx-small')

plt.show()

#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''
