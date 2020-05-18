hi5 = dict()
hi5 = {'himel': 1, 'junaid': 10}
hi = list()
while True:
    name = input('Enter a name:')
    newname = name.rstrip()
    if newname == 'done':
        break
    else:
        hi.append(newname)
for i in hi:
    hi5[i] = hi5.get(i, 0)
print(hi5)