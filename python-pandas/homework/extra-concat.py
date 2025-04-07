# %%

import pandas as pd

df = pd.DataFrame({
    "client": [1,2,3,4,5],
    "name": ["teo", "jose", "nah", "mah", "lah"],
})

df_02 = pd.DataFrame({
    "client": [6,7,8],
    "name": ['kozato','laura','dan'],
    "age": [32,29,31]
})

df_03 = pd.DataFrame({
    "age": [32,34,19,54,33],
})

# %%

dfs = [df, df_02]

pd.concat(dfs, ignore_index=True)

# %%

df_03 = df_03.sort_values(by='age')
df_03

# %%

pd.concat([df, df_03], axis=1)
# even when df_03 is sorted the concat is being done by the index

# %%

df_03 = df_03.sort_values(by='age').reset_index(drop=True)
df_03

# %%

pd.concat([df, df_03], axis=1)

# %%
