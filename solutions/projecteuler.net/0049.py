from collections import Counter
def binSearch(nums, n):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == n:
            return True
        elif nums[m] < n:
            l = m + 1
        else:
            r = m - 1
    return False

limit = 10000
primes = []
nums = [True for i in range(limit)]
for i in range(2, limit):
    if nums[i]:
        primes.append(i)
        j = 2*i
        while j < limit:
            nums[j] = False
            j += i
result = []
for i in range(1000, 9999):
    if binSearch(primes, i):
        for d in range(1, (limit-i)//2):
            if binSearch(primes, i+d) and binSearch(primes, i+2*d) and Counter(str(i)) == Counter(str(i+d)) and Counter(str(i)) == Counter(str(i+2*d)):
                result.append([i,i+d,i+2*d])
print(result)

# 296962999629