text = input("Write a text:")

a = 0
u = 0
i = 0
e = 0
o = 0
for j in text:
    if j in "uU":
        u += 1
    elif j in "aA":
        a += 1
    elif j in "oO":
        o += 1
    elif j in "eE":
        e += 1
    elif j in "iI":
        i += 1



print(f"Aa:{a} Ii:{i} Oo:{o} Ee:{e} Uu:{u}")


