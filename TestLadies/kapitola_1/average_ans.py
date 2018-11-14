numbers = []

while True:
    try:
        user_input = input("Input number or Enter for end: ")
        if user_input:
            number = int(user_input)
            numbers.append(number)

        else:
            break

    except ValueError as err:
        print(err)

print('numbers: ', numbers)
print ('count: ', len(numbers), '\ntotal: ', sum(numbers), '\nminimum: ', min(numbers),
'\nmaximum: ', max(numbers), '\naverage: ', sum(numbers)/len(numbers))
