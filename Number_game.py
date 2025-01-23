print("                             Number game                 \nHere, you have to guess the number the I am thinking about\nIf you collect 3 points You will win")

import random
playing = True
points = 0
while playing:
    num = int(random.randint(10,20))
    i = int(input("Enter a number between 10 to 20 : "))
    if i == num:
        print(f"Your points have increased                       [{points+1}]" )
        points += 1
        if points == 3:
            print("And\nYou have won the challenge")
            break
    else:
        print(f"Wrong guess                                      [{points}] \nLet's try again\n")
