longest = 0
for i in range(1, 1000000):
    n = i
    chain = 1
    while n > 1:
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        chain += 1
    longest = max(longest, chain)
    if longest == chain:
        result = i
print(result)

# 837799