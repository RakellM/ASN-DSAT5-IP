# Exercise 3
# 03.01 - How many rows are there in the file clientes.csv?
# 03.02 - How many integer-type columns are there in the file transacoes.csv?
# 03.03 - How many object-type columns are there in the file produtos.csv?
# 03.04 - What is the id of the customer at index 4 in the file clientes.csv?
# 03.05 - What is the points balance of the customer at position 10 (without sorting) in the file clientes.csv?

# %%

import pandas as pd
import os

path_main = os.path.dirname(__file__)
path_file = os.path.join(path_main, "../data/clientes.csv")

clients = pd.read_csv(path_file)

clients

# %%

clients.info()

# %%

clients.shape
# (rows, columns)


# %%

clients.shape[0]  # number of rows

# %%

print(f"Number of rows: {clients.shape[0]:,.0f}")

# %%
