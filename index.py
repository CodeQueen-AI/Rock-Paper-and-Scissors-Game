import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, and Paper beats Rock")
    
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nMake your choice: (rock, paper, scissors) or type 'quit' to exit.")
        user_choice = input("Your choice: ").lower()
        
        if user_choice == 'quit':
            print("Game Over!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
    
        print(f"Score - You: {user_score}, Computer: {computer_score}")

# Run the game
rock_paper_scissors()