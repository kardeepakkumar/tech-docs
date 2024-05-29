limit = 10**6
result = 0
for i in range(1, limit):
    m = 1
    counts = [1]+[0]*9
    pan = ""
    possible = True
    while sum(counts) < 10:
        num = i*m
        pan += str(num)
        for ch in str(num):
            counts[int(ch)] += 1
            if counts[int(ch)] > 1:
                possible = False
                break
        if possible and sum(counts) == 10:
            print(i)
            result = max(result, int(pan))
            break
        m += 1
        if not possible:
            break
print(result)

# 932718654