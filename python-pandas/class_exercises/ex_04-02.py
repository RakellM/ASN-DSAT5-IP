# Exercise 4
# 04.02 - How many customers have a points balance greater than 1000?

# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv')

# %%

df.info()

# %%

# Method 1

filter_points = df['qtdePontos'] > 1000

Customers = df[filter_points].shape[0]

print(f"Number of customers with mopre than 1,000 points: {Customers}")

# %%

# Method 2

(df['qtdePontos'] > 1000).sum()

# %%

# If I want to know the Customer IDs for those customers with more than 1,000 points:

df[df['qtdePontos'] > 1000]['idCliente']

# %%
