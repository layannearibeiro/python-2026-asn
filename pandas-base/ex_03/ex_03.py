# 03.01 - Quantos clientes tem vínculo com a Twitch?
# 03.02 - Quantos clientes tem um saldo de pontos maior que 1000?
# 03.03 - Quantas transações ocorreram no dia 2025-02-01?


# %%

import pandas as pd

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df

# %%
## 03.01 - Quantos clientes tem vínculo com a Twitch?
df[df["flTwitch"] == 1].shape[0]
# %%
## 03.02 - Quantos clientes tem um saldo de pontos maior que 1000?

df[df["qtdePontos"] > 1000].shape[0]


# %%
df.dtypes

# %%
# 03.03 - Quantas transações ocorreram no dia 2025-02-01?

df = pd.read_csv("../../dados/transacoes.csv", sep=";")

filtro = (df["DtCriacao"] >= "2025-02-01") & (df["DtCriacao"] < "2025-02-02")
df[filtro].shape[0]


# %%
df[df["DtCriacao"].between("2025-02-01", "2025-02-02")].shape[0]