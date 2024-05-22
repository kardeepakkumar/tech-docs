import collections

factors = collections.defaultdict(int)
primes = [2,3,5,7,11,13,17,19]

for i in range(1, 20):
    for p in primes:
        n = i
        count = 0
        while n > 0:
            if n%p == 0:
                count += 1
                n //= p
            else:
                break
        factors[p] = max(factors[p], count)
result = 1
for p in primes:
    result *= p**factors[p]
print(result)

# 232792560