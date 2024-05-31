limit = 1001
term = [3,2]
result = 0
for i in range(2, limit):
    term = [term[0] + 2*term[1], term[0] + term[1]]
    if len(str(term[0])) > len(str(term[1])):
        result += 1
print(result)

# 153