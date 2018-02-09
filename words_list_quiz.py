with open("data/words_alpha.txt", 'r') as f:
    words = f.read().splitlines()

print(words[:10])

print(len(words))

count = 0
for w in words:
    if len(w) == 5:
        count += 1
print(count)

count = 0
for w in words:
    if len(w) > 7:
        count += 1
print(count)

chars = 0
for w in words:
    chars += len(w)
print(chars)

count = 0
for w in words:
    if "e" not in w:
        count += 1
print(count)

count = 0
for w in words:
    if w[0] == w[-1]:
        count += 1
print(count)

count = 0
aez = 0
for w in words:
    for i in range(len(w)):
        if w[i] == "a":
            aez += 1
            if aez == 3:
                count += 1
print(count)

count = 0
quuz = False
for w in words:
    for i in range(len(w)-1):
        if w[i] == 'q' and w[i+1] != 'u':
            quuz = True
    if quuz == True:
        count += 1
    elif w[-1] == 'q':
        count += 1
print(count)
