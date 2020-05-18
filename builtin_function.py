name = input('Enter your name:')
greet = 'hello user'
if 'imtiaz' in name:
    used = greet.replace('user', 'Boss')
else:
    used = greet.replace('user', name)

print(used)