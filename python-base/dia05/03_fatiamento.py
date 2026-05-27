# %%

x = [1,2,3,4,5,6,10,20,30,40,50]

# %%

x[0 : 3] # x[start:stop] onde stop não é incluído

# %%

x[0:-2]

# %%

x[-3: ]

# %%

x[::-1]

# %%
# [1,2,3,4,5,6,10,20,30,40,50]
x[::2]

# x[ start : stop : step ]

# %%

x[0:3][::-1]

# %%

minha_lista = list(range(1,101))
minha_lista[1::2]


# %%

nome = "Victor Delabio Ferraz de Almeida Meira"
nome[:3]

# %%

nome_lista = nome.split(" ")
nome_lista = nome_lista[:2]
nome_2 = " ".join(nome_lista)
nome_2

# %%

palavra = "Osso"
palavra == palavra[::-1]
