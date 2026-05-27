# %%

def f(x):
    return x ** 2

def r_none():
    print("Essa funcao nao retorna nada")


# %%
print("f(2) =", f(2))
print("f(10) =", f(10))
print("f(25) =", f(25))

# %%

print("r_none() =", r_none())

# %%

def soma(a, b=0, c=0):
    """
    funçao soma(a, b=0, c=0)

    recebe 3 inteiros ou floats e realiza sua soma
    - a (orbrigatório)
    - b (opcional. default=0)
    - c (opcional. default=0)
    """
    
    res = a + b + c
    return res

# %%

res = soma(-10, c=100)
print(res)

res = soma(-10, c=500)
print(res)


# %%

# f(x) = x **2 + 2

# f(0) = 2
# f(1) = 3
# f(2) = 6

# f(x, y) = x **2 + 2 + y **2
# f(0, 0) = 2
# f(1, 0) = 3
# f(1, 1) = 4

# %%
