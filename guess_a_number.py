import sys
import random

def get_difficulty():
    """Prompts the user to choose a difficulty and returns the corresponding max_tries."""
    while True:
        difficulty_input = input("Choose a difficulty: Easy, Medium, or Hard - ").strip().capitalize()
        if difficulty_input == "Easy":
            return sys.maxsize
        elif difficulty_input == "Medium":
            return 10
        elif difficulty_input == "Hard":
            return 5
        else:
            print("Invalid difficulty. Please choose 'Easy', 'Medium', or 'Hard'.")

def get_player_guess():
    """Prompts the user for a number guess and validates the input."""
    while True:
        guess_input = input("Guess the number (1-100): ").strip()
        if guess_input.isdigit():
            player_number = int(guess_input)
            if 1 <= player_number <= 100:
                return player_number
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Invalid input. Please enter a whole number.")

def play_round(max_tries):
    """Manages a single round of the guessing game."""
    computer_number = random.randint(1, 100)
    tries = 0

    while tries < max_tries:
        player_number = get_player_guess()

        if player_number == computer_number:
            print(f"You guessed it in {tries + 1} tries!")
            return True
        else:
            if player_number < computer_number:
                print("Too low!\n")
            else:
                print("Too high!\n")
            tries += 1

    print(f"Sorry, you reached the maximum tries ({max_tries}). The number was {computer_number}. Better luck next time!")
    return False

def main_game():
    """Runs the main game loop, allowing the player to play multiple rounds."""
    print("Welcome to the Number Guessing Game!")
    while True:
        max_tries = get_difficulty()
        play_round(max_tries)

        while True:
            play_again = input("Do you want to play again? (yes/no) - ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == 'no':
            break

main_game()