def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)
limit = 2000000
result = 0

for i in range(10, limit):
    if sum([factorial(int(n)) for n in str(i)]) == i:
        result += i
print(result)

# 40730