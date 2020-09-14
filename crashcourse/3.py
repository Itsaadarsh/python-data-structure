# FOR and IF statements

personData = [{'gender': 'Male', 'age': 19}, {'gender': 'FEMALE', 'age': 2}]

for i in range(len(personData)):
    print('For Person', i+1)
    if(personData[i]['age'] >= 18):
        print('\nAge is', personData[i]['age'])
        if(personData[i]['gender'].lower() == 'male'):
            print('Gender is male\n')
        elif(personData[i]['gender'].lower() == 'female'):
            print('Gender is female')
    else:
        print('Age is less than 18')
