#!/usr/bin/env python3

numbers = []

while True:
    try:
        user_input = input("Enter number or click Enter to end program: ")
        if user_input:
            number = int(user_input)
            numbers.append(number)
        else:
            break

    except ValueError as err:
        print(err)

print("numbers: ", numbers)
print('count:', len(numbers), 'sum:', sum(numbers), 
      'minimum:', min(numbers), 'maximum:', max(numbers), 
      'average:', sum(numbers)/len(numbers))
