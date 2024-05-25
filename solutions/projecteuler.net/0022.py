with open('0022_names.txt', 'r') as file:
    data = file.read()
data = data.split(",")
data = [name[1:len(name)-1] for name in data]
data.sort()
result = 0
for i in range(0, len(data)):
    name = data[i]
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    score *= (i+1)
    result += score
print(result)

# 871198282