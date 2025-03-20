
# %%

import pandas as pd
import os

# %%

os.getcwd()

# %%

df = pd.read_csv("../data/clientes.csv")
df

# %%

df.to_excel("clientes.xlsx")

# %%

df_excel = pd.read_excel("clientes.xlsx")
df_excel

# %%
df.to_parquet("clientes.parquet")

# %%
transactions = pd.read_csv("../data/transacoes.csv")
transactions.to_parquet("transacoes.parquet", index=False)

# %%

df_trans = pd.read_parquet("transacoes.parquet")


# %%

ufs = pd.read_clipboard(header=None)
ufs

# %%

ufs.columns

# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)

# %%

#-- We will have a list of DataFrames
dfs

# %%

len(dfs)

# %%

uf = dfs[1]
uf

# %%

uf.to_csv('ufs.csv', index=False, sep=";")

