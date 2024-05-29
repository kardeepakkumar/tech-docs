with open('0042_words.txt', 'r') as file:
    data = file.read()
data = data.split(",")
data = [name[1:len(name)-1] for name in data]

words = [sum([ord(w)-ord('A')+1 for w in word ]) for word in data]
# print(len(words))
result = 0
for w in words:
    r = ((1+8*w)**(1/2) - 1)/2
    if r > 0 and r == int(r):
        result += 1
print(result)

# 162