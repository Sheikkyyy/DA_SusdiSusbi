# QF2204A
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#class
class data_analyse:
    def _init_(self):
        self.dataset = pd.read_excel(r"./Project_File.xlsx")
        self.top3 = []

    #funcion
    def process_data(self):
        dataset_2 = self.dataset.rename(columns={self.dataset.columns[0]: 'year_month'})
        dataset_2["year"] = dataset_2["year_month"].str.split().str[0]
        dataset_2["month"] = dataset_2["year_month"].str.split().str[1]
        region_asia_df = dataset_2[['year', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
                                    ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
                                    ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
                                    ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]
        region_asia_df = region_asia_df.astype({'year': 'int'})
        years_dataset = region_asia_df[(region_asia_df["year"] >= 2008) & (region_asia_df["year"] <= 2017)]
        years_dataset = years_dataset.astype('int')

        print(years_dataset)

        total_sum_df = years_dataset

        total_sum_df = total_sum_df.sum()
        total_sum_df = total_sum_df.sort_values(ascending=False)
        print(total_sum_df)

        self.top3 = total_sum_df.index[0:3]
        print(self.top3)

        return total_sum_df

    #function show graph
    def showgraph(self, total_sum_df):
        ps = total_sum_df[:].sort_values(ascending=False)
        index = np.arange(len(ps.index))
        plt.xlabel("Country")
        plt.ylabel("total sum")
        plt.xticks(index, ps.index, fontsize=10, rotation=90)
        plt.title("sum of visitor by country")
        plt.bar(ps.index, ps.values)
        plt.ticklabel_format(useOffset=False, style='plain', axis='y')
        plt.show()

dataAna = data_analyse()

df = dataAna.process_data()
dataAna.showgraph(df)