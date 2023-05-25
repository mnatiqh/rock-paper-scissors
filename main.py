import random

game = ("Rock" , "Paper" , "Scissors")

while True:
    computer = random.choice(game)

    user=input("Enter Rock, Paper or Scissors (q-quit): ")

    print("Computer played:" ,computer)

    if user == computer :
        print("Draw, please try again.")

    elif user == "Rock" :

        if computer == "Paper" :
            print("You lost.")

        else :
            print("You won!!!")

    elif user == "Paper" :
        
        if computer == "Scissors" :
            print("You lost.")

        else :
            print("You won!!!")

    elif user == "Scissors" :

        if computer == "Rock" :
            print("You lost.")

        else :
            print("You won!!!")

    elif user == "q" :
        print("Thanks for playing the game!!!")
        break

    else :
        print("Invalid input. Please learn how to play the game atleast and then come here XD.")

