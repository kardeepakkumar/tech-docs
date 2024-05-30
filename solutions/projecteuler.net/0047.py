def dpf(primes, num):
    result = 0
    for p in primes:
        if num % p == 0:
            result += 1
            while num % p == 0:
                num //= p
            if num == 1:
                break
    return result


limit = 1000000
primes = []
cons = 4
nums = [True for i in range(limit)]
for i in range(2, limit):
    if nums[i]:
        primes.append(i)
        j = 2*i
        while j < limit:
            nums[j] = False
            j += i

for i in range(1, limit-cons+1):
    if i % (limit//100) == 0:
        print(100*i//limit)
    possible = True
    for k in range(i, i+cons):
        if dpf(primes, k) != cons:
            possible = False
            break
    if possible:
        print(i)
        break
# 134043