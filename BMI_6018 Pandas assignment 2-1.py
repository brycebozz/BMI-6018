import pandas as pd
import numpy as np
#Question 1
#Input
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(p-q) #this is scratch to see how the two pandas subtracted from each other.
Euclidean_distance= (((p-q) ** 2).sum()) ** 0.5
print(Euclidean_distance)
#Question 2
#change the order of columns of a dataframe. Interchange columns 'a' and 'c'
#Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df = df[['c', 'b', 'a','d','e']]
print(df) #confirming if columns a and c switched.
#Question 3
#Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.
#Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
def interchangecol(frame, col1, col2):
    column_list = list(frame.columns)
    new_column = []
    for col in column_list:
        if col == col1:
            new_column.append(col2)
        elif col == col2:
            new_column.append(col1)
        else:
            new_column.append(col)
    return frame[new_column]
print(interchangecol(df, 'e', 'b')) #confirming it works. Found that it works



#Question 4
#Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
#Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
print(df) #printing to see before and after
#>          random
#> 0  3.474280e-03
#> 1  3.951517e-05
#> 2  7.469702e-02
#> 3  5.541282e-28
#Desired Output
#>    random
#> 0  0.0035
#> 1  0.0000
#> 2  0.0747
#> 3  0.0000
pd.options.display.float_format = '{:,.4f}'.format
print(df) #printing to see if it worked
#Question 5
#Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
#Input
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
#df
print(df)
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34
#Desired Output
#df
#    p   q   r   s nearest_row   dist
# a  57  77  13  62           i  116.0
# b  68   5  92  24           a  114.0
# c  74  40  18  37           i   91.0
# d  80  17  39  60           i   89.0
# e  93  48  85  33           i   92.0
# f  69  55   8  11           g  100.0
# g  39  23  88  53           f  100.0
# h  63  28  25  61           i   88.0
# i  18   4  73   7           a  116.0
# j  79  12  45  34           a   81.0


#Question 6
#Input
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]}

df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
print(df.corr()) #I interpretted the question as make a data frame with whats provided and use .corr() to make a correlation matrix. 