import pandas as pd
import numpy as np

df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())
print('How mant rows and columns in the whole dataset')
print(df.shape)
print(df.info()) # summary of columns 

# Fill in brackets with a CONDITIONAL
# Filter films that cost over a million dollars 
# df['budget'] grab the column you eant
budget_df = df[ df['budget'] > 1000000]
print(budget_df.shape) # 7208 movies have a budget above 1mil 
