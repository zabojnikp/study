animals = ['dog', 'cat', 'rabbit', 'snake', 'ponny', 'mouse', 'dunkey']

# funkce, která vrací jména domácích zvířat (zadaných argumentem), která jsou kratší než 5 písmen.
def less_than (number):
    count = len(animals)
    short_animals = []
    for i in range(count):
        if len(animals[i]) < number:
            short_animals.append(animals[i])
    
    return short_animals   

print(less_than(5))

# funkce, která vrací jména domácích zvířat (zadaných argumentem), která začínají na vybrane pismeno.
def start_with_letter (letter):
    count = len(animals)
    start_with = []
    for i in range(count):
        if animals[i][0] == letter:
            start_with.append(animals[i])

    return start_with

print(start_with_letter('k'))

#funkce, která dostane slovo a zjistí, jestli je v seznamu domácích zvířat.
def verify_in_list (list):
    word = input("Which animal do you want to verify if exist in the list?")
    if word in list:
        return True
    else:
        return False

print(verify_in_list(animals))

#program, který seřadí seznam domácích zvířat podle abecedy
animals.sort()
print(animals)

#funkce, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno
def takeSecond(elem):
    return elem[1]

animals.sort(key=takeSecond)
print(animals)

#funkce, která zvířata seřadí podle delky
animals.sort(key=len)
print(animals)

#je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False)
def birth_number():
    while True:
        try:
            user_input = input('What is your birth number? ')
            if int(user_input[0:6]) and int(user_input[-4:]) and user_input[6] == "/":
                return user_input
            else:
                print('incorrect format, please try again')
        
        except ValueError:
            print("incorrect format, please try again")


print(birth_number())

#je delitelne cislem
def divisible(number):
    user_birth_number = birth_number()
    stripped_number = user_birth_number.replace('/', '')
    if int(stripped_number) % number == 0:
        return True
    else:
        return False

print(divisible(11))

#Jaké datum narození je v čísle zakódováno? (vrací trojici čísel – den, měsíc, rok)
def rozkodovani():
    user_birth_number = birth_number()
    year = user_birth_number[:2]
    month = user_birth_number[2:4]
    day = user_birth_number[4:6]
    if int(day) > 31:
        print('invalid day input')
    
    elif int(month) >= 50:
        girl_month = user_birth_number[3:4]
        print("date: {}.{}.19{}".format(day, girl_month, year))
    
    else:
        print("date: {}.{}.19{}".format(day, month, year))

    return day, month, year

print(rozkodovani())

# Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')
def pohlavi():
    sex = ['woman', 'man']
    user_birth_number = birth_number()
    month = user_birth_number[2:4]
    if int(month) > 12:
        return sex[0]
    else:
        return sex[1]

print(pohlavi())