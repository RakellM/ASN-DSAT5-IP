# %%

import pandas as pd
import os

path_main = r'C:/Users/kel_m/OneDrive/Nerd_Code/DSAT5-IP/python-pandas/data' 

df = pd.read_excel(os.path.join(path_main, "homicidios/homicidios.xlsx"))
df

# %%

df.info()

# %%

df.set_index(['nome', 'período']).unstack()

# %%

df_pivot = df.pivot_table(values='valor', columns= 'nome', index='período')
df_pivot

# %%

df_pivot.stack().reset_index()


# %%

df1 = pd.read_excel(os.path.join(path_main, "homicidios/homicidios.xlsx"))
df2 = pd.read_excel(os.path.join(path_main, "homicidios/homicidios-negros.xlsx"))

df2
# %%

df1 = df1.rename(columns={"valor": "homicidios_geral"}).set_index(['nome', 'período'])
df2 = df2.rename(columns={"valor": "homicidios_negros"}).set_index(['nome', 'período'])

pd.concat([df1, df2], axis=1)

# %%
