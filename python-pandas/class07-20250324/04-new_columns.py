
# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head(2)

# %%

df["unitaryColumn"] = 1
df

# SELECT *,
#        1 as unitaryColumn

# FROM clientes

# %%

df["points_x10"] = df["qtdePontos"] * 10
df

# %%
df["pointsTwitch"] = df["flTwitch"] * df["qtdePontos"]
df

# %%
df["qtdePontos"].describe()

# %%

import matplotlib.pyplot as plt

df["qtdePontos"].hist(color='#F80373')
plt.title("Histogram of Points")
plt.xlabel("Value Points")
plt.ylabel("Frequency")
plt.show()

# %%

import numpy as np

df["qtyPointsLog"] = np.log(df["qtdePontos"]+1)
df["qtyPointsLog"].hist()
plt.title("Histogram of Log Points")
plt.xlabel("Value Log Points")
plt.ylabel("Frequency")
plt.savefig("log-points.png")

# %%
