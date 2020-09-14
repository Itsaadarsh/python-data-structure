# TRY AND EXCEPT

inp = input('Username : ')

try:
    num = int(inp)
    print('VALID', num)
except:
    print('Invalid! Try again')
