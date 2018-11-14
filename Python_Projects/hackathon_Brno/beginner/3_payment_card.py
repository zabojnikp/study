def is_valid_card_number():
    while True:
        str_number = get_string_value("Input card number: ")
        if len(str_number) != 16:
          print("Card number must be 16 digits long. Please try again.")
          continue          
        total = luhn_calculation(str_number)
        break 
    return total % 10 == 0

def get_string_value(msg):
    while True:
        try:
            number = int(input(msg))
            break
        except ValueError as err:
            print(err, ". You need to input integer.")
    return str(number)

def luhn_calculation(string):
    numbers_sum = int()

    for value in (string[::-2]):
        numbers_sum += int(value)

    for value in (string[-2::-2]):
        multiplicated_value = int(value) * 2
        value = multiplicated_value if multiplicated_value < 9 else sum_digits(multiplicated_value)
        numbers_sum += value
    
    return numbers_sum

def sum_digits(integer):
    digits = [int(char) for char in str(integer)]
    return sum(digits)

print(is_valid_card_number())
