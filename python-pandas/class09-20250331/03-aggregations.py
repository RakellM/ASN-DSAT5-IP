# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

df[df["qtdePontos"]>0]["qtdePontos"] .sum()

# %%

df["qtdePontos"].describe()

# %%

df.describe()

# %%
df.columns

# %%

df_product_transaction = pd.read_csv("../data/transacao_produto.csv")
df_product_transaction["idProduto"] = df_product_transaction["idProduto"].astype(str)
df_product_transaction.describe()

# %%
df_product_transaction[['idTransacaoProduto','idTransacao','idProduto']].describe()

# %%

df.groupby(by="idCliente")[["qtdePontos"]].sum()


# %%

df = pd.DataFrame(
    {
        "first_name": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "last_name": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "father_last_name": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "age": [32, 35, 32, 30, 30, 32, 32],
        "wage": [3231, 5543, 5332, 6530, 1232, 12345, 23456],
    }
)

df


# %%

def amplitude(x):
    return max(x) - min(x)

grouped = df.groupby(by="last_name").agg({"age": "mean",
                                           "wage": ["median", "mean", amplitude],
                                           "first_name":"count"})

grouped

# %%
grouped[[("wage", "mean"), ("wage", "amplitude")]]

# %%

grouped.columns = ["age_mean",
                   "wage_median",
                   "wage_mean",
                   "wage_amplitude",
                   "qty_first_name"]
grouped
# %%
