limit = 1111
result = 0
for pow in range(1, limit):
    i = 1
    n = 1
    while len(str(n)) < pow + 1:
        if len(str(n)) == pow:
            result += 1
        i += 1
        n = i**pow
print(result)

# 49