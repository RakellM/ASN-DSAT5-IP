# %%

import pandas as pd
import os

path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data' 

df_general = pd.read_excel(os.path.join(path_main, "homicidios/homicidios.xlsx"))
df_general = df_general.rename(columns={"valor": "homicidios"})
df_general.head()

# %%

df_negros = pd.read_excel(os.path.join(path_main, "homicidios/homicidios-negros.xlsx"))
df_negros = df_negros.rename(columns={"valor": "nohomicidios"})
df_negros.head()

# %%

# want to keep "nome" and "período" and change "value" to the name of the file

df_general = df_general.set_index(["nome", "período"])
df_negros = df_negros.set_index(["nome", "período"])

# %%

pd.concat([df_general, df_negros], axis=1)

# %%

# Making it better

import pandas as pd
import os

path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data' 

df_general = pd.read_excel(os.path.join(path_main, "homicidios/homicidios.xlsx"))
df_general = df_general.rename(columns={"valor": "homicidios"})
df_general = df_general.set_index(["nome", "período"])
df_general = df_general.drop(["cod"], axis=1)
df_general.head()

df_negros = pd.read_excel(os.path.join(path_main, "homicidios/homicidios-negros.xlsx"))
df_negros = df_negros.rename(columns={"valor": "nohomicidios"})
df_negros = df_negros.set_index(["nome", "período"])
df_negros = df_negros.drop(["cod"], axis=1)
df_negros.head()

# %%

# creating a function

import pandas as pd
import os

path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data' 

def read_file(file_name:str):
    
    df = (pd.read_excel(os.path.join(path_main, f"homicidios/{file_name}.xlsx"))
            .rename(columns={"valor": {file_name}})
            .set_index(["nome", "período"])
            .drop(["cod"], axis=1)
)

    return df

# %%
df_general = read_file("homicidios")
df_general

# %%

file_names = os.listdir(os.path.join(path_main, "homicidios"))

dfs = []

for i in file_names:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))

# %%
df_general = read_file("homicidios")
df_general

# %%

df_full = (pd.concat(dfs, axis=1)
             .reset_index()
             .sort_values(["nome", "período"]))

df_full.to_csv("homicidios_consolidado.csv", index=False)
