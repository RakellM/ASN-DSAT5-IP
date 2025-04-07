# %%

import pandas as pd
import os

path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data' 

transactions = pd.read_csv(os.path.join(path_main, "transacoes.csv"))
transaction_product = pd.read_csv(os.path.join(path_main, "transacao_produto.csv"))
products = pd.read_csv(os.path.join(path_main, "produtos.csv"))

# %%

transactions.info()

# %%

transaction_product.info()

# %%

transactions.merge(right=transaction_product)
#-- it merge using the column name that are the same in both dataframes

# %%

transactions.merge(right=transaction_product, 
                   on=['idTransacao'])
#-- it can be used ON to specify the column name: IF the column names are the same

# %%

transactions.merge(right=transaction_product, 
                   right_on=['idTransacao'],
                   left_on=['idTransacao'])
#-- it can be used RIGHT_ON and LEFT_ON to specify the column name: IF the column names are different

# %%

transactions.merge(right=transaction_product, 
                   how='left',
                   on=['idTransacao'])
#-- default join is INNER

# %%

# example
# s1 = transactions.sample(10000)
# s1['dayCreated'] = pd.to_datetime(s1['dtCriacao'])

# s1.merge(transactions)

# %%

join = transactions.merge(right=transaction_product, 
                   how='left',
                   on=['idTransacao'])

join = join.merge(products)

filter_streak = join['descProduto'].str.contains("Streak")

(join[filter_streak].groupby(['idCliente'])['idTransacao']
                    .count()
                    .sort_values(ascending=False)
                    .head(1))

# %%

# all at once is also possible
join = (transactions.merge(right=transaction_product, 
                   how='left',
                   on=['idTransacao'])
                    .merge(products))
# as the first join is a data frame it can be done another join on a sequence

filter_streak = join['descProduto'].str.contains("Streak")

(join[filter_streak].groupby(['idCliente'])['idTransacao']
                    .count()
                    .sort_values(ascending=False)
                    .head(1))

