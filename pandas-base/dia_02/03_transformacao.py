# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df.head()

# %%

import matplotlib.pyplot as plt

# %%

plt.figure(dpi=400, figsize=[4,4])
plt.hist(df["qtdePontos"], density=True, bins=50)
plt.title( "Histograma das carteiras de pontos")
plt.grid()
plt.xlabel("Qtd. Pontos Carteira")
plt.savefig("chart.png")

# %%

df["log_qtdePontos"] = np.log(df["qtdePontos"]+1)
df.head()

plt.hist(df["log_qtdePontos"], bins=50, alpha=0.5)
plt.hist(df["qtdePontos"], bins=50, alpha=0.5)
plt.title( "Histograma das log(carteiras de pontos)")
plt.grid()
plt.xlabel("Qtd. Pontos Carteira (log)")
plt.show()

# %%

df["qtdePontos"].hist()
plt.title("fodase")