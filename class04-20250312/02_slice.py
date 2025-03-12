# %%

teo = ["Teodoro", 32, "professor", 2500.45, ['ana', 'maria', 'clara']]
teo
# %%

teo[0:2]

# start = 0
# end = 2
# total = end - start = 2
# teo[start:stop] # open on the end part

# %%
# last item
teo[-1]

# %%
teo[-3:]

# %%
# start / stop / step

numbers = [1,2,3,4,5,6,7,8,9,10]

# if I want to invert the list, my step is -1
# list[stat:stop:step]
numbers[::-1]

# %%
# what if I want to get all odd numbers

numbers[::2]

# %%
numbers[1::2]