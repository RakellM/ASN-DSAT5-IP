
# %%

import pandas as pd

ages = pd.Series([32, 34, 56, 43], name='ages')
names = pd.Series(['Teo', 'nah', 'ana', 'jose'], name='names')


# %%

df = pd.DataFrame()
df['ages'] = ages
df['names'] = names
df

# %%

df['names']

# TATTOO: A DataFrame is a group of Series.

# %%

#-- get the name in the 3rd position (return a Series where index are the same as the DF)
df['names'].iloc[2]

# %%

#-- get the 3rd row of the data frame (return a Series where index are the column names)
df.iloc[2]

# %%

#-- change the order will give us the same result:
df['names'].iloc[2]

# %%

#-- change the order will give us the same result:
df.iloc[2]['names']

# %%

df['wages'] = [4324, 5436, 5432, 4564]
df

# %%

df[['wages', 'names']]

# %%

columns = ['wages', 'names']
df[columns]

# %%

df['wages'] # returns a series

# %% 

df[['wages']] # returns a DataFrame

# %%

df = df[['names', 'ages', 'wages']]
df

# %%

df_01 = df[['names', 'ages']]
df_01

