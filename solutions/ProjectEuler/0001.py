result = 0
i = 1
end = 1000
while i < end:
    if i%3 == 0 or i%5 == 0:
        result += i
    i += 1
print(result)
# 233168