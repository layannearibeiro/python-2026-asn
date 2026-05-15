# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Entre com uma palavra: ")

contador = 0
for letra in palavra:
    if letra.lower() == "a":

        contador += 1

print(f"A palavra '{palavra}' tem {contador} a's")