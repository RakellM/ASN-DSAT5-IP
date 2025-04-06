# Exercise 3
# 03.03 - How many object-type columns are there in the file produtos.csv?

# %%

import pandas as pd
import os

# path_main = os.path.dirname(__file__)
path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data'  
path_file = os.path.join(path_main, "produtos.csv")

products = pd.read_csv(path_file)

products

# %%
products.dtypes == 'object'

# %%

(products.dtypes == 'object').sum()

print(f"Number of object-type columns: {(products.dtypes == 'object').sum()}")


