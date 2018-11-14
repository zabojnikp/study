veta = "mama ma misu".split()
print(veta)

test = "hello, world!".split()
print(test)

zaznamy = "3A,8B,2E,9D".split(',')
print(zaznamy)

slova = " ".join(veta)
print(slova)

veta = "mama ma misu!"
print(veta[-5:-1])
slova = veta.split()
print(slova[2])



# funkce, která vybere jen ty správně zadané záznamy, které mají správně jméno i příjmení s velkým počátečním písmenem.
zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník', 'Marius Andrei Dima']
result_correct = []
result_incorrect = []


def checking_values(list):
    number_of_records = len(list)
    for index in range (number_of_records):
        name_surname = list[index]
        split_name_surname = name_surname.split()
        names_count = len(split_name_surname)
        iscorrect = True
        for i in range (names_count):
            names = split_name_surname[i]
            first_letter = names[0]

            if first_letter.islower():
                iscorrect = False
                break
        
        if iscorrect:
            result_correct.append(name_surname)
        
        else:
            result_incorrect.append(name_surname)

    return result_correct, result_incorrect

def fix_list(list):
    result_fixed = []
    values = checking_values(list)
    incorrect_values = values[1]
    number_of_records = len(incorrect_values)
    for index in range (number_of_records):
        name_surname = list[index]
        split_name_surname = name_surname.split()
        names_count = len(split_name_surname)
        fixed_name = []
        for i in range (names_count):
            names = split_name_surname[i]
            fixed = names.capitalize()
            fixed_name.append(fixed)
        result_fixed.append(' '.join(fixed_name))
    return result_fixed

print(fix_list(zaznamy))