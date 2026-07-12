# %%

import pandas as pd

# %%

# Leia o arquivo transacoes.csv com a formatação correta;
# Adicione uma coluna com valores 1;
# Salve o dataframe com nome: transacoes_1.csv


df = pd.read_csv("../../dados/transacoes.csv", sep=";")
df

# %%

df["valores"] = "1"
df

# %%

df.to_csv("../../dados/transacoes_1.csv", sep=";")