
# %%

import pandas as pd

# %%

age = [32, 12, 43, 26, 72, 13, 45, 32, 67, 86, 34]

#-- Calculate mean
mean_ = sum(age) / len(age)

print(f"Mean: {mean_}")

#-- Calculate Variance
total = 0
for i in age:
    total += ((i - mean_) ** 2)

variance_ = total / (len(age) - 1)
print(f"Variance: { variance_}")

# %%

age_series = pd.Series(age)
age_series

# %%

age_series.mean()

# %%

age_series.var()

# %%

age_series.median()

# %%

age_series.describe()

# %%




# %%
age_series = pd.Series(age, name='ages')
age_series

# %%

age[0]

# %%

age_series = age_series.sort_values()
age_series

# %%

#-- position in the series
age_series.iloc[0]

# %%

#-- index value
age_series.loc[0]

# %%

#-- index value
age_series[0]

# %%

age_series.shape

# %%

age_series.index = ["a", "b", "c",
                    'd', 'e', 'f',
                    'h', 'i', 'j',
                    'k', 'e']

age_series['e']

# %%
