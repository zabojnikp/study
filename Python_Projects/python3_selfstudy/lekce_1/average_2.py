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

#sort the list - bubble sort
unsorted = True
while unsorted:
    unsorted = False #zarazka
    for index in range (0, len(numbers)-1):
        if numbers[index] > numbers[index + 1]:
            highest = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = highest
            unsorted = True

# find out median
index = int(len(numbers) / 2)

if len(numbers) % 2 == 0:
    median = (numbers[index] + numbers[index - 1]) / 2
else:
    median = numbers[index]

print("sorted list: ", numbers)
print('count:', len(numbers), 'sum:', sum(numbers), 
      'minimum:', min(numbers), 'maximum:', max(numbers), 
      'average:', sum(numbers)/len(numbers), 'median:', median)
