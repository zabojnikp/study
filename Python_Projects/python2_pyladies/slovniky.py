## -*- coding: utf-8 -*-
# funkci, která pro argumentem zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n a jako hodnoty k nim jejich druhé mocniny.
import operator
letter_counts = {}
def create_dictionary(number):
    new_dictionary = {}
    for key in range(1,number):
        new_dictionary[key] = key ** 2
    return new_dictionary

print(create_dictionary(5))

# funkci, která sečte a vrátí sumu všech klíčů a sumu všech hodnot ve slovníku, který dostane jako argument. 
def sum_dictionary(dictionary):
    sum_keys = sum(dictionary.keys())
    sum_values = sum(dictionary.values())
    return sum_keys, sum_values

print sum_dictionary(create_dictionary(5))[0]
print sum_dictionary(create_dictionary(20))[1]

# funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci.
def string_to_dictionary():
    user_input = raw_input('What string do you want to transfer?')
    new_dictionary = {}
    for i in range(len(user_input)):
        key = user_input[i]
        new_dictionary[key] = user_input.count(key)
    sorted_dict = sorted(new_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_dict

print(string_to_dictionary())

#Napiš funkci, která vypíše obsah slovníku (klíče a k nim náležící hodnoty) na jednotlivé řádky
def dictionary_content(dictionary):
    for key, value in dictionary.items():
        print('{}:{}'.format(key, value))


print(dictionary_content(create_dictionary(10)))

dictionary = dict(string_to_dictionary())
for key, value in dictionary.items():
    print('{}:{}'.format(key, value))