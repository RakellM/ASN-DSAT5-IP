# Exercise 6
# 06.01 - What is the average number of social media platforms per user? And the variance? And the maximum?
# 06.02 - Who are the users who made the most transactions? Consider the top 10.
# 06.03 - Which user had the highest amount of debited points?
# 06.04 - Who had the most Streak transactions?
# 06.05 - What is the average number of transactions per day?
# 06.06 - How can we calculate the descriptive statistics of transaction points for each user?
    
# %%

import pandas as pd
import os

# path_main = os.path.dirname(__file__)
path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data'  
path_file = os.path.join(path_main, "clientes.csv")

clients = pd.read_csv(path_file)

clients.info()

# %%

# 06.01

columns_ = ['flTwitch','flYouTube','flBlueSky','flInstagram']

clients[columns_].sum(axis=1).describe()

# %%

path_file = os.path.join(path_main, "transacoes.csv")

transactions = pd.read_csv(path_file)

transactions.info()

# %%

# 06.02

(transactions.groupby('idCliente')['idTransacao']
             .count()
             .sort_values(ascending=False)
             .head(10))

# %%

# 06.03

(transactions[transactions['qtdePontos'] < 0].groupby('idCliente')['qtdePontos']
                                             .sum()
                                             .sort_values(ascending=True)
                                             .head(1))

# %%

path_file = os.path.join(path_main, "produtos.csv")

products = pd.read_csv(path_file)

products

# %%

path_file = os.path.join(path_main, "transacao_produto.csv")

transaction_product = pd.read_csv(path_file)

transaction_product.head()

# %%

# 06.04
# idProduto = 12 is Presença Streak

filter_ = transaction_product[transaction_product['idProduto'] == 12]['idTransacao']

(transactions[transactions['idTransacao'].isin(filter_)]
                                         .groupby(by='idCliente')['idTransacao']
                                         .count()
                                         .sort_values(ascending=False)
                                         .head(1))

# %%

# 06.05

transactions['dayCreated'] = pd.to_datetime(transactions['dtCriacao']).dt.date

transactions['dayCreated'] 

# %%

len(transactions['dayCreated'] )

# %%

transactions['dayCreated'].unique()

# %%

len(transactions['dayCreated'].unique())

# %%

transactions['dayCreated'].nunique()

# %%

# transactions['idTransacao'].count() / transactions['dayCreated'].nunique()

transactions['idTransacao'].nunique() / transactions['dayCreated'].nunique()

# %%

# 06.06

(transactions.groupby(by='idCliente')['qtdePontos']
             .describe())


