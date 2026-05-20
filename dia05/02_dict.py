# %%

chave = "nao sei"

teo = {
    "nome":"Téo",
    "chave":"valor",
    "sobrenome":"Calvo",
    "idade":33,
    "conjuge":{"nome":"Nah"},
    "empregos": ["ASN", "Twitch", "YouTube"],
    "parcerias": ["Google", "Nvidia", "Nekt", "linkedin"],
    "ex": [ {"nome": "Ana", "idade":31}, {"nome":"Marcela", "idade": 36} ],
    0: [0,1,2,3],
    "a": 1,
    chave: "alguma coisa",
    1.50: "4.5",
}


mauro = {
    "nome":"Mauro",
    "chave":"valor",
    "sobrenome":"Silva",
    "idade":42,
    "conjuge":{"nome":"Maria"},
    "empregos": ["gov.br"],
    "parcerias": ["ASN"],
    "ex": [ ],
}

dados = [teo, mauro]
dados
# %%

teo["nome"] = "Teodoro"
teo

# %%

teo["empregos"].append("aZmina")
teo

# %%

teo.keys()

# %%

teo.values()

# %%

teo.items()

# %%

for i in teo:
    print("===================")
    print(f"Chave: {i}")
    print(f"Valor: {teo[i]}")

# %%

for k, v in teo.items():
    print("===================")
    print(f"Chave: {k}")
    print(f"Valor: {v}")

# %%

# deletando chave do dicionário
del teo[1.5]

# %%

teo