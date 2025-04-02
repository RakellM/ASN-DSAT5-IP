# %%

import pandas as pd

df = pd.DataFrame(
    {
        "first_name": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "last_name": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "father_last_name": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "age": [32, 35, None, 30, None, 32, 32],
        "wage": [3231, 5543, 5332, 6530, 1232, None, None],
    }
)

df 

# %%

df = df.replace({
    "father_last_name": {"silva": "costa", "calvo": "balbino"},
    "last_name":{"ataide": "gironde"}
})

df
# %%

df["father_last_name"] = df["father_last_name"].replace({"silva": "costa", "calvo": "balbino"})
df["last_name"] = df["father_last_name"].replace({"ataide": "gironde"})
df
