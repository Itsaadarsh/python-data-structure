# FOR LOOPS

check = input('Enter ODD or EVEN : ')
x = int(input('Enter the max number of even numbers you want to print : '))

if(check.lower() == 'odd'):
    for i in range(0, x, 3):  # START , STOP , STEP
        print(i)
else:
    for i in range(0, x, 2):  # START , STOP , STEP
        print(i)
