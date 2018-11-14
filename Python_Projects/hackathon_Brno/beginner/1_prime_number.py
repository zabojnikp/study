prime_numbers = []

def get_integer():
    try:
        user_input = input("Input any number: ")
        number = int(user_input)
    except ValueError as err:
        print("Error!", err)
    return number
    
def is_prime(value):
    if value > 1:
        for i in range(2, value):
            if (value % i) == 0:
                return False
        return True
    else:
        return False

user_input = get_integer()

if is_prime(user_input):
    for y in range(2, user_input + 1):
        if is_prime(y):
            prime_numbers.append(y)
    print(prime_numbers)

else:
    print("Not a prime number")

#kratsi zapis z mnohem chytrejsich zdroju :)
def new_prime(n):
    for i in range(3,n):
        if n % i == 0:
            return False
    return True