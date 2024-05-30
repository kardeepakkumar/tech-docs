from collections import Counter
found = False
x = 0
while not found:
    x += 1
    nums = [str(x*i) for i in range(1, 7)]
    counts = Counter(nums[0])
    found = True
    for i in range(1, 6):
        if counts != Counter(nums[i]):
            found = False
            break
print(x)

# 142857