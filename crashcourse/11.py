def func(x='Rebeca', age=17):  # Optional parameter (age=11)
    print('\nNAME =>', x)
    if(age >= 18):
        return('ELIGIBLE\n')
    else:
        return('NOT ELIGIBLE\n')


print(func('John', 20))
print(func('Aadarsh'))
print(func())
