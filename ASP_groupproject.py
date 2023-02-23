#QF2204A

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dataset = pd.read_excel(r"./Project_File.xlsx")

#print(dataset)



# dimension of dataset
dataset_dim = dataset.shape


# renaming the first column to date
dataset_2 = dataset.rename(columns={dataset.columns[0]:'year_month'})
print(dataset_2)

# To Do: removing white space in columns

# split the year_month to year and month columns
dataset_2["year"] = dataset_2["year_month"].str.split().str[0]
dataset_2["month"] = dataset_2["year_month"].str.split().str[1]

print(dataset_2)

# creating region
region_asia_df = dataset_2[['year', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]


#print(region_asia_df)

# cast to integer
#region_asia_df = region_asia_df.astype("int")
region_asia_df = region_asia_df.astype({'year':'int'})

#print(region_asia_df.dtypes)

#filtering to year
years_dataset = region_asia_df[(region_asia_df["year"] >= 2008) & (region_asia_df["year"] <= 2017)]

years_dataset = years_dataset.astype('int')

print(years_dataset.dtypes)


#sum
total_sum_df = years_dataset.sum()

print(total_sum_df)

#remove year column
total_sum_df = total_sum_df.drop('year', axis = 0)

print(total_sum_df)
#plot
ps = total_sum_df[:].sort_values()
index = np.arange(len(ps.index))
plt.xlabel("Country")
plt.ylabel("total sum")
plt.xticks(index, ps.index, fontsize=10, rotation=90)
plt.title("sum of visitor by country")
plt.bar(ps.index, ps.values)
plt.show()

#top 3