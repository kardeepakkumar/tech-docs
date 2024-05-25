spds = [0, 0]
def d(num):
    spd = 1
    for i in range(2, int(num**(1/2) + 1)):
        if num % i == 0:
            spd += i
            if i*i != num:
                spd += num//i
    return spd

for i in range(2, 10001):
    spds.append(d(i))
result = 0
for i in range(1, 10001):
    if spds[i] < 10001 and spds[spds[i]] == i and spds[spds[i]] != spds[i]:
        result += i
print(result)

# 31626