from random import choice
import functions
import obrazky

possible_words = ['game', 'chocolate', 'mobile', 'computer']
selected_word = choice(possible_words)
#print(selected_word)
word = '-' * len(selected_word)
print(word)
unsuccessful_try = 0
wrong_letters = []
isCompleted = False

while isCompleted == False:
    user_input = raw_input("Select a letter: ").lower()

    #condition to determin whether the letter is correct
    if len(user_input) == 1:
 
        #letter is correct, replace word with the user input
        if user_input in selected_word:
            count = selected_word.count(user_input)

            for i in range(0, count):
                position = selected_word.index(user_input)
                next_positions = selected_word.index(user_input, i + position)
                new_string = functions.replace_string(word, next_positions, user_input)
                word = new_string
                print(word)
        
        # letter is incorrect, put incorrect letter to list with wrong letters
        elif user_input not in wrong_letters:
            print("incorrect letter")
            unsuccessful_try = unsuccessful_try + 1
            print(obrazky.seznam_obrazku[-unsuccessful_try])
            wrong_letters.append(user_input)

        #letter is already chosen, raise this to user
        else:
            print('You have already selected this letter')

        #condition to determine whether the word is completed    
        if '-' not in word:
            isCompleted = True
            break

    elif len(user_input) == 0:
        print("you need to select at least 1 letter")

    else:
        print('you need to select only 1 letter')

#condition to determine whether the limit of tries was reached  
    if unsuccessful_try == 6:
        print("You have lost!")
        break

if isCompleted == True:
    print('You have won!')