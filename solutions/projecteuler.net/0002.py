n_2 = 1
n_1 = 1
n = n_1 + n_2
result = 0
while n < 4000000:
    if n%2==0: result += n
    temp = n_1 + n
    n_1 = n
    n = temp
print (result)

# 4613732