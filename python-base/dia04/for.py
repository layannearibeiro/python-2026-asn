# %%

nome = "Teodoro Calvo"

for letra in nome:
    print(letra)


for fodase in nome:
    print(fodase)

# %%

for i in range(1,101):

    print("==========================")
    print("Testando Mult 2...")    
    if i % 2 == 0:
        print("Par")
        continue

    print("Testando Mult 15...")
    if i % 15 == 0:
        break

    print(i)


print("Fim!")