# %%

# while True:
#     print("Esse não para nunca!")

# %%

i = 1
while i <= 10000:
    print(i)
    i += 1  # i = i + 1

# %%

i = 1
while i <= 100:

    if i % 31 == 0 and i != 31:
        print("Achei esse caraio!!!", i)
    
    else:
        print(i)
    
    i += 1

# %%

i = 1
while i <= 100:

    if i % 31 == 0 and i != 31:
        print("Achei esse caraio!!!", i)
        break
    
    else:
        print(i)
    
    i += 1

# %%

i = 1
while i <= 100:

    if i % 31 == 0 and i != 31:
        print("Achei esse caraio!!!", i)
        i += 1
        continue

    print(i)
    i += 1