# %%

# 0, 1 ,1 ,2 ,3 ,5...

def fib(i):

    if i == 1:
        return 0
    
    elif i == 2:
        return 1
    
    else:
        return fib(i-1) + fib(i-2)

# %%

fib(6)