# WHILE LOOP
flag = True
x = 0
check = int(input('Enter the max number you want to print : '))

print('Loop: Started\n')
while flag:
    print(x)
    x = x+1
    if(x > check):
        flag = False
        break
print('\nLoop: Ended')
