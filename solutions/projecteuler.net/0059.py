with open('0059_cipher.txt', 'r') as file:
    data = file.read()
data = data.split(",")

base = ord('a')
words = ["which", "the", "a"]
for a in range(base, base+26):
    for b in range(base, base+26):
        for c in range(base, base+26):
            key = [a,b,c]
            msg = [int(data[i])^key[i%3] for i in range(0, len(data))]
            decoded = ""
            for m in msg:
                decoded += chr(m)
            valid = True
            for word in words:
                if word not in decoded:
                    valid = False
            if valid:
                print(sum(msg))

# 129448