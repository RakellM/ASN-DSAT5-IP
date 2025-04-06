# Exercise 5
# 05.01 - Create a new column “twitch_points”, which is the result of multiplying the points balance by the Twitch linkage indicator.
# 05.02 - Apply the log function to the points balance column, creating a new column.
# 05.03 - Create a column that indicates whether a person is linked to any (any) social media platform.
# 05.04 - What is the customer id with the highest points balance? And the lowest?
# 05.05 - Select the first daily transaction of each customer.

# %%

import pandas as pd
import os

# path_main = os.path.dirname(__file__)
path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data'  
path_file = os.path.join(path_main, "clientes.csv")

clients = pd.read_csv(path_file)

clients

# %%

clients.info()

# %%

#05.01

clients['twitch_points'] = clients['qtdePontos'] * clients['flTwitch']

# %%

clients.head(10)

# %%

# 05.02

import numpy as np

clients['log_qtdePontos'] = clients['qtdePontos'].apply(lambda x: np.log(x) if x > 0 else None)

# OR
# clients["log_qtdePontos"] = np.log(clients["qtdePontos"] + 1)

# %%

clients.head(10)


# %%

# 5.03

clients['flSocialMedia'] = clients[['flYouTube', 'flInstagram', 'flTwitch']].any(axis=1).astype(int)

# %%

clients.head(10)

# %%

# 5.04

c_high = clients.sort_values(by="qtdePontos", ascending=False).head(1)['idCliente']

print(f"Customer ID with the highest points balance: {c_high.values[0]}")

# %%

c_low = clients.sort_values(by="qtdePontos", ascending=True).head(1)['idCliente']

print(f"Customer ID with the lowest points balance: {c_low.values[0]}")

# %%
