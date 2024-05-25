from decimal import Decimal, getcontext 

precision = 20000
getcontext().prec = precision

result = 0
lrc = 0
for num in range(2, 1000):
    val = str(Decimal('1') / Decimal(num))[2:-2]
    for start in range(0, min(len(val), precision//10)):
        found = False
        for i in range(1, precision//10):
            if val[start:start+i]*8 == val[start:start+8*i]:
                found = True
                if lrc < i:
                    lrc = i
                    result = num
                break
        if found:
            break
        if start == precision//10 -1:
            lrc = 99999999

print(result)

# 983