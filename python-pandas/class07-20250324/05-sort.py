
# %%

import pandas as pd

clients = pd.read_csv("../data/clientes.csv")
clients

# %%

clients.sort_values(by="qtdePontos").tail(5)

# %%

clients.sort_values(by="qtdePontos", ascending=False).head(5)

# %%

df = pd.DataFrame({
    "nome": ["teo", "nah", "mah", "lara",],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo",],
    "idade": [32, 35, 4, 32],
})

df.sort_values(by=["idade", "nome"], ascending=[False, True])

