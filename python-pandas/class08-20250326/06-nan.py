# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%

# remove a row if any column has a NA
df.dropna()

# %%

# same as the above
df.dropna(how='any')

# %%

# remove columns have have NA
df.dropna(how='any', axis=1)

# %%

#-- threshhold: how many non NA I can have in a row (minimum non NA)
#-- reading this: I will drop the columns that have less than 70% of complete rows
df.dropna(thresh=int(0.3 * df.shape[0]), axis=1)

# %%

df.dropna(subset=["dtCriacao"])


# %%

df = pd.DataFrame(
    {
        "first_name": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "last_name": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "age": [32, 35, 32, 30, 32, 32, 32],
        "wage": [3231, 5543, 5332, 6530, 1232, None, None],
    }
)

df

# %%

# guess the value of the wage  to replace the NAs
mean = df["wage"].mean()
mean

print("Mean:", mean)

new_mean = df["wage"].fillna(mean).mean()
new_mean

print("New Mean:", new_mean)

# %%

std = df["wage"].std()

print("Std:", std)

new_std = df["wage"].fillna(mean).std()

print("New Std:", new_std)

# %%

df["new_wage"] = df["wage"].fillna(mean)

df


