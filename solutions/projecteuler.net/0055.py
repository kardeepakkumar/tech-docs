result = 0
limit = 50
for n in range(1, 10**4):
    num = n
    for i in range(0, limit):
        num = num + int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            break
        elif i == limit - 1:
            result += 1
print(result)

# 249