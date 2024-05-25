abundants = []

def spd(num):
    ans = 1
    for i in range(2, int((num)**(1/2)) + 1):
        if num % i == 0:
            ans += i
            if num // i != i:
                ans += num //i
    return ans

for i in range(12, 28124):
    if spd(i) > i:
        abundants.append(i)

result = 0

for num in range(1, 28184):
    l, r = 0, len(abundants) - 1
    possible = False
    while l <= r:
        if abundants[l] + abundants[r] == num:
            possible = True
            break
        elif abundants[l] + abundants[r] < num:
            l += 1
        else:
            r -= 1
    if not possible:
        result += num
print(result)

# 4179871