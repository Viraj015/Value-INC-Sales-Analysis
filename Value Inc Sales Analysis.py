# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:34:40 2022

@author: Viraj
"""
# Importing Libraries
import pandas as pd
import numpy as np

data = pd.read_csv('transaction.csv', sep=';')

# Summary of Data
data.info()

# Woking with calculations
# Column Calculations

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
data['CostPerTransaction'] = CostPerItem * NumberOfItemsPurchased

#Sales Per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['MarkUp'] = (data['ProfitPerTransaction'])/data['CostPerTransaction']
data['MarkUp'] = round(data['MarkUp'], 2)

# Modifying Dates/Combining data fields
# Changing data type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
data['Date'] = day+'-'+data['Month']+'-'+year

# Using iloc to view specific columns/rows

# Using split to split client keywords
Split_col = data['ClientKeywords'].str.split(',', expand=True)

# Columns for split columns in our dataframe
data['ClientAge'] = Split_col[0]
data['ClientType'] = Split_col[1]
data['LengthOfContract'] = Split_col[2]

#Using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

# Using lower case for item description
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Merging 2 files
Seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')
New_data = pd.merge(data, Seasons, on = 'Month')

# Dropping Columns
New_data = New_data.drop('ClientKeywords', axis =1)
New_data = New_data.drop('Day', axis =1)
New_data = New_data.drop(['Year', 'Month'], axis =1)

# Export our cleaned file to csv
New_data.to_csv('ValueInc_Cleaned.csv', index = False)












