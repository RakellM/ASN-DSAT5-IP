# %%

data = ['Teo',
        'Calvo',
        32,
        ['jr', 'pl', 'sr', 'head', 'pl'],
        ['tapps', 'sas', 'via', 'gc', 'globo'],
        [3000, 4500, 7600, 12000, 4500],
]

# %%
# What is this person's first and last name?
name_first = data[0]
name_last = data[1]

print(f"First Name: {name_first}\nLast Name: {name_last}")

# %%

# What was the first company he/she worked for?
company = data[4]
company_first = data[4][0]

print(f"First company they have worked for: {company_first}")

# %%

# What were the last two positions in the market (seniority)?
position = data[3]
position_last2 = data[3][-2:]

print(f"Last 2 positions in the market: {position_last2}")

# %%

# Show the jumps from 2 to 2 companies of this person.
print(f"Jumps from 2 to 2 companies: {data[4][::2]}")


# %%

# Show the salary from the last to the first
print(f"Salary from the last to the first: {data[5][::-1]}")