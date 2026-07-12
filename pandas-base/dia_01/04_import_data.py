# %%

import pandas as pd

import os
os.getcwd() #mostra onde o python está sendo executado

# %%

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df

# %%

df.shape #sempre linhas e depois colunas
# %%

df.describe() #mostra estatísticas do dataframe

# %%

linhas = df.shape[0]
colunas = df.shape[1]

print(f"O arquivo foi importado com {linhas} linhas e {colunas} colunas.")
# %%
df.head(10)

# %%
df.tail(15)

# %%

df_10 = df.head(10)
df_10

# %%

df_10.to_csv("../../dados/top_10_cliente.csv", sep="|", index=False)

# %%



lista = [30, 10, 20]

# %%

s = pd.Series(lista, name="valores")
s

# %%

resultado = s.sort_values()
resultado