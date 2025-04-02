# %%

import pandas as pd

df = pd.DataFrame(
    {
        "first_name": ["teo", "nah", "ana", "leo", "bia", "teo", "teo" ],
        "last_name": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "age": [32, 35, 32, 30, 32, 32, 32],
    }
)

df

# %%

df.drop_duplicates()
#-- remove all rows that are duplicated and keep first one

# %%

df.drop_duplicates(keep='last')
#-- remove all rows that are duplicated and keep last one

# %%

#--subset, keep the first one of each last name
df.drop_duplicates(subset=["last_name"])

# %%

df.drop_duplicates(subset=["last_name"], keep='last')

# %%

df.sort_values(by=["first_name"]).drop_duplicates(subset=["last_name"], keep='last')

# %%

df.sort_values(by=["first_name"]).drop_duplicates(subset=["last_name", "age"], keep='last')

# %%
