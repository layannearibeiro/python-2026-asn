# %%

import pandas as pd

# %%

# 02.01 - Quantas linhas há no arquivo clientes.csv ?
# 02.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
# 02.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
# 02.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
# 02.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

# 02.01 

df_clientes = pd.read_csv("../../dados/clientes.csv", sep=";")
df_clientes.shape[0]



# %% 

# 02.02
df_transacoes = pd.read_csv("../../dados/transacoes.csv", sep=";")
df_transacoes  

df_transacoes.dtypes

df_transacoes.dtypes.value_counts()

# %%
# 02.03
df_produtos = pd.read_csv("../../dados/produtos.csv", sep=";")
df_produtos.dtypes.value_counts()

# %%
# 02.04
df_clientes.iloc[4]["idCliente"]

# %% 
# 02.05 

df_clientes.iloc[9]["qtdePontos"]

# %%

df_clientes.head(10)