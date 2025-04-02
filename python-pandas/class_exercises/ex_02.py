# Exercise 2
# - Read the file transacoes.csv with the correct formatting.
# - Add a column with values 1.
# - Save the DataFrame with the name: transacoes_1.csv.

# %%

import pandas as pd
import os

path_main = os.path.dirname(__file__)
path_file = os.path.join(path_main, "../data/transacoes.csv")

df = pd.read_csv(path_file)

df

# %%

df['values'] = 1

df.head()


# %%

df.to_csv(os.path.join(path_main, "../data/transacoes_1.csv"), index=False)


# %%
