import pandas as pd
import numpy as np
import matplotlib as plt

dataset = pd.read_excel(r'C:\Users\haris\PycharmProjects\ASP_Labs\PYProjectNew\Project_File.xlsx')

print(dataset)
#renaming the first column to date
dataset_1 = dataset.rename(columns={'   ': 'Date'})
print(dataset_1)

