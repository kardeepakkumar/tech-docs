from bisect import bisect_left

def factorial(n) -> int:
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
    
def permutation(nums, rank) -> list[int]:
    n = len(nums)
    result = []
    for i in range(n-1, -1, -1):
        idx = 0
        for j in range(0, i+1):
            if rank > factorial(i):
                rank -= factorial(i)
                idx += 1
            else:
                result += [nums[idx]]
                nums.pop(idx)
                break
    return result

def nck(n, k):
    return int(factorial(n)/(factorial(k) * factorial(n-k)))

def combination(nums, k, rank):
    n = len(nums)
    result = [[],[]]
    for i in range(len(nums)):
        if rank <= nck(n-len(result[0])-len(result[1])-1, k-1-len(result[0])):
            result[0].append(nums[i])
            if len(result[0]) == k and i != len(nums)-1:
                result[1] = result[1] + nums[i+1:]
                break
        else:
            rank -= nck(n-len(result[0])-len(result[1])-1, k-1-len(result[0]))
            result[1].append(nums[i])
    return result

limit = 10**6
primes = []
familyGoal = 8
result = []
nums = [True for i in range(limit)]
for i in range(2, limit):
    if nums[i]:
        primes.append(i)
        j = 2*i
        while j < limit:
            nums[j] = False
            j += i

def isPrime(primes, n):
    idx = bisect_left(primes, n)
    return (idx < len(primes) and primes[idx] == n)

found = False
while primes:
    print(len(primes)//100)
    p = primes[0]
    n = len(str(p))
    for r in range(1, n):
        for c in range(1, nck(n, r) + 1):
            genPrimes = set()
            r_idx, o_idx = combination(nums=[i for i in range(n)], k=r, rank=c)
            for d in range(0, 10):
                currNum = ""
                while o_idx or r_idx:
                    if o_idx and r_idx and o_idx[0] < r_idx[0]:
                        currNum += str(p)[o_idx[0]]
                        o_idx.pop(0)
                    elif o_idx and r_idx:
                        currNum += str(d)
                        r_idx.pop(0)
                    elif o_idx:
                        currNum += str(p)[o_idx[0]]
                        o_idx.pop(0)
                    else:
                        currNum += str(d)
                        r_idx.pop(0)
                r_idx, o_idx = combination(nums=[i for i in range(n)], k=r, rank=c)
                while len(currNum) > 1 and currNum[0] == '0':
                    currNum = currNum[1:]
                currNum = int(currNum)
                if isPrime(primes, currNum):
                    genPrimes.add(currNum)
            
            if len(genPrimes) == familyGoal:
                print(genPrimes)
                found = True
                break
        if found:
            break
    primes.pop(0)
    if found:
        break

# 121313