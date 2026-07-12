# %%

import pandas as pd

df = pd.read_csv("../../dados/produtos.csv", sep=";")
df

# %%

valores = []

for i in df["DescCategoriaProduto"]:
    valores.append(i.upper())

df["DescCategoriaProdutoUpper"] = valores
df

# %%

def to_upper(x:str, fodase):
    return x.upper()

df["DescCategoriaProduto"].apply(lambda x: to_upper(x, 0) )

# apply nas linhas de uma coluna

# %%

print(to_upper(df["DescCategoriaProduto"].iloc[0]))
print(to_upper(df["DescCategoriaProduto"].iloc[1]))
print(to_upper(df["DescCategoriaProduto"].iloc[2]))
print(to_upper(df["DescCategoriaProduto"].iloc[3]))
print(to_upper(df["DescCategoriaProduto"].iloc[4]))
print(to_upper(df["DescCategoriaProduto"].iloc[5]))

# %%

df["DescCategoriaProduto"].apply(lambda x: x.upper())
