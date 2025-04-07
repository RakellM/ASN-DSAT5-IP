
# %%
import pandas as pd

df_client = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6, 7 ],
        "first_name": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "last_name": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "fatehr_last_name": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "age": [32, 35, 32, 30, 30, 32, 32],
        "wage": [3231, 5543, 5332, 6530, 1232, 12345, 23456],
    }
)

df_sales = pd.DataFrame(
    {
        "id": [1,2,3,4,5,6,7,8],
        "idCliente": [1,1,2,2,5,4,3,3],
        "name": ["A","B","A","C","A","D","A","B"]
    }
)

# %%

df_sales.merge(right=df_client, 
               how="inner",
               left_on="idCliente", 
               right_on="id", 
               suffixes=("_sales", "_client"),
               )

# %%

# example

# dfs = []
# for i in files:
#     dfs.append(pd.read_csv(i))

# pd.concat(dfs, ignore_index=True)
