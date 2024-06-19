def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

diags = [1]
limit = 100001
side = 1
threshold = 0.1
primesCount = 0
for i in range(limit):
    for j in range(4):
        diags.append(diags[-1] + 2*i + 2)
        primesCount += isPrime(diags[-1])
    side += 2
    if primesCount/len(diags) < threshold:
        print(side)
        break

# 26241