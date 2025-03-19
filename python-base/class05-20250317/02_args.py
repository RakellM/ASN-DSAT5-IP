# %%

def sum_basic(a: float, b: float, *args):
    return a + b + sum(args)

# %%

sum_basic(10, 20)

# %%

def sum_square(a: float, b: float, *args):
    a *= a
    b *= b
    return a + b


# %%

sum_square(1,2,3,4)


# %%

def sum_ages(a, b, *args):
    ages = [a, b]
    for i in args:
        ages.append(i["age"])
    
    return sum(ages)

sum_ages(20, 24, {"age": 23, "name": "Teo"} , {"age": 39, "name": "Raquel"})
# %%
#--Search for *kwargs, and present an example for next class.