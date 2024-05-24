teens = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
result = 11

for i in range(1, 1000):
    if i % 100 < 20:
        result += teens[i%100]
    else:
        result += teens[i%10]
        result += tens[(i//10)%10]
    if i//100 > 0:
        result += teens[i//100]
        result += hundred
        if i % 100 > 0:
            result += 3
print(result)

# 21124