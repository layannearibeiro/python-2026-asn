# Faça um programa que receba 4 alturas usando
# um laço de repetição e realize a soma dessas alturas.

total = 0
for i in range(1,5):
    altura = input(f"Entre com a altura {i} em metros: ")
    total += float(altura)

print("Soma =", total)