def d(num):
    digits = 1
    while num > (10**(digits-1))*9*digits:
        num -= (10**(digits-1))*9*digits
        digits += 1
    rank = (num-1)//digits
    place = (num-1)%digits
    result = int(str(10**(digits-1) + rank)[place])
    return result

print(d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))

# 210