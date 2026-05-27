# Faça um programa que a pessoa entra com 3 notas e verificamos se
#  a média delas é suficiente para passar na prova. Nota de corte 6.

n1 = input("Entre com a nota 1: ")
n1 = float(n1)

n2 = input("Entre com a nota 2: ")
n2 = float(n2)

n3 = input("Entre com a nota 3: ")
n3 = float(n3)

media = (n1 + n2 + n3) / 3

print("MÉDIA FINAL:", media)

if media >= 6:
    print("Ha! Você passou! Parabéns!")

else:
    print("Vish! Vai ter que tentar novamente ano que vem. :( ")