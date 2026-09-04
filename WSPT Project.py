#1: Importing csv file created in excel. Current translated type is class 'pandas.DataFrame'
import pandas as pd
import numpy as np
df = pd.read_csv('WSPT.csv')
print(df)
print(type(df))

#2: Using Panda Data Frames to calculate weighted completion time
# Adding a new column for calculated data
new_column_weighted_completion_time = np.zeros(len(df),dtype=object)
df["Weighted Completion Time"] = new_column_weighted_completion_time
print(df)

# Calculate weighted completion time and add it to the new column
for i in range(len(df)):
    df.iloc[i,3] = round(df.iloc[i,1] / df.iloc[i,2], 1)
print(df)

#3:Using Numpy arrays to calculate weighted completion time
df = pd.read_csv('WSPT.csv')

# Stacking the Pandas Data Frame headings on top of the Pandas Data Frame values
a = df.columns.to_numpy()
b = df.to_numpy()
numpy_array = np.vstack((a,b))

# Adding a new column for calculated data input
new_column_weighted_completion_time = np.zeros(len(numpy_array),dtype=object)
new_column_weighted_completion_time[0] = "Weighted Completion Time"
numpy_array = np.column_stack((numpy_array,new_column_weighted_completion_time))

#Calculate weighted completion time and add it to the new column
for i in range(1,len(numpy_array)):
    numpy_array[i,3] = round(numpy_array[i,1] / numpy_array[i,2], 1)
print(numpy_array)