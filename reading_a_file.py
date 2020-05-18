file = open('welcome.txt')
count = 0
for line in file:
    print(line)
    count += 1
print(count)
