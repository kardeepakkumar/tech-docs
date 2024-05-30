factorials = [1]
limit = 101
threshold = 10**6
for i in range(1, limit):
    factorials.append(i*factorials[-1])

def ncr(n,r) -> int:
    return factorials[n]/factorials[r]/factorials[n-r]

result = 0
for n in range(1, limit):
    for r in range(0, n+1):
        if ncr(n,r) > threshold:
            result += 1
print(result)

# 4075