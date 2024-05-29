limit = 1000000
result = 0
primes = []
nums = [True for i in range(limit)]
for i in range(2, limit):
    if nums[i]:
        primes.append(i)
        j = 2*i
        while j < limit:
            nums[j] = False
            j += i
for j in range(len(primes)):
    p = primes[j]
    circular = True
    for i in range(0, len(str(p))):
        if int(str(p)[i:] + str(p)[0:i]) not in primes:
            circular = False
            break
    if circular:
        result += 1
print(result)

# 55