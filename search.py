file_name = input('Enter file name: ')
full_name = file_name + '.txt'
try:
    file = open(full_name)
except:
    print(file_name, ', File-name is invalid.\ncheck the name again')
    quit()
for line in file:
    if line.startswith('my name'):
        line = line.rstrip()
        print(line)