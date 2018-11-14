import random

zajmena = ['muj', 'tvuj', 'jeho', 'jeji']
podstatna_jmena = ['kocka', 'pes', 'muz', 'zena']
slovesa = ['zpiva', 'bezi', 'skace']
prislovce = ['hlasite', 'tise', 'kvalitne', 'hrozne']

lines = 0
while True:
    try:
        user_input = input('How many lines would you like to have from 1-10? ')
        if not user_input:
            lines = 5
            break

        elif 1 <= int(user_input) <= 10:
            lines = int(user_input)
            break
        
        else:
            print('Your number is not from interval')


    except ValueError as err:
        print(err)

while lines:
    if random.randint(0, 1) == 0:
        print(random.choice(zajmena), random.choice(podstatna_jmena), random.choice(prislovce), random.choice(slovesa))

    else:
        print(random.choice(zajmena), random.choice(podstatna_jmena), random.choice(slovesa))
    
    lines -= 1