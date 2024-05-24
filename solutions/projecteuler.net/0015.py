n = 20
arr1 = [1]*(n+1)
for i in range(1, n):
    arr2 = [sum(arr1[0:i]) for i in range(1, n+2)]
    arr1 = arr2
print(sum(arr1))

# 137846528820