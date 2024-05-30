def binSearch(nums, n):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == n:
            return True
        elif nums[m] < n:
            l = m + 1
        else:
            r = m-1
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
for i in range(9, limit, 2):
    if not binSearch(primes, i):
        for p in primes:
            if p > i:
                result = i
                print(result)
                break
            if ((i-p)/2)**(1/2) == int(((i-p)/2)**(1/2)):
                break

# 5777