n = 1000

for a in range(1, 999):
    for b in range(a+1, 999):
        c = 1000 - a - b
        if c < 0:
            break
        if a**2 + min(b,c)**2 == max(b,c)**2:
            print(a*b*c)
            break

# 31875000