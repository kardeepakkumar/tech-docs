nums = set()
for a in range(2, 101):
    for b in range(2, 101):
        nums.add(a**b)
result = len(nums)
print(result)

# 9183