result = 0
for a in range(1, 100):
    print(a)
    for b in range(1, 100):
        result = max(sum([int(ch) for ch in str(a**b)]), result)

print(result)

# 972