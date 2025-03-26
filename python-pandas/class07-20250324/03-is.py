
# %%

import pandas as pd

customers = pd.read_csv('../data/clientes.csv')
customers

# %%

customers[customers['dtCriacao'].isna()]

# %%

# customers[~customers['dtCriacao'].isna()]

customers[customers['dtCriacao'].notna()]

# %%

products = pd.read_csv('../data/produtos.csv')
products

filer_products = ['Lista de presença',
                  'Presença Streak',
                  'Resgatar Ponei']

filter = products["descProduto"].isin(filer_products)

products[filter]
