import random

def get_names_surnames():
    names = []
    surnames = []
    for forenames, filename in ((names, 'data/forenames.txt'),
                        (surnames, 'data/surnames.txt')):
        for name in open(filename, encoding="utf8"):
            forenames.append(name.rstrip())
    return names, surnames

forenames, surnames = get_names_surnames()

new_file = open("random_names.txt", "w", encoding="utf8")
for i in range (100):
    line = "{0} {1}\n".format(random.choice(forenames), random.choice(surnames))
    new_file.write(line)


full_names = []
for name in zip(forenames, surnames):
    full_names.append(name)
    print(name)

print(len(forenames))
print(len(surnames))