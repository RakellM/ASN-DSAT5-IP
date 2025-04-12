# %%

import pandas as pd
import os
import sqlalchemy

# %%

os.chdir(r"C:\Users\kel_m\OneDrive\Nerd_Code\DSAT5-IP\python-pandas")

os.getcwd()

# %%

engine = sqlalchemy.create_engine("sqlite:///./data/olist.db")
engine

# %%

query = """
SELECT seller_id , count(*)
FROM tb_order_items
GROUP BY 1
"""

# %%

with open("class10-20250402/etl.sql") as open_file:
    query = open_file.read()

print(query)

# %%

df = pd.read_sql(query, engine)
df.head()

# %%

# Hypothetical model: clustering sellers

from sklearn import cluster

kmeans = cluster.KMeans(n_clusters=5, random_state=42)

kmeans.fit(df[["frequency" , "amount"]])

# %%

df["cluster"] = kmeans.labels_
df

# %%

import matplotlib.pyplot as plt

plt.scatter(df["frequency"], df["amount"])

# %%

for i in pd.Series(kmeans.labels_).unique():
    X = df[df["cluster"] == i]
    plt.scatter(X["frequency"], X["amount"])

plt.grid(True)

# %%

for i in df["cluster"].unique():
    X = df[df["cluster"] == i]
    plt.scatter(X["frequency"], X["amount"])

plt.grid(True)

# %%

df.to_sql("seller_cluster", engine, if_exists="replace")

# %%
