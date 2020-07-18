#Import pandas, which is python's data analysis library
import pandas as pd

#load data from data file - 'dataset.csv'
data = pd.read_csv("dataset.csv", delimiter = ',' , index_col = "material")

#Sanity check - print the first 5 rows
#print(data.head())

#Another sanity check
