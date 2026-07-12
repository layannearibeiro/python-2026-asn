# %%

# Faça um programa que use uma função para responder a saudação de um usuário:
# “Olá, fulano! Boas vindas!”. Use funções para isso.

def saudacao(nome:str):
    text = f"Olá, {nome.title()}! Boas vindas!"
    print(text)
    

# %%

nome = input("Nome: ")
saudacao(nome)

