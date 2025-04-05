import random

choices = ["rock", "paper", "scissors"]

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice not in choices:
        print("Invalid choice. Try again.")
        return get_player_choice()
    return choice

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score => You: {player_score} | Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

play_game()
