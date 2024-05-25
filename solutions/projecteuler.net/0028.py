result = 1
side = 1
d = 2
term = 1
while side < 1001:
    for i in range(4):
        term += d
        result += term
    side += 2
    d += 2
print(result)

# 669171001