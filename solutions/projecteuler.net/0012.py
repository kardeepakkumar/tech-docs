i = 1
F = 2
while F < 500:
    F = 2
    t = int(i*(i+1)/2)
    for f in range(2, int(t**(1/2))):
        if t%f == 0:
            F += 2
    i += 1
result = t 
print(result)

# 76576500