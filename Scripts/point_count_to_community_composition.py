import pandas as pd
import csv

# Set your working directory
data = pd.read_csv("BU_Big_Grids_basic_summary.csv")

# dummies from the species code column, drops column
data['dummies'] = data['species_code']

abundance = pd.get_dummies(data=data, columns= ['dummies'], prefix='', prefix_sep='')

# extract only desired columns
thisList = ['location',	'recording_date','longitude',	'latitude'	, 'species_code']
# dictionary of codes to common names
desiredCodes = pd.read_csv("DesiredCodes.csv")
desiredCodeslist = desiredCodes['Codes'].to_list()
desiredcolumnsList = thisList + desiredCodeslist

# make a dict of the aggregate function for each column. For the species code (length 4), use sum. Use first for the rest. Exclude 'location at indox 0.
columns_dictB =  { i : 'sum' for i in desiredcolumnsList[1:] if len(i) == 4}
columns_dictA = { i : 'first' for i in desiredcolumnsList[1:] if len(i) != 4}
columns_dictA.update(columns_dictB)
# Agg function for species_code is the list of all species counted at that location.
columns_dictA['species_code'] = lambda x: list(x)

# Use selcted columns only
df1 = abundance[desiredcolumnsList]

# Group the report by unique location 
grouped = df1.groupby('location').agg(columns_dictA)

grouped.to_csv('Data/Processed/community_abundance_by_location.csv')