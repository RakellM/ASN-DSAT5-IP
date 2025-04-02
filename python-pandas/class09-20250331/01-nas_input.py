# %%

import pandas as pd

df = pd.DataFrame(
    {
        "first_name": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "last_name": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "age": [32, 35, None, 30, None, 32, 32],
        "wage": [3231, 5543, 5332, 6530, 1232, None, None],
    }
)

# %%
mean_age = df["age"].mean()
mean_wage = df["wage"].mean()


# %%
df.fillna({
    "age": mean_age , 
    "wage": mean_wage
    })

# %%

means = df[['age', 'wage']].mean()
df.fillna(means)

# %%
