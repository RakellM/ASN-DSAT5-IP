# Exercise 5
# 05.05 - Select the first daily transaction of each customer.

# %% 

import pandas as pd
import os

# path_main = os.path.dirname(__file__)
path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data'  
path_file = os.path.join(path_main, "transacoes.csv")

transactions = pd.read_csv(path_file)

transactions

# %%

transactions.info()

# %%

transactions['dayCreated'] = pd.to_datetime(transactions['dtCriacao']).dt.date

transactions.head()

# %%

transactions.sort_values(by=['dayCreated'], ascending=[True], inplace=True)

transactions

# %%

transactions.drop_duplicates(subset=['idCliente'], keep='first', inplace=True)

transactions.head(10)

# %%

(transactions.sort_values(by=['dayCreated'], ascending=[True])
    .drop_duplicates(subset=['idCliente', 'dayCreated'], keep='first'))

# %%

transactions.shape

# %%

(transactions.sort_values(by=['dayCreated'], ascending=[True])
    .drop_duplicates(subset=['idCliente', 'dayCreated'], keep='first')).shape


