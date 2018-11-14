#print fibonacci sequece until 20
fibonacci_numbers = [0, 1]
for index in range(2, 25):
    fibonacci_numbers.append(fibonacci_numbers[index-1] + fibonacci_numbers[index-2])

print(fibonacci_numbers)

#print fibonacci sequesce from function
def fibonaci(n):
    fibonacci_numbers = [0, 1]
    for index in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[index-1] + fibonacci_numbers[index-2])
    return fibonacci_numbers

print(fibonaci(30))

#fibonacci list in fuction based on user input
def inputNumber(message):
    while True:
      try:
        user_input = int(input(message))
        if user_input < 0:
            print("Please add number bigger than 0. Try again")
            continue
            
        return user_input

      except ValueError:
           print("That's not a number. Try again")    
      


def fibonacci():
    fibonacci_numbers = [0, 1]
    n = inputNumber("How many fibonacci numbers do you want to see?")

    if n < 2 and n >= 0:
        return fibonacci_numbers[0:n]
       
    elif n >= 2:
        for index in range(2, n):
            fibonacci_numbers.append(fibonacci_numbers[index-1] + fibonacci_numbers[index-2])
        return fibonacci_numbers

    
print(fibonacci())

#new_fibonacci = list(fibonacci_numbers)
#print(new_fibonacci)
#one_item = new_fibonacci[-1]
#print(one_item)
#fibonacci not in list

list = [1, 2, 5, 10, 15, 18, 20, 15]
def average(numbers):
    return float(sum(numbers) / len(numbers))

print(average(list))