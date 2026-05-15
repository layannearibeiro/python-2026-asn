# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: MORANGO, creme, chocolate
# Cobertura: Caramelo (R$1,50), MORANGO (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00).
# Apresente o valor a ser pago

# obter o tipo de sorvete
tipo_sorvete = input("Entre com um tipo de sorvete [1]CASQUINHA (R$1,00), [2]CASCÃO (R$2,50), [3]CESTINHA (R$4,00): ")

if tipo_sorvete == "1":
    valor_sorvete = 1.00

elif tipo_sorvete == "2":
    valor_sorvete = 2.50

elif tipo_sorvete == "3":
    valor_sorvete = 4.00

else:
    valor_sorvete = 0

# Obtendo o sabor
sabor = input("Escolha o sabor do sorvete: [MORANGO / CREME / CHOCOLATE]: ")

# Obter a cobertura
cobertura = input("Escolha a cobertura: [1]CARAMELO (R$1,50), [2]MORANGO (R$1,50), [3]CHOCOLATE (R$1,50), [4]SEM COBERTURA (R$0,00)")

if cobertura in "1 2 3":
    valor_cobertura = 1.5
else:
    valor_cobertura = 0

valor_total = valor_sorvete + valor_cobertura
print(f"Seu sorverte custou: R${valor_total}")
