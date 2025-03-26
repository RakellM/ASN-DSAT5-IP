
# %%

ages = [22, 25, 30, 35, 13, 40, 45, 60, 65, 16, 12, 15, 18, 20]

ages_18_plus = []

for age in ages:
    if age >= 18:
        ages_18_plus.append(age)

ages_18_plus

# %%

check_age = []

for age in ages:
    check_age.append(age >= 18)

check_age

# %%

check_age = []
for age in ages:
    check_age.append(age >= 18)

ages_18_plus = []
for i in range(len(ages)):
    if check_age[i]:
        ages_18_plus.append(ages[i])

ages_18_plus

# %%

import pandas as pd

s_ages = pd.Series(ages)

check_age_series = s_ages >= 18

s_ages[check_age_series]

# %%

df = pd.read_csv("../data/clientes.csv")
df.head(2)

# %%

filter = df["qtdePontos"] > 1000

df[filter]

# %%

columns_social = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
df[columns_social] == 1

# %%

filter_email = df["flEmail"] == 1
filter_twitch = df["flTwitch"] == 1
filter_general = filter_email & filter_twitch

filtro_geral
# %%
df[filter_general].shape

# %%

