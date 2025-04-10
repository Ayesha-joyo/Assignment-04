import random
import string

# Ensure the words list is properly defined
from words import words  # Assuming words.py contains a list of words


def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word from the list

    while '-' in word or ' ' in word:  # Ensure no invalid words are picked
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)  # Get a valid word
    word_letters = set(word)  # Letters in the word to guess
    alphabet = set(string.ascii_uppercase)  # All possible uppercase letters
    used_letters = set()  # Letters the user has guessed
    attempts = 10 # Number of allowed incorrect guesses


    print("Welcome to Hangman!")

    while len(word_letters) > 0 and attempts > 0:
        # Display the current status of the word
        print('You have', attempts, 'attempts left.')
        print('Used letters:', ' '.join(sorted(used_letters)))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        # Check for valid input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('Good guess!')
            else:
                attempts -= 1
                print('Incorrect guess!')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    if attempts == 0:
        print("You lost! The word was:", word)
    else:
        print("Congratulations! You've guessed the word:", word)


if __name__ == "__main__":
    hangman()
