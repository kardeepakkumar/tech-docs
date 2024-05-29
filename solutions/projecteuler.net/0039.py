limit = 1001
result = -1
maxSol = 0
for p in range(1, limit):
    sol = 0
    for a in range(1, p):
        for b in range(a, p):
            c = p - a - b
            if c > 0 and c**2 == a**2 + b**2:
                sol += 1
    if sol > maxSol:
        result = p
        maxSol = sol
print(result)

# 840