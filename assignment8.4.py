file = input('Enter a file name:')
fl = open(file)
words = list()
for line in fl:
    line = line.split()
    for i in range(len(line)-1):
        if line[i] not in words:
            words.append(line[i])
        else:
            continue
words.sort()
print(words)
