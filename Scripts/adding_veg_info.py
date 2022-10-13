import pandas as pd
import csv

vegInfo = pd.read_csv("Data/Raw/BigGrids_Veg.csv")

vegInfo.rename(columns={'Unnamed: 0': 'location'}, inplace=True)
print(vegInfo)