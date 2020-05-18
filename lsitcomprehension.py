l = dict()
while True:
    name = input('Enter name: ')
    money = input('Enter payment: ')
    while True:
        try:
            dollar = float(money)
            break
        except:
            print('Enter ammount of money.')
            quit()

    l[name] = dollar
    check = input('Continue?')
    if check == "":
        continue
    elif check == 'done':
        break
arr = sorted([(v,k) for k,v in l.items()], reverse=True)
print(arr)
