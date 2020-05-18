name = 'Banana'
#for loop
print('!!!! for loop !!!!')
for letter in name:
    print(letter)
#while loop
print('!!!! while loop !!!!')
index = 0
while index < len(name):
    letter = name[index]
    print(letter)
    index = index + 1
#count of letters
count = 0
for letter in name:
    count += 1
print('Total letter in the name:', count)

#number of 'a' in the name
number = 0
for letter in name:
    if letter == 'a':
        number += 1
print('number of "a" is:', number)

