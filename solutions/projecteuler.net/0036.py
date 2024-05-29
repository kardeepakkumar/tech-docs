n = 10**6
result = 0
for i in range(1, n):
    b2 = ""
    num = i
    while num > 0:
        if num % 2 == 0:
            b2 = "0" + b2
        else:
            b2 = "1" + b2
        num //= 2
    if str(i) == str(i)[::-1] and b2 == b2[::-1]:
        result += i
print(result)

# 872187