# 04.03 - How many transactions occurred on 2025-02-01?

# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv')

# %%

df.info()

# %%

df.head(2)

# %%

# No Data Transformation

filter_floor = df['dtCriacao'] >= '2025-02-01'
filter_ceiling = df['dtCriacao'] < '2025-02-02'

filter_date = filter_floor & filter_ceiling

transactionCount = df[filter_date]

transactionCount

# %%

# Data Transformation

datetime_ = pd.to_datetime(df['dtCriacao']).dt.date.astype(str)

(datetime_ == '2025-02-01').sum()

datetime_

# %%
