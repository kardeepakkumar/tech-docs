def binSearch(nums, n):
    P = 78498
    l, r = 0, P-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == n:
            return True
        elif nums[m] < n:
            l = m + 1
        else:
            r = m - 1
    return False

limit = 10**6
primes = []
nums = [True for i in range(limit)]
for i in range(2, limit):
    if nums[i]:
        primes.append(i)
        j = 2*i
        while j < limit:
            nums[j] = False
            j += i
sums = [0]
for i in range(1, len(primes)+1):
    sums += [sums[-1]+primes[i-1]]
result = 0
P = len(primes)
for len in range(P, 0, -1):
    found = False
    for l in range(0, P-len+1):
        r = l + len
        if sums[r] - sums[l] > primes[-1]:
            break
        if binSearch(primes, sums[r] - sums[l]):
            print(sums[r] - sums[l])
            found = True
            break
    if found:
        break

# 997651