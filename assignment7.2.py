file = input('Enter a file name: ')
try:
    fl = open(file)
except:
    print('Enter valid file name')
    quit()
total = 0
count = 0
for line in fl:
    if line.startswith('X-DSPAM-Confidence:'):
        target = line.find(':')
        num = line[target+1:]
        s_num = num.strip()
        new_num = float(s_num)
        total = total + new_num
        count = count + 1
    else:
        continue
avg = (total/count)
print('Average spam confidence:', avg)