import random

level_change = False
current_level = 1
number_range = '(1-100)'
computer_number = random.randint(1, 100)
attempts_count = 0
init_attempts = 8
attempts_left = init_attempts

while True:
    if level_change:
        if current_level == 1:
            level_change = False
            current_level = 1
            number_range = '(1-100)'
            computer_number = random.randint(1, 100)
            attempts_count = 0
            init_attempts = 8
            attempts_left = init_attempts
        elif current_level == 2:
            level_change = False
            current_level = 2
            number_range = '(1-200)'
            computer_number = random.randint(1, 200)
            attempts_count = 0
            init_attempts = 9
            attempts_left = init_attempts
        elif current_level == 3:
            level_change = False
            current_level = 3
            number_range = '(1-300)'
            computer_number = random.randint(1, 300)
            attempts_count = 0
            init_attempts = 10
            attempts_left = init_attempts
    if attempts_left == init_attempts:
        player_input = input(f'Guess the number {number_range}, level {current_level}. You have \033[1m\033[4m{attempts_left}\033[00m attempts: ')
    else:
        player_input = input(f'Guess the number {number_range}. You have \033[1m\033[4m{attempts_left}\033[00m attempts left: ')
    if not player_input.isdigit():
        print('Invalid input. Try again.')
        continue
    attempts_count += 1
    attempts_left -= 1
    player_number = int(player_input)
    if player_number == computer_number:
        print(f'\033[92mYou guessed it after {attempts_count} attempts!\033[0m')
        if current_level == 1:
            player_input = input('Do you want to go to level 2? (y/n): ')
            if player_input == 'y':
                level_change = True
                current_level = 2
            else:
                print('Thanks for playing!')
                break
        elif current_level == 2:
            player_input = input('Do you want to go to level 3? (y/n): ')
            if player_input == 'y':
                level_change = True
                current_level = 3
            else:
                print('Thanks for playing!')
                break
        elif current_level == 3:
            print('\033[00mYou completed the game!\033[00m')
            player_input = input('Do you want to play again? (y/n): ')
            if player_input == 'y':
                level_change = True
                current_level = 1
            else:
                print('Thanks for playing!')
                break
    else:
        if attempts_left == 0:
            print(f'\033[91mYou have no more attempts left. The number is: {computer_number}\033[0m')
            player_input = input('Do you want to play again? (y/n): ')
            if player_input == 'y':
                level_change = True
                current_level = 1
            else:
                print('Thanks for playing!')
                break
        elif player_number > computer_number:
            print('\033[95mToo high!\033[0m')
        else:
            print('\033[94mToo low!\033[0m')