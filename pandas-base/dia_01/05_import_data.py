# %%

import pandas as pd
import gc

# %%

df = pd.read_csv("../../dados/transacoes.csv", sep=";", )
df

# %%

df.shape

# %%

df.info(memory_usage="deep")

# %%

df.dtypes["QtdePontos"]

# %%

df["QtdePontos"].dtypes

# %%

columns = ['IdTransacao', 'DtCriacao', 'QtdePontos']
df[columns]

# %%

df.iloc[10:20]

# %%

nomes_novos = {
    "IdTransacao": "TransactionID",
    "IdCliente": "CustomerID",
    "DtCriacao": "CreatedAt",
    "QtdePontos": "PointsQtty",
    "DescSistemaOrigem": "OriginSystemName"
}

df_new = df.rename(columns=nomes_novos)
df_new

# %%

ordem_colunas = [
    'CustomerID',
    'TransactionID',
    'CreatedAt',
    'PointsQtty',
    'OriginSystemName',
]

df_new = df_new[ordem_colunas]
df_new

# %%

df_new["Origem"] = df_new["OriginSystemName"].copy()
df_new = df_new.rename(columns={"Origem":"OriginSystemName"})
df_new

# %%

df["fodase"] = "fodase"
df
# %%

import sys

# %%

