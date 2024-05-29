limit = 10**6
primes = []
nums = [True for i in range(0, limit)]
for i in range(2, limit):
    if nums[i]:
        primes.append(i)
        j = 2*i
        while j < limit:
            nums[j] = False
            j += i

result = 0
for p in primes:
    if p < 10:
        continue
    truncatable = True
    for i in range(0, len(str(p))):
        if int(str(p)[i:]) not in primes:
            truncatable = False
            break
        if int(str(p)[0:i+1]) not in primes:
            truncatable = False
            break
    if truncatable:
        result += p
        print(p)

print(result)

# 748317