result = []
for num in range(11, 99):
    if num % 10 != 0:
        for den in range(num+1, 99):
            if den % 10 != 0 and not(den % 11 == 0 and num % 11 == 0):
                n = str(num)
                d = str(den)
                if n[0] == d[0] and num/den == int(n[1])/int(d[1]):
                    result.append([num, den])
                if n[0] == d[1] and num/den == int(n[1])/int(d[0]):
                    result.append([num, den])
                if n[1] == d[0] and num/den == int(n[0])/int(d[1]):
                    result.append([num, den])
                if n[1] == d[1] and num/den == int(n[0])/int(d[0]):
                    result.append([num, den])
num = result[0][0]*result[1][0]*result[2][0]*result[3][0]
den = result[0][1]*result[1][1]*result[2][1]*result[3][1]

f = 2
while f < den:
    while num % f == 0 and den % f == 0:
        num //= f
        den //= f
    f += 1
print(den)

# 100