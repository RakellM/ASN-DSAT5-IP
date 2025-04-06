# Exercise 3
# 03.02 - How many integer-type columns are there in the file transacoes.csv?

# %%

import pandas as pd
import os

# path_main = os.path.dirname(__file__)
path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data'  
path_file = os.path.join(path_main, "clientes.csv")

clients = pd.read_csv(path_file)

clients

# %%

(clients.dtypes == 'int64').sum()

print(f"Number of integer-type columns: {clients.dtypes[clients.dtypes == 'int64'].count()}")


