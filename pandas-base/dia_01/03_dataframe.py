# %%

import pandas as pd
# %%

dados = {
    "idades":  [27, 30, 35, 42, 28, 50, 35, 36, 36],
    "nome": ["Ana", "Barbara", "Cida", "Dona", "Teo", "Bela", None, "Lara", "Nah"],
}

dados

# %%

df = pd.DataFrame(dados)
df

# %%
df.describe()

# %%

df["idades"]
# %%

df.iloc[0]

# %%

sobrenome =  ["Silva", "Costa", "Brandao", "Paiva", "Silva", "Nobre", None, "Niau", "Santos"]
sobrenome

df["sobrenome"] = sobrenome
df

# %%

df["sobrenome"].describe()

# %%

stats = df["idades"].describe()
stats

# %%

stats['std']

# %%

stats