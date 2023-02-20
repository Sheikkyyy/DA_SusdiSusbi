import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_excel(r'C:\Users\haris\PycharmProjects\ASP_Labs\PYProjectNew\Project_File.xlsx')

print(df)

class calSusbisusdi:
    def __init__(self):
        self.country = []
        self.date = []
        self.avgvisitor = []
        self.totalcountry = 0
        self.totalavgvisitor = 0

    #function

    def calamtofppl(self):
        country = []
        date = []
        avgvisitor = []

