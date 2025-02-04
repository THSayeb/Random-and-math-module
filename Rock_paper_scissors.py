import random
print("Rock paper scissors")
while True:
    userChoice = input("Choise (rock, paper, scissor) : ")
    possibleChoice = ["rock", "paper", "scissor"]
    CompChoice = random.choice(possibleChoice)
    
    if userChoice==CompChoice:
        print(f"Both have chosen {CompChoice} \nIt is a tie ")
    elif userChoice == "rock":
        if CompChoice == "paper":
            print(f"Computer has chosen {CompChoice} \nYou lose ")
        elif CompChoice == "scissor":
            print(f"Computer has chosen {CompChoice} \nYou won ")

    elif userChoice == "scissor":
        if CompChoice == "paper":
            print(f"Computer has chosen {CompChoice} \nYou won ")
        elif CompChoice == "rock":
            print(f"Computer has chosen {CompChoice} \nYou lose ")
    
    elif userChoice == "paper":
        if CompChoice == "rock":
            print(f"Computer has chosen {CompChoice} \nYou won ")
        elif CompChoice == "scissor":
            print(f"Computer has chosen {CompChoice} \nYou lose ")
    else:
        print(f"Please enter a valid input (rock, paper, scissor)")
    
    