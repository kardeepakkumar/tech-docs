result = 0
limit = 1001
for i in range(1, limit):
    result += i**i
    digs = len(str(result))
    if digs > 10:
        result = int(str(result)[digs-10:])
print(result)

# 9110846700