f = 1
n = 100
for i in range(1, n+1):
    f *= i
result = 0
for char in str(f):
    result += int(char)
print(result)

# 648