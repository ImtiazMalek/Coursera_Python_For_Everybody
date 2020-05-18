#file = input('Enter a file name:')
fl = open('box.txt')
count = 0
for line in fl:
    newline = line.split()
    if len(newline) > 0 and newline[0] == 'From ':
        print(newline[1])
        count = count + 1
    else:
        print(len(newline))
        continue
print("There were", count, "lines in the file with From as the first word")