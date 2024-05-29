def binSearch(nums, n):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == n:
            return True
        elif nums[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return False

limit = 5000
p = [(i+1)*(3*(i+1)-1)/2 for i in range(limit)]
result = 10**10
for j in range(0, limit):
    for k in range(j+1, limit):
        if ((binSearch(p, p[k]+p[j])) and binSearch(p,p[k]-p[j]) and (result > p[k] - p[j])):
            result = p[k] - p[j]
        if k + 1 < limit and p[k+1] - p[k] > p[j]:
            break
print(result)

# 5482660