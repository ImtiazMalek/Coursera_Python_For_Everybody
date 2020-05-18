name = input('Enter a file name:')
if len(name) < 1:
    name = "box.txt"
file = open(name)
diclink = dict()
links = list()
for line in file:
    if line.startswith('From '):
        sline = line.rstrip()
        newline = sline.split()
        links.append(newline[1])
for link in links:
    diclink[link] = diclink.get(link, 0) + 1
maxemail = None
maxnumber = None
for k, v in diclink.items():
    if maxnumber is None or v > maxnumber:
        maxemail = k
        maxnumber = v
    else:
        continue
print(maxemail, maxnumber)