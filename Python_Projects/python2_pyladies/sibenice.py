import random
import string
import obrazky

possible_words = ['chair', 'pen', 'table', 'game', 'umbrela']
selected_word = random.choice(possible_words)
word = ' _ ' * len(selected_word)
unsuccesfull_try = 0
wrong_letters = []
print(word)
isCompleted = False

while isCompleted == False:

    user_input = raw_input('Guess the letter: ')

    if user_input in string.ascii_lowercase and len(user_input) == 1:
        if user_input in selected_word:
            for i in range (len(word)):
                if selected_word[i] == user_input:
                    word[i] = user_input
            print(user_input)
        else:
            if user_input in wrong_letters:
                print("You have already selected this letter")
            
            else:
                print("Selected letter is not correct")
                wrong_letters.append(user_input)
                print obrazky.seznam_obrazku[-len(wrong_letters)]

        isCompleted = True       

        for letter in word:
            if letter == ' - ':
                isCompleted = False
                break
        
        if len(wrong_letters) == 6:
            print("You lose!")
            isCompleted = False
            break
        
        print " ".join(word)
        print " ".join(wrong_letters) 

    else:
        print('Needs to be one letter from "abcdefghijklmnopqrstuvwxyz"')

if isCompleted == True:
    print('Congratulation, you have won!')