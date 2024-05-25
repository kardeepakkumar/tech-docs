F1 = 1
F2 = 1
idx = 2
while len(str(F2)) < 1000:
    F1 = F1 + F2
    F2 = F1 + F2
    F1 = F2 - F1
    F2 = F2 - F1
    idx += 1
print(idx)

# 4782