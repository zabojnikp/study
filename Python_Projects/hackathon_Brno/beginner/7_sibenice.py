import random
import string

possible_words = ['chair', 'pen', 'table', 'game', 'umbrela']
selected_word = random.choice(possible_words)
word_length = len(selected_word)
word = '-' * word_length
isCompleted = False
available_guesses = word_length + 5
guessed_letters = []
print("I am thinking of a word. What word is it?: ")
print(word)

def get_string(msg):
    while True:
        try:
            user_input = str(input(msg)).lower()
            if user_input in string.ascii_letters and len(user_input) == 1:
                return user_input
            elif len(user_input) != 1:
                print("Input needs to be 1 letter")  
            else:
                print("Needs to be letter from ", string.ascii_letters)    
        except ValueError as err:
            print(err)

while isCompleted == False:
    letter = get_string("Guess a letter ({0} guesses available): ".format(available_guesses))
    if letter in guessed_letters:
        print("You already guessed this letter, try again.")
        continue
    
    if letter in selected_word:
        count = selected_word.count(letter)
        for i in range(0, len(selected_word)):
            if selected_word[i] == letter:
                word = word[:i] + letter + word[i + 1:]
        print("Yes, there {0} letter{1} '{2}'".format(("is" if count == 1 else "are"), ("" if count == 1 else "s"), letter))
    else: 
        print("No, the letter '{}' is not in my word".format(letter))
    
    if "-" not in word:
        isCompleted = True
        break
    
    guessed_letters.append(letter)  
    available_guesses -= 1  
    if not available_guesses:
        print("Computer wins!")
        isCompleted = False
        break
    print(word)

if isCompleted:
    print("Congratulation, you have won!")
print("Guessed word was:", selected_word)