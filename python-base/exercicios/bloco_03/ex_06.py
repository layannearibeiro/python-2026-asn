# Faça um programa que verifique se o item que a pessoa escolheu para comprar
#  na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

item = input("Entre com o seu item: ").lower()

if item in "laranja":
    print("Você escolheu um produto da lista!")

elif item in "cerveja":
    print("Você escolheu um produto da lista!")

elif item in "miojo":
    print("Você escolheu um produto da lista!")

elif item in "carvão":
    print("Você escolheu um produto da lista!")

elif item in "picanha":
    print("Você escolheu um produto da lista!")

else:
    print("Tente mais uma vez!")

    
# if item in "laranja|cerveja|miojo|carvão|picanha":
#     print("Você escolheu um item da lista! Parabéns!")

# else:
#     print("Tente mais uma vez!")