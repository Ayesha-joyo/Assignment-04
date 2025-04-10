import random

def guess(x):
    random_number = random.randint(1, x)  # Random number between 1 and x
    guess = -1  # Initialize with a value not equal to the random number
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))  # Get input and convert to int

        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats! You have guessed the number {random_number} correctly.')  # Correct place

# Example usage
guess(10)
