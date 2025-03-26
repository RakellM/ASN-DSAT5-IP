
# %%

import pandas as pd

# %%

df = pd.read_csv('../data/clientes.csv')

# %%

df.tail()

# %%

df.rename(columns={
    'qtdePontos': 'qtyPoints', 
    'idCliente': 'idUser', 
    }, inplace=True)

# %%

df.head(2)

# %%

#-- need to give all columns otherwiseit will complain
df.columns = [
    'idCustomer' ,
    'flEmail' ,
    'flTwitch', 
    'flYouTube',
    'flBlueSky'	,
    'flInstagram' ,
    'qtyPoints',
    'dtCreated'	,
    'dtUpdated'
]

df.head(2)

# %%

df.shape

# %%

df.info()

