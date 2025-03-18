# %%
a = 10
b = 5

print(a)
print(b)

c = a
a = b
b = c

print(a)
print(b)

a,b = b, a+b

print(a)
print(b)

# %%

a, b, *c = 1, 2, 3, 4, 5, 6

print(a, b, c)
# %%

a, *c, b = 1, 2, 3, 4, 5, 6

print(a, b, c)

