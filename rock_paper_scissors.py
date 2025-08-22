import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

play_again = ''
player_score = 0
computer_score = 0
while True:
    player_move = input('\nChoose [rock], [paper], [scissors]: ')

    if player_move == 'rock':
        player_move = rock
    elif player_move == 'paper':
        player_move = paper
    elif player_move == 'scissors':
        player_move = scissors
    else:
        raise SystemExit('Invalid input, please try again.')

    computer_random_number = random.randint(1, 3)
    computer_move = ''
    if computer_random_number == 1:
        computer_move = 'rock'
    elif computer_random_number == 2:
        computer_move = 'paper'
    else:
        computer_move = 'scissors'

    print(f'The computer chose {computer_move}.')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_score += 1
        print('You win!')
    elif player_move == computer_move:
        print('It\'s a draw!')
    else:
        computer_score += 1
        print('You lose!')

    print(f'Your score is {player_score} and the computer has a score of {computer_score}')
    play_again = input('Do you want to play again? - [yes} or [no]')
    if play_again == 'no':
        break