n = 600851475143
limit = int(n**(1/2) + 1)
primes = [True for i in range(0, limit+1)]
primes[0], primes[1], primes[2]= False, False, True
for i in range(2, limit+1):
    if primes[i]:
        k = 2*i
        while k < limit:
            primes[k] = False
            k += i
for i in range(len(primes)-1, 2, -1):
    if primes[i] and n % i == 0:
        result = i
        break
print(result)

# 6857