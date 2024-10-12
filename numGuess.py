# Kyle Nimrick 10-11-2024
# This is a number guessing game
# The goal of this program is to help myself gain experiecne using loops and functions

import random

# Function with the tittle material that prints the tittle of the game and the author of the game
def tittle_material():
    print('') # White space for readability
    print('Number Guessing Game!')
    print('By: Kyle Nimrick')
    print('') # White space for readability

# Function that provides the instructions to the game
def game_instructions():
    print('''
Instructions:
- A random number will be taken randomly anywhere from 1 to 100
- The player will need to guess the exact number to win 
- If the player is wrong they will be prompted to increase or decrease their guess
''')

# Everything that makes the number guessing game work
def num_guess ():

    running = True

    while running:
        # Prompts the user whether they would like to play, read the instructions, or quit
        user_initial_choice = input('Would you like to [p]lay, read the [i]nstructins, or [q]uit: ').lower().strip()

        # Prompts the user again on what they would like to do
        # If the user enters the wrong input an error message is shown with what they entered
        # As well as what the proper input is supposed to be
        while user_initial_choice != 'p' and user_initial_choice != 'i' and user_initial_choice != 'q':
            print('') # White space for readability
            print(f'ERROR! You entered "{user_initial_choice}" which was invalid')
            print('Please enter either a "p", "i", or "q"')
            print('') # White space for readability
            user_initial_choice = input('Would you like to [p]lay, read the [i]nstructins, or [q]uit: ').lower().strip()
    
        # If the user enters "p" for their initial input they are entered into the game
        if user_initial_choice == 'p':
            # The random function takes a number from 1 to 100 and is assigned to chosen_random_number
            chosen_random_number = random.randint(1,100)
            
            # Prompts the user to choose a number anywhere between 1 and 100
            print('') # White space for readability
            user_second_choice = int(input('Choose a number anywhere between 1 and 100: '))
            
            # If the user enters the wrong number they are prompted to enter another number
            # As well as given a hint on whether or not to go higher or lower
            while user_second_choice != chosen_random_number:

                if user_second_choice > chosen_random_number:
                    print('') # White space for readability
                    print(f'You chose {user_second_choice} which is too high.')
                    print('Try going lower')
                    print('') # White space for readability

                elif user_second_choice < chosen_random_number:
                    print('') # White space for readability
                    print(f'You chose {user_second_choice} which is too low.')
                    print('Try going higher')
                    print('') # White space for readability

                user_second_choice = int(input('Choose a number anywhere between 1 and 100: '))
            
            # If the users second choice equals the random number a winning message is printed as well as what the number was 
            if user_second_choice == chosen_random_number:
                    print('') # White space for readability
                    print(f'Congradulations! You chose {user_second_choice} which was the random number.')
                    print('') # White space for readability
                    

        # If the user enters "i" for their initial choice they are given the instructions
        if user_initial_choice == 'i':
            game_instructions()

        # If the user enters "q" for their intial choice they are given a goodbye message and stop the program
        if user_initial_choice == 'q':
            print('') # White space for readability
            print('I hope you had fun playing the Number Guessing Game!')
            print('Goodbye :)')
            print('') # White space for readability
            running = False

def main():
    # Calls the function that contains the tittle material
    tittle_material()

    # Calls the function that contains the number gussing game
    num_guess()

# Makes everything work 
if __name__ == '__main__':
    main()

    