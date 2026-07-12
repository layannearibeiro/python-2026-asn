# %%

import pandas as pd
# %%

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df.head()

# %%

idades = [13,18,29,12,11,87,34,12,57]
nomes = ["Teo","Ana","Jose","Maria","Bela","joao","Paulo","Tiago","Denise" ]
is_menor_18 = []

for i in range(len(idades)):
    is_menor_18.append( idades[i] < 18)

print(is_menor_18)


# %%

nomes_nova = []
for i in range(len(idades)):
    if idades[i] < 18:
        nomes_nova.append(nomes[i])

print(nomes_nova)


# %%

idades_nova = []
for i in idades:
    if i < 18:
        idades_nova.append(i)

print(idades_nova)

# %%

# Quem tem youtube no Tmw?
filtro = df['flYouTube'] == 1
df[filtro]

# %%

filtro = df["qtdePontos"] > 10000
filtro


# %%

df[df["qtdePontos"] > 10000][df["flEmail"] == 1]


# %%
df_pontos_10000 = df[df["qtdePontos"] > 10000]
df_pontos_10000_email = df_pontos_10000[df["flEmail"] == 1]
df_pontos_10000_email

# %%

filtro = (df["qtdePontos"] > 10000) & (df["flTwitch"] == 1)
df[filtro].shape # condição E

# %%

filtro = (df["flEmail"] == 1) | (df["flYouTube"] == 1)
df[filtro].shape  # condição OU

# %%

df_produto = pd.read_csv("../../dados/produtos.csv", sep=";")
df_produto

# %%
df_produto["DescCategoriaProduto"].unique()

# %%

produtos_desejo = ['lovers', 'present', 'chat', 'fiel']
filtro_produto_desejo = df_produto["DescCategoriaProduto"].isin(produtos_desejo)
df_produto[filtro_produto_desejo]

# %%
produtos_desejo = ['lovers', 'present', 'chat', 'fiel']
df_produto[df_produto["DescCategoriaProduto"].isin(produtos_desejo)]

# %%

df_transacao = pd.read_csv("../../dados/transacoes.csv", sep=";")
df_transacao.head()