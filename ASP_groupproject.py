import pandas as pd
import numpy as np
import matplotlib as plt

dataset = pd.read_excel(r'C:\Users\haris\PycharmProjects\ASP_Labs\PYProjectNew\Project_File.xlsx')

print(dataset)

#dimension of dataset
dataset_dim = dataset.shape

#renaming the first column to date
dataset_2 = dataset.rename(columns={'   ': 'Date'})
print(dataset_2)

#removing the missing value
dataset_3 = dataset_2.dropna()

#checking the dimension
dataset_3

#creating region
region_asia = dataset_3[['date','Brunei Darussalam','Indonesia','Malaysia',
                    'Philippines','Thailand','Viet Nam','Myanmar',
                    'Japan','Hong Kong','China','Taiwan',
                    'Korea, Republic Of','India'
                    ]]
