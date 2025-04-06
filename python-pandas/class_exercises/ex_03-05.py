# Exercise 3
# 03.05 - What is the points balance of the customer at position 10 (without sorting) in the file clientes.csv?

# %%

import pandas as pd
import os

# path_main = os.path.dirname(__file__)
path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data'  
path_file = os.path.join(path_main, "clientes.csv")

clients = pd.read_csv(path_file)

# %%

clients['qtdePontos'].iloc[9]

# %%
