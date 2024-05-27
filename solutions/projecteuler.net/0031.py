coins = [1,2,5,10,20,50,100,200]
target = 200
result = 0
count = 1
for a in range(0,201):
    for b in range(0,(200-a*coins[0])//coins[1] + 1):
        for c in range(0,(200-a*coins[0]-b*coins[1])//coins[2] + 1):
            for d in range(0, (200-a*coins[0]-b*coins[1]-c*coins[2])//coins[3] + 1):
                for e in range(0, (200-a*coins[0]-b*coins[1]-c*coins[2]-d*coins[3])//coins[4] + 1):
                    for f in range(0, (200-a*coins[0]-b*coins[1]-c*coins[2]-d*coins[3]-e*coins[4])//coins[5] + 1):
                        for g in range(0, (200-a*coins[0]-b*coins[1]-c*coins[2]-d*coins[3]-e*coins[4]-f*coins[5])//coins[6] + 1):
                            for h in range(0,(200-a*coins[0]-b*coins[1]-c*coins[2]-d*coins[3]-e*coins[4]-f*coins[5]-g*coins[6])//coins[7] + 1):
                                count += 1
                                if a*coins[0] + b*coins[1] + c*coins[2] + d*coins[3] + e*coins[4] + f*coins[5] + g*coins[6] + h*coins[7] == target:
                                    result += 1
print(result)

# 73682