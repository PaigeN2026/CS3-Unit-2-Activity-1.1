import pandas as pd
import numpy as np

# PART A: Load & view 
df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())
print('How mant rows and columns in the whole dataset')

print(df.shape)

print(' ')

print(df.info()) # summary of columns 

print(' ')


# Fill in brackets with a CONDITIONAL
# Filter films that cost over a million dollars 
# df['budget'] grab the column you want
budget_df = df[ df['budget'] > 1000000]
print(budget_df.shape) # 7208 movies have a budget above 1mil 

print(' ')

# Create a series from the budget column 
# that uses the title column for the indicies 
# Fill in the parameters for (values, index)
budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['title'])
print(budget_lookup) # now we can look up budgets by movie title

print(' ')

print(budget_lookup['Sabrina']) # 2 mil and 58 mil

print(' ')

print(budget_lookup[budget_lookup.index.str.startswith('A')].sort_index()[[0]])

print(' ')

print(budget_lookup[budget_lookup.index.str.startswith('B')].sort_index()[[-1]])

condition = budget_lookup[budget_lookup.index.str.startswith('B')].sort_index()[[-1]] 

# First define the condition to be checked
# budget_lookup.index is the title of the movie 
condition = (budget_lookup.index >= 'A Bag of Hammers') & (budget_lookup.index <= 'Byzantium')
# condition is satisfied when the movie starts with A or B
budget_lookup_AB = budget_lookup[condition]
print(budget_lookup_AB)

print(' ')
# PART C: Number as indices (loc vs iloc)

# Create a series with runtime as the index
runtime_lookup = pd.Series(df['title'].values, index=df['runtime'])
runtime_lookup = runtime_lookup.sort_index()

# We want to look up movies TITLES by their RUNTIME
# So we use the titles as the VALUES and the runtime as the INDEXES

print(' ')

# Filter series by removing movies > 180 min
# and < 10 min, pulling only rows that are in between
condition2 = (runtime_lookup.index > 10) & (runtime_lookup.index < 180)
runtime_lookup = runtime_lookup[condition2]
print(runtime_lookup)

# Use our series lookup object to answer questions 
# Which movies are exactly 40 minutes long? (have an index of 40.0)
print(runtime_lookup.loc[40]) # .loc retrieves by explicit index 

print(' ')

# How many movies are 40 mins?
print(runtime_lookup.loc[40].shape) # (42,) means 42 (entries)

print(' ')

# In contrast: .iloc locates entries by their POSITIONAL index
# What is the 100th shortest film in the series? 
print(runtime_lookup.iloc[100]) # what movie is at the 100th row here? 
# the i in loc stands for 'implicit' like the implied index rather than the index that's explicitly there 