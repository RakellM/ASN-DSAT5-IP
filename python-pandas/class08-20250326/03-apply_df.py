# %%

import pandas as pd

clients = pd.read_csv("../data/clientes.csv")
clients.head()

# %%

# I want to attribute 100 points for users who have Twitch and Email

x = clients.iloc[0]
x

def plus_100_t_yt(x):
    # using IF
    if x['flTwitch'] == 1 and x['flYouTube'] == 1:
        return x['qtdePontos'] + 100
    else:
        return x['qtdePontos'] 
    
    # multiplying columns (better option)
    # return x['flTwitch'] * x['flYouTube'] * 100 + x['qtdePontos'] 
    
clients.apply(plus_100_t_yt, axis=1)

# %%

clients['flTwitch'] * clients['flYouTube'] * 100 + clients['qtdePontos'] 

# %%

# IF ternário
clients.apply(lambda row: "engaged" if row["flTwitch"] == 1 and row["flYouTube"] == 1 else "not engaged", axis=1)

# %%

nbr = 100

# method 1: we can do a IF like that
# value = ""
# if nbr > 100:
#     value = "a lot"
# else:
#     value = "less"

# method 2: IF ternário (it does not exist a ELIF in a situation like this)
value = "a lot" if nbr > 100 else "less"
value

# %%
