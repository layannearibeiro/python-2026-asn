# Faça um programa que informe se uma número é par ou ímpar com uma função que se chama “EhPar”, retornando um booleano.

# %%

def eh_par(numero:int):
    return numero % 2 == 0


for i in range(1, 100):
    
    if eh_par(i):
        print(f"{i} é par")

    else:
        print(f"{i} é ímpar")