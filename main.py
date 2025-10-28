import pandas as pd
import numpy as np

df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())
print('How mant rows and columns in the whole dataset')
print(df.shape)
print(df.info()) # summary of columns 

# Fill in brackets with a CONDITIONAL
# Filter films that cost over a million dollars 
# df['budget'] grab the column you want
budget_df = df[ df['budget'] > 1000000]
print(budget_df.shape) # 7208 movies have a budget above 1mil 

# Create a series from the budget column 
# that uses the title column for the indicies 
# Fill in the parameters for (values, index)
budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['title'])
print(budget_lookup) # now we can look up budgets by movie title
print(budget_lookup['Sabrina']) # 2 mil and 58 mil

print(budget_lookup[budget_lookup.index.str.startswith('A')].sort_index()[[0]])
print(budget_lookup[budget_lookup.index.str.startswith('B')].sort_index()[[-1]])

condition = budget_lookup[budget_lookup.index.str.startswith('B')].sort_index()[[-1]] 

# First define the condition to be checked
# budget_lookup.index is the title of the movie 
condition = (budget_lookup.index >= 'A Bag of Hammers') & (budget_lookup.index <= 'Byzantium')
# condition is satisfied when the movie starts with A or B
budget_lookup_AB = budget_lookup[condition]
print(budget_lookup_AB)