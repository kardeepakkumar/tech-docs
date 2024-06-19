from collections import Counter
limit = 10001
cubes = ["".join(sorted(list(str(i**3)))) for i in range(limit)]
counts = Counter(cubes)
val = counts.most_common(1)[0][0]
print(val)
for i in range(1, limit):
    if "".join(sorted(list(str(i**3)))) == val:
        print(i**3)
        break 

# 127035954683