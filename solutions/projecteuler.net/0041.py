def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)

def isPrime(num):
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

def permutation(nums, k):
    n = len(nums)
    if k > factorial(n):
        return []
    result = []
    for i in range(n-1, -1, -1):
        idx = 0
        for j in range(0, i+1):
            if k > factorial(i):
                k -= factorial(i)
                idx += 1
            else:
                result += [nums[idx]]
                nums.pop(idx)
                break
    return result

limit = 10
result = 0
for n in range(2, limit):
    print(n)
    nums = [n-i for i in range(0, n)]
    for j in range(1, factorial(n) + 1):
        p = int("".join([str(item) for item in permutation(nums.copy(), j)]))
        if isPrime(p):
            if result < p:
                result = p
                break
print(result)

# 7682413