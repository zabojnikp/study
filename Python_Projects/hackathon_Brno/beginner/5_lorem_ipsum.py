import random

articles = ["the", "a", "an"]
determiner = ["another", "this", "every", "many"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]


def get_integer():
    try:
        user_input = int(input("How many lines of lorem ipsum do you need? "))
    except ValueError:
        print("You need to input integer")
    return user_input

lines = get_integer()
while lines:
    sequence = random.randint(0, 2)
    if sequence == 0:
        print(random.choice(articles), random.choice(subjects), random.choice(verbs), random.choice(adverbs))
    elif sequence == 1:
        print(random.choice(determiner), random.choice(subjects), random.choice(verbs))
    else:
        print(random.choice(determiner), random.choice(subjects), random.choice(verbs), random.choice(adverbs))    
    lines -= 1