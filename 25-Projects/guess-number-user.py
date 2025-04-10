import random

def computer_guess(max_number):
    low = 1
    high = max_number
    guess = None
    attempts = 0

    print(f"Think of a number between 1 and {max_number}, and I will try to guess it.")

    while guess != low and guess != high:
        guess = random.randint(low, high)  # Randomly pick a number in the range
        attempts += 1
        print(f"Attempt {attempts}: My guess is {guess}.")
        
        feedback = input(f"Is the number {guess}? (Type 'lower', 'higher', or 'correct'): ").lower()
        
        if feedback == 'lower':
            high = guess - 1
        elif feedback == 'higher':
            low = guess + 1
        elif feedback == 'correct':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        else:
            print("Please type 'lower', 'higher', or 'correct'.")

# Calling the function with the maximum number being 10
computer_guess(10)
