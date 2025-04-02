# Exercise 4
# 04.01 - How many customers are linked to Twitch?
# 04.02 - How many customers have a points balance greater than 1000?
# 04.03 - How many transactions occurred on 2025-02-01?

# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv')

# %%

df.info()

# %%

# Filters: Method 1a

filter_twitch = df['flTwitch'] == 1

twitchCustomers = df[filter_twitch].shape[0]

print(f"Number of customers with Twitch account: {twitchCustomers}")

# %%

# Filters: Method 1b

twitchCustomers = df[df['flTwitch'] == 1].shape[0]

print(f"Number of customers with Twitch account: {twitchCustomers}")

# %%

# Method 3

(df['flTwitch'] == 1).sum()


# %%
