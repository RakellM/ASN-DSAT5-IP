
# %%

list_ = [1,2,3,4,5]
list_01 = [1]

tuple_ = (1,2,3,4,5)
tuple_01 = (1,)

dictionary_ = {"nome": "teo", "idade": 32}
# %%

import pandas as pd

s = pd.Series(list_)
s

# %%
teo = pd.Series(dictionary_)
teo
# %%
