n = 2000000
primes = [True for i in range(0, n)]
primes[0], primes[1] = False, False

for i in range(2, n):
    if primes[i]:
        for j in range(2*i, n, i):
            primes[j] = False

result = 0
for i in range(0, n):
    if primes[i]:
        result += i
print(result)

# 142913828922