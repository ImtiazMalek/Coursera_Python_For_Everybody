file = open('randomtxt.txt')
count = dict()
for line in file:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0)+1
bigword = None
bignumber = None

for k, v in count.items():
    if bignumber is None or v > bignumber:
        bignumber = v
        bigword = k
print(bigword, bignumber)