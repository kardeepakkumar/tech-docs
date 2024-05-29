def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
    
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

primes = [2,3,5,7,11,13,17]
n = 10
result = 0
fn = factorial(n)
for i in range(1, fn+1):
    if i % (fn//100) == 0:
        print(i//(fn//100))
    p = permutation([k for k in range(n)], i)
    spd = True
    for j in range(1, n-2):
        num = p[j]*100 + p[j+1]*10 + p[j+2]
        if num % primes[j-1] != 0:
            spd = False
            break
    if spd:
        result += int("".join(str(item) for item in p))
print(result)

# 16695334890