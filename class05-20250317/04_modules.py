# %%
#--Do I have to keep writing a square root function every time I want to use it?
def sqrt_1(x):
    return x ** 0.5 

sqrt_1(4)

# %%

import math

# %%

math.sqrt(4)

# %%

math.e

# %%

math.pi

# %%

def normal(x, mu=0, sigma=1):
    result = ((1 / (sigma * math.sqrt(2 * math.pi)))) * (math.e ** ( (-1 / 2) * ((x - mu) / sigma) ** 2 ))
    return result

# %%

from math import sqrt, pi, e
from math import cos

# %%

import math # import the entire container to your house

from math import * # unload everything from the container to your house (regular practive in R)

# %%

#--give nicknames to libraries
import math as mh

# %%

import random

random.randint(1, 10)

# %%

import time

for i in range(10):
    print(i)
    time.sleep(1)


# %%
