def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
    
n = 1000000
result = []
nums = [0,1,2,3,4,5,6,7,8,9]

for place in range(0, 10):
    i = 0
    while n > (i+1)*factorial(9-place):
        i += 1
    n -= i*factorial(9-place)
    result.append(nums[i])
    nums.pop(i)
result = int("".join([str(num) for num in result]))
print(result)

# 2783915460