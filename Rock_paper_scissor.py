import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice:")
    print("Rock")
    print("Paper")
    print("Scissors")
    
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter rock,paper or scissors: ")
        if user_choice in ["rock", "paper", "scissors"]:
            break
        print("Invalid input. Please enter rock paper scissor")
    
    computer_choice = random.choice(choices)
    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Congratulations! You win!")
    else:
        print("You lose!")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thank you for playing!")

play_game()