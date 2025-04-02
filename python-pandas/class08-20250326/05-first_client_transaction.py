# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()


# %%
#-- can order both, but idClientes doesnt need to be ordered
df.sort_values(["idCliente","dtCriacao"])

# %%

(df.sort_values(["dtCriacao"])
   .drop_duplicates(subset=["idCliente"], keep='first'))

# %%

# OR

(df.sort_values(["dtCriacao"], ascending=False)
   .drop_duplicates(subset=["idCliente"], keep='last'))


# %%

# 05.05 - Select the first daily transaction of each client.

df["diaCriacao"] = pd.to_datetime(df["dtCriacao"]).dt.date

(df.sort_values(["idCliente" , "dtCriacao"])
   .drop_duplicates(subset=["idCliente", "diaCriacao"]))

# %%


