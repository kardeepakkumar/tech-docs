dom = [31,0,31,30,31,30,31,31,30,31,30,31]
def isLeap(y):
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        return True
    else:
        return False
def nextDate(date):
    y = date[0]
    m = date[1]
    d = date[2]
    if m == 2:
        if isLeap(y):
            M = 29
        else:
            M = 28
    else:
        M = dom[m-1]
    if d == M:
        d = 1
        if m == 12:
            m = 1
            y += 1
        else:
            m += 1
    else:
        d += 1
    return ([y, m, d])

result = 0
date = [1901,1,1]
day = 2
while date[0] < 2001:
    if day == 0 and date[2] == 1:
        result += 1
    date = nextDate(date)
    day = (day + 1)%7
print(result)