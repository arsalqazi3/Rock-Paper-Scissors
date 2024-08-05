import random

computerDict = {1: "Rock", 2: "Paper", 3: "Scissors"}
userDict = {"r": 1, "p": 2, "s": 3}

def Menu():
    print("====================== Menu ======================")
    print("1. Know the rules of the game")
    print("2. Play the game against computer")
    print("3. Exit")

while True:
    Menu()
    choice = input("Please select one option: ")
    
    if choice == "1":
        print("====================== Rules of the game ======================")
        print("Rock wins against Scissors")
        print("Paper wins against Rock")
        print("Scissors wins against Paper")
    
    elif choice == "2":
        computerChoice = random.choice([1, 2, 3])
        userChoice = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")
        
        if userChoice in userDict:
            YouChoice = userDict[userChoice]

            print(f"You chose: {computerDict[YouChoice]}")
            print(f"Computer chose: {computerDict[computerChoice]}")

            if computerChoice == YouChoice:
                print("It is a draw")
            elif (YouChoice - computerChoice) % 3 == 1:
                print("You win!!")
            else:
                print("Computer wins!!")
        else:
            print("Invalid choice. Please enter r, p, or s.")
    
    elif choice == "3":
        print("Exiting the game. Goodbye!")
        break
    
    else:
        print("Invalid option. Please select a valid option from the menu.")

