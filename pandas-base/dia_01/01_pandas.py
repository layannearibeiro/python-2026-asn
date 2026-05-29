# %%

import pandas as pd

# %%

idades = [27,30,35,42,28,50,35,36,36]
idades

# %%

media = sum(idades)/len(idades)

# %%

total = 0
for i in idades:
    total += (i - media) ** 2

variancia = total / (len(idades) - 1 )
variancia

# %%

idades_series = pd.Series(idades, name="idades")
idades_series
# %%

idades_series.mean()

# %%

idades_series.var()

# %%
idades_series.median()

# %%

idades_series.quantile(0.95)

# %%

idades_series.index

# %%

idades_series.shape[0]

# %%

idades_series.name
# %%

dados = {
    "idades": idades_series,
    "nomes": pd.Series(["A", "B", "C", "D", "Teo", "Bela", None, "Lara", "Nah"]),
}

for i in dados:
    print(dados[i])