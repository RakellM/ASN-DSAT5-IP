# %%

data = {
    "first_name": 'Teo' ,
    "last_name": 'Calvo',
    "age": 32,
    "position": ['jr', 'pl', 'sr', 'head', 'pl'],
    "company": ['tapps', 'sas', 'via', 'gc', 'globo'],
    "salary": [3000, 4500, 7600, 12000, 4500],
}

data

# %%
data['first_name']

# %%
# link: https://viacep.com.br/ws/19061070/json/
# change CEP on the link

address = {
    "cep": "20755-063",
    "logradouro": "Rua Mário Carpenter",
    "complemento": "até 718 - lado par",
    "unidade": "",
    "bairro": "Pilares",
    "localidade": "Rio de Janeiro",
    "uf": "RJ",
    "estado": "Rio de Janeiro",
    "regiao": "Sudeste",
    "ibge": "3304557",
    "gia": "",
    "ddd": "21",
    "siafi": "6001"
}

# %%

address.keys()

# %%

address.values()

# %%

address.items()

# return a list of double values, since a dictionary is a combination of key and value. "tuplas"




