# %%

age = [32, 45, 32, 56, 21, 24, 26, 34, 27, 18, 19]

print(age)

# %%
# using WHILE to run on all values

index_ = 0

while index_ < len(age):
    print(f"Index {index_}: {age[index_]}")
    index_ += 1

# %%
# using FOR to run on all values

for i in age:
    print(i)

# %%
# using FOR to run on all indexes

for index_ in range(len(age)):
    print(f"Index {index_}: {age[index_]}")


# %%

data = {
    "first_name": 'Teo' ,
    "last_name": 'Calvo',
    "age": 32,
    "position": ['jr', 'pl', 'sr', 'head', 'pl'],
    "company": ['tapps', 'sas', 'via', 'gc', 'globo'],
    "salary": [3000, 4500, 7600, 12000, 4500],
}

for i in range(len(data['position'])):
    position = data['position'][i]
    company = data['company'][i]
    salary = data['salary'][i]

    print(f"Position: {position} | Company: {company} | Salary: R${salary:,.02f}")

# %%

for item in data.items():
    print(item)


# %%
# Unpacking
for (key, value) in data.items():
    print(key, "=> ", value)

# %% Tuple list

values = list(zip(data['position'], data['company'], data['salary']))

values

# %%

for i, j, k in values:
    print(f"Position: {i} | Company: {j} | Salary: R${k:,.02f}")

