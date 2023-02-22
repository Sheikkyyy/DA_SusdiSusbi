import pandas as pd
import numpy as np
import matplotlib as plt

dataset = pd.read_excel(r'C:\Users\haris\PycharmProjects\ASP_Labs\PYProjectNew\Project_File.xlsx')

#print(dataset)



#dimension of dataset
dataset_dim = dataset.shape


#renaming the first column to date
dataset_2 = dataset.rename(columns={dataset.columns[0]:'Date'})
print(dataset_2)

#removing white space in columns


#creating region
region_asia = dataset_2[['Date', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]

print(region_asia)

#filtering to year
years_dataset = region_asia[360:480]

print(years_dataset)

#plotting of graph
