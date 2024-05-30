from collections import defaultdict
from bisect import bisect_left
from collections import Counter

cards = [str(i) for i in range(2, 10)] + ['T','J','Q','K','A']
values = defaultdict(int)
for i in range(0, len(cards)):
    values[cards[i]] = i

def evaluate(hand, type) -> int:
    if type == 0:
        expected = [7,8,9,10,11,12]
        for c in hand:
            if values[c[0]] not in expected:
                return -1
            expected.pop(bisect_left(expected, values[c[0]]))
        suit = hand[0][1]
        for c in hand:
            if c[1] != suit:
                return -1
        return 12
    if type == 1:
        v = []
        for c in hand:
            v.append(values[c[0]])
        v.sort()
        if len(v) != len(set(v)) or v[-1] - v[0] != 4:
            return -1
        suit = hand[0][1]
        for c in hand:
            if c[1] != suit:
                return -1
        return max(v)
    if type == 2:
        counts = Counter([values[c[0]] for c in hand])
        if counts.most_common(1)[0][1] != 4:
            return -1
        return int(counts.most_common(1)[0][0])
    if type == 3:
        counts = Counter([values[c[0]] for c in hand])
        if counts.most_common(1)[0][1] != 3 or counts.most_common(2)[1][1] != 2:
            return -1
        return int(counts.most_common(1)[0][0])
    if type == 4:
        suit = hand[0][1]
        for c in hand:
            if c[1] != suit:
                return -1
        return max([values[c[0]] for c in hand])
    if type == 5:
        v = []
        for c in hand:
            v.append(values[c[0]])
        v.sort()
        if len(v) != len(set(v)) or v[-1] - v[0] != 4:
            return -1
        return max(v)
    if type == 6:
        counts = Counter([values[c[0]] for c in hand])
        if counts.most_common(1)[0][1] != 3:
            return -1
        return int(counts.most_common(1)[0][0])
    if type == 7:
        counts = Counter([values[c[0]] for c in hand])
        if counts.most_common(1)[0][1] != 2 or counts.most_common(2)[1][1] != 2:
            return -1
        return int(counts.most_common(1)[0][0])
    if type == 8:
        counts = Counter([values[c[0]] for c in hand])
        if counts.most_common(1)[0][1] != 2:
            return -1
        return int(counts.most_common(1)[0][0])        

def rank(hand):
    for t in range(0, 9):
        if evaluate(hand, t) != -1:
            return t*100 + (12-evaluate(hand,t))
    return 900

with open('0054_poker.txt', 'r') as file:
    data = file.read()
data = data.split("\n")
data = data[:-1]

result = 0
for turn in data:
    hand1 = turn.split(" ")[:5]
    hand2 = turn.split(" ")[5:]
    rank1 = rank(hand1)
    rank2 = rank(hand2)
    if rank1 < rank2:
        result += 1
    elif rank1 == rank2:
        hand1 = sorted([values[c[0]] for c in hand1])
        hand2 = sorted([values[c[0]] for c in hand2])
        while hand2[-1] == hand1[-1]:
            hand2.pop(-1)
            hand1.pop(-1)
        if hand1[-1] > hand2[-1]:
            result += 1
print(result)
# 376