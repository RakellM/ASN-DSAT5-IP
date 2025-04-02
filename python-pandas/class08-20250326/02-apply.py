# %%

# I want to check if the the input is a given a string value

input_ = input("Enter a string: ")

input_.lower().startswith("venda de item:")    #-- this works

# %%

import pandas as pd

products = pd.read_csv("../data/produtos.csv")
products.head()

# %%

filter_sell = []
for i in products["descProduto"]:
    filter_sell.append(i.lower().startswith("venda de item:"))

filter_sell

# %%

products[filter_sell]

# %%

def is_sell(product):
    return product.lower().startswith("venda de item:")

is_sell(input_)

# %%

filter_sell = []
for i in products["descProduto"]:
    filter_sell.append(is_sell(i))

filter_sell

# %%	

products[filter_sell]

# %%

# Using apply to filter the products
#-- understanding that we can call a function without invoking it

def sum_(a, b):
    return a + b

def sub_(a, b):
    return a - b

option = 'sum_'

#-- the way we learned so far
# if option == 'sum_':
#     result = sum_(1, 2)

# elif option == 'sub_':
#     result = sub_(1, 2)

#-- we can make it better by using a dictionary
functions = {
    'sum_': sum_,
    'sub_': sub_
}

functions[option](1, 2)

# %% 

#-- usinf the same logic to filter the products
#-- this will behave like a FOR and apply the function to each row
products["descProduto"].apply(is_sell)

# %%

# Anonymous function: lambda function
#-- this is a function that we can use without defining it first
#-- if the fuction is one line only, otherwise it is better to define a fuction
products["descProduto"].apply(lambda x: x.lower().startswith("venda de item:"))


# %%

# Not usual, but it can be done this way too
is_sell_lambda = lambda x: x.lower().startswith("venda de item:")

products["descProduto"].apply(is_sell_lambda)

# %%

# products["descProduto"]   #--this is series of type object

products["descProduto"].str.lower().str.startswith("venda de item:") 
#-- if there is a NA value, it will cause an error

# %%

# now look for items that have "bota" in the description
def is_bota(product:str):
    return product.lower().count(" bota") > 0

products["descProduto"].apply(is_bota)

# %%

# how can we use aplly in a dataframe?
