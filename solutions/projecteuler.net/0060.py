def isPrime(num):
    l, r = 0, len(primes)-1
    while l <=r:
        m = (l+r)//2
        if primes[m] == num:
            return True
        elif primes[m] < num:
            l = m+1
        else:
            r = m-1
    return False

def findValidSet(indices, depth, currentDepth):
    if currentDepth < depth:
        for i in range(indices[-1] + 1, len(primes)):
            if currentDepth < 1 and i%(len(primes)//100) == 0:
                print(100*i//len(primes))
            p2 = primes[i]
            valid = True
            big = False
            for j in range(1, len(indices)):
                p1 = primes[indices[j]]
                if int(str(p1)+str(p2)) > primes[-1] or int(str(p2)+str(p1)) > primes[-1]:
                    big = True
                    break
                if not isPrime(int(str(p1)+str(p2))) or not isPrime(int(str(p2)+str(p1))):
                    valid = False
                    break
            if big:
                break
            if valid:
                indices.append(i)
                findValidSet(indices, depth, currentDepth+1)
                if len(indices) == target+1:
                    print([primes[idx] for idx in indices[1:]])
                    result.append([primes[idx] for idx in indices[1:]])
                indices.pop(-1)

primes = []
limit = 10**3
nums = [True for i in range(limit)]
for i in range(2, limit):
    if nums[i]:
        primes.append(i)
        j = 2*i
        while j < limit:
            nums[j] = False
            j += i
result = []#float("infinity")
target = 1
findValidSet([-1], target, 0)
print(result)

arr = [13, 5197, 5701, 6733, 8389]
print(sum(arr))

# 26033