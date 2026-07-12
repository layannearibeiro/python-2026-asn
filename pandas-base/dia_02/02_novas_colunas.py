# %%

import pandas as pd

df = pd.read_csv("../../dados/transacoes.csv", sep=";")
df.head()

# %%
df["dtDateTime"] = pd.to_datetime(df["DtCriacao"])
df

# %% 
df.dtypes


# %%

df["dtDateTime"].dt.quarter
# %%
df[df["dtDateTime"].dt.normalize() == "2025-02-01"]

# %%
df["dtDateTime"].dt.day_name("pt")

# %%

pd.value_counts(df["dtDateTime"].dt.day_name("pt"))