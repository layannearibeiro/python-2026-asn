# %%

def media(x:list=[]):
    total = sum(x)

    if len(x) == 0:
        return 0
    
    res = total / len(x)
    return res

# %%

media([1,2])

# %%

media([1,2,3,4,5])

# %%
