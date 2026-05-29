# %%

import pandas as pd

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df

# %%


df_top_5 = (df.sort_values(by="qtdePontos", ascending=False)
              .head(5)
              .reset_index(drop=True))

df_top_5

# %%

df_index = df.set_index("idCliente")
df_index.index

# %%

df_teo = pd.DataFrame(
    {
        "nome": ["Teo", "Nah", "Mah", "Le"],
        "sobrenome": ["Calvo", "Gironde", "Calvo", "Silva"],
        "idade": [33,33,4,18]
    }
)

df_teo.sort_values( by=["sobrenome", "idade"], ascending=[True, False] )

# %%
