# %%

import pandas as pd

clients = pd.read_csv("../data/clientes.csv")
clients.head()

# %%

#--type object
clients['dtAtualizacao']   

# %%

#--type str
type(clients['dtAtualizacao'][3])  

# %%

#-- now it is datetime64[ns]
pd.to_datetime(clients['dtAtualizacao'])   

# %%

#-- convert the dataframe column to datetime64[ns]
clients['dtAtualizacao'] = pd.to_datetime(clients['dtAtualizacao'])   

# %%

#-- get the data from the datetime column
clients['dtAtualizacao'].dt.date

# %%

#-- the type of the column is now datetime64[ns] in a tuple
clients['dtAtualizacao'].dt.date[3]

# %%

#-- this will not work, because the type is datetime64[ns] and not str
clients['dtAtualizacao'].dt.date == '2025-02-19' 

# %%

#-- convert the datetime64[ns] to str
clients['dtAtualizacao'].dt.date.astype(str) == '2025-02-19' 

# %%

clients['dtAtualizacao'].dt.date.astype(str)[3]

# %%

#-- convert the dataframe column from datetime64[ns] to str
clients['dtAtualizacao'] = clients['dtAtualizacao'].astype(str)

# %%

(clients['qtdePontos'] * 0.5)

# %%

#-- convert float to int
(clients['qtdePontos'] * 0.5).astype(int)

# %%

#-- it is possible to convert into boolean
(clients['qtdePontos'] * 0.5).astype(bool)

# %%

(clients['qtdePontos'] * 0.5).astype(bool).astype(str)

# %%
