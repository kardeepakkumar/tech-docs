def binSearch(nums, n):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == n:
            return True
        elif nums[m] < n:
            l = m+1
        else:
            r = m-1
    return False

limit = 3 * 10**9
T, P, H = [1], [1], [1]
result = []
for i in range(0,limit):
    if binSearch(P,T[i]) and binSearch(H, T[i]):
        result.append(T[i])
    T.append((i+2)*(i+3)/2)
    P.append((i+2)*(3*i+5)/2)
    H.append((i+2)*(2*i+3))
print(result)

# 1533776805