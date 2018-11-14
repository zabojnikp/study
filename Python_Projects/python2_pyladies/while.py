from random import randint

points = 0
while points < 21:
    print(points)
    answer = input("Do you want to continue?") 
    if answer == 'yes':
        points = points + randint(2,10)
        print(points)
    
    elif answer == 'no':
        break
    else:
        print("Try again. Invalid input!")

if points == 21:
    print("you have won!")

elif points > 21:
    print("game over")

else:
    print("you were missing ", 21 - points, " points!" )

