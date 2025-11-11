import pandas as pd

#imported data set using link below
cols =['sepal length','sepal width','petal length','petal width','class']
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names=cols)
print(df)
melt_df = pd.melt(df, id_vars=['class', 'sepal length', 'petal length'], value_vars=['sepal width', 'petal width']) #what this does is it gives the class and lengths and makes it easier to see the width of each and seperates out the widths.
print(melt_df)
#heres the groupby code and the aggregate code
group_df = df.groupby('class').agg({'sepal length': ['min', 'max', 'mean'], 'sepal width': ['min', 'max', 'mean'], 'petal length': ['min', 'max', 'mean']})
print(group_df)
#heres the pivot code
pivot_df = df.pivot_table(index='class',  values=['sepal length','sepal width','petal length', 'petal width'], aggfunc='mean') #have to use pivot_table because can't have an index with multiple entries so i did a pivot with an aggregate that found the mean
print(pivot_df)
#heres the iteration code
for row_index,row in df.iterrows():
   print(row_index,row)