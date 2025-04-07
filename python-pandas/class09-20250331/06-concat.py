# %%

import pandas as pd

df_01 = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6, 7 ],
        "first_name": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "last_name": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "fatehr_last_name": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "age": [32, 35, 32, 30, 30, 32, 32],
        "wage": [3231, 5543, 5332, 6530, 1232, 12345, 23456],
    }
)

df_02 = pd.DataFrame(
    {
        "id": [8, 9 ],
        "first_name": ["bia", "zé" ],
        "last_name": ["costa", "barnabé"],
        "age": [32, 30],
        "wage": [6530, 1232],
    }
)

# %%

pd.concat([df_01, df_02])

# %%

pd.concat([df_02, df_01])

# %%

# if the columns are not in order the concat will break
# df_02.columns = df_02.columns.sort_values()
# df_02

# %%

pd.concat([df_01, df_02])

# %%

pd.concat([df_01, df_02], ignore_index=True)

# %%

df_03 = df_01.copy()

pd.concat([df_01, df_02, df_03], ignore_index=True)


# %%
