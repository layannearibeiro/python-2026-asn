# %%

minha_lista = [
    "Téo",
    "Calvo",
    33,
    1.82,
    1_678.98,
    "Nah",
    "ASN.Rocks",
]

print(minha_lista)


# %%

minha_lista[2]

# %%

len(minha_lista)

# %%

minha_lista[-1]

# %%

minha_lista[-len(minha_lista)]

# início ->           0 / fim -> len(lista)-1
# início -> -len(lista) / -1

# %%

minha_lista.append("Maria")

# %%

minha_lista.remove("Maria")

# %%

minha_lista.remove("Teodoro")

# %%

minha_lista

# %%
minha_lista.extend(["Professor", "Streamer"])
minha_lista

# %%

ex = ["Ana", "Maria", "Josefa", "Petúnia"]
minha_lista.append(ex)
# minha_lista.append(["Ana", "Maria", "Josefa", "Petúnia"])
minha_lista

# %%

minha_lista[-1][-1]

# %%

ex = minha_lista.pop(-1)

# %%

minha_lista

# %%

ex.append("Talita")

# %%
ex

# %%

minha_lista

# %%

A = [1,2,3]
# ---
B = A

print("A =", A, "/ ID:", id(A))
print("B =", B, "/ ID:", id(B))

print("A == B ->", A == B)
print("A is B ->", A is B)

# %%

id(A) == id(B)

# %%

A.append("fodase")

print("A =", A)
print("B =", B)

# %%

nome = "Téo"
nome_2 = nome

print(nome)
print(nome_2)

nome = nome.upper()
print(nome)
print(nome_2)

# %%

print(id(nome))
print(id(nome_2))

# %%

teo = ["Teodoro", 33, 1.82, 1500, "Nah"]

ex = [ ["Ana", 31], ["Raquel", 36], ["Laura", 30], ["Marcela", None]]

teo.append(ex)

teo

# %%

teo[-1][1][-1]

# %%

numeros = [1, 2.12, 3, 4.32, 5, -6, 7, 8, 9, 10]

# %%
sum(numeros)

# %%
min(numeros)

# %%
max(numeros)


# %%

x = [1,2,3,4]

retorno_1 = x.append(5)
# %%

retorno_2 = print("Ola mundo")
print(retorno_2)

# %%

print(retorno_1 is None)
print(retorno_2 is None)
print(retorno_2 is retorno_1)
