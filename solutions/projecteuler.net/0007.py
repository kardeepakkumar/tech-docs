primes = [2]
n = 10001
for i in range(3, 1000000):
    for p in primes:
        if i % p == 0:
            break
        if p == primes[-1]:
            primes.append(i)
    if len(primes) == n:
        break
print(primes[-1])

# 104743