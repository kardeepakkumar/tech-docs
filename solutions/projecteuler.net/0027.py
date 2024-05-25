def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

result = 0
maxPrimes = 0
for b in range(1, 1001):
    for a in range(-b-1, 1000):
        primes = 0
        while isPrime(primes**2 + a*primes + b):
            primes += 1
        if primes > maxPrimes:
            maxPrimes = primes
            result = a*b
print(result)

# -59231