# Faça um programa que receba 4 notas,
# calcule a média,
# mínimo e 
# máximo dessas notas.
# %%

n1 = input("Entre com a primeira nota: ")
n2 = input("Entre com a segunda nota: ")
n3 = input("Entre com a terceira nota: ")
n4 = input("Entre com a quarta nota: ")

notas = [float(n1), float(n2), float(n3), float(n4)]

media = sum(notas) / len(notas)  # soma e divide pela quantidade
minimo = min(notas)
maximo = max(notas)

print("Média:", media)
print("Minimo:", minimo)
print("Maximo:", maximo)

# %%

notas = []
for i in range(1,5):
    nota = input(f"Entre com a nota {i}: ")
    notas.append(float(nota))

media = sum(notas) / len(notas)  # soma e divide pela quantidade
minimo = min(notas)
maximo = max(notas)

print("Média:", media)
print("Minimo:", minimo)
print("Maximo:", maximo)

# %%

# compreensao de listas

# numeros = [i for i in range(1,5)]
# quadrados = [i**2 for i in range(1,5)]

notas = [float(input(f"Entre com a nota {i}: ")) for i in range(1,5)]

media = sum(notas) / len(notas)  # soma e divide pela quantidade
minimo = min(notas)
maximo = max(notas)

print("Média:", media)
print("Minimo:", minimo)
print("Maximo:", maximo)

