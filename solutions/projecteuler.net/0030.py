limit = 10000000
result = 0
for num in range(2, limit):
    if num == sum([(int(ch))**5 for ch in str(num)]):
        result += num
print(result)

# 443839