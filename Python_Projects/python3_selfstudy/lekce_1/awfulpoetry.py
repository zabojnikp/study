#!/usr/bin/env python3
import random

zajmena = ['muj', 'tvuj', 'jeho', 'jeji']
podstatna_jmena = ['kocka', 'pes', 'muz', 'zena']
slovesa = ['zpiva', 'bezi', 'skace']
prislovce = ['hlasite', 'tise', 'kvalitne', 'hrozne']

while True:
    try:
        user_input = input("how many lines do you want to print from 1-10 including?")

        if not user_input:
            lines = 5
            break
        
        number = int(user_input)   
        if 1 <= number <= 10:
            lines = number
            break
            
        else:
            print('number is not in 1-10 interval')

    except ValueError as err:
        print(err)

while lines:
    if random.randint(0, 1) == 0:
        print(random.choice(zajmena), random.choice(podstatna_jmena), random.choice(prislovce), random.choice(slovesa))

    else:
        print(random.choice(zajmena), random.choice(podstatna_jmena), random.choice(slovesa))
    
    lines -= 1
