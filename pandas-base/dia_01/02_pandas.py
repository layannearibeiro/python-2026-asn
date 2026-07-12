# %%

import pandas as pd


# %%

idades = [27,30,35,42,28,50,35,36,36]
idades

# %%

idades_series = pd.Series(idades)
idades_series

# %%
idades_series[1] ==  idades[1]

# %%
idades.sort()

# %%

idades_series = idades_series.sort_values()
idades_series

# %%

# Isso é posiçao
idades[1]

# %%

# isso é índice
idades_series[1]

# %%

# isso é posiçao
idades_series.iloc[1]

# %%

idades_series.loc[1]