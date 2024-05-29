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

def nck(n, k):
    return int(factorial(n)/(factorial(k) * factorial(n-k)))

def combination(nums, k1, k):
    n = len(nums)
    result = [[],[]]
    for i in range(len(nums)):
        if k <= nck(n-len(result[0])-len(result[1])-1, k1-1-len(result[0])):
            result[0].append(nums[i])
            if len(result[0]) == k1 and i != len(nums)-1:
                result[1] = result[1] + nums[i+1:]
                break
        else:
            k -= nck(n-len(result[0])-len(result[1])-1, k1-1-len(result[0]))
            result[1].append(nums[i])
    return result

nums = [1,2,3,4,5,6,7,8,9]
n = len(nums)
result = 0

for k1 in range(2, 8):
    for k in range(1, nck(n, k1) + 1):
        c = combination(nums.copy(), k1, k)
        for i in range(1, factorial(len(c[1]))+1):
            p = int("".join([str(item) for item in permutation(c[1].copy(), i)]))
            found = False
            for k11 in range(1, k1):
                for k2 in range(1, nck(k1, k11)):
                    c2 = combination(c[0].copy(), k11, k2)
                    for j1 in range(1, factorial(len(c2[0]))+1):
                        n1 = int("".join([str(item) for item in permutation(c2[0].copy(), j1)]))
                        for j2 in range(1, factorial(len(c2[1])) + 1):
                            n2 = int("".join([str(item) for item in permutation(c2[1].copy(), j2)]))
                            if n1*n2 == p:
                                result += p
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
print(result)

# 45228