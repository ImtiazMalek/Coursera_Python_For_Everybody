name = input("Enter file:")
if len(name) < 1 : name = "box.txt"
file = open(name)
hours = list()
hour_count = dict()
for line in file:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        words = line[5]
        words = words.split(':')
        hours.append(words[0])
for word in hours:
    hour_count[word] = hour_count.get(word, 0) + 1
new_hour_count = sorted(hour_count.items())
for k,v in new_hour_count:
    print(k,v)
