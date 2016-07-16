import random
import os
import sys


with open(r"hangman_words.txt") as w:
    word_bank = w.read().split()


def clear():
    """System level command to clear screen"""
    os.system("cls" if os.name == "nt" else "clear")


def strike_calculator(secret_word):
    """Allows more guesses for longer words"""
    if len(secret_word) <= 5:
        return 5
    else:
        return 7


def draw(bad_guesses, good_guesses, secret_word, strikes):
    """The basic view given to the user whilst playing"""
    clear()
    print("Strikes: {} / {}\n".format(len(bad_guesses), strikes), end="\n")
    print(" ".join([char for char in bad_guesses]), end="\n\n\n")
    print("".join([char if char in good_guesses else '_' for char in secret_word]), end="\n\n")


def get_guess(bad_guesses, good_guesses):
    """Requests and validates input from user"""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        clear()

        if len(guess) != 1:
            print("\nYou must only guess a single letter!\n")
        elif guess in bad_guesses or guess in good_guesses:
            print("\nYou've already guessed that!\n")
        elif not guess.isalpha():
            print("\nYou can only guess letters!\n")
        else:
            return guess


def welcome():
    """Introduction screen that allows user to play or quit"""
    print("Welcome to hangman!")
    start_question = input("Press enter to play, or type 'q' to quit: ").lower()
    if start_question == "q":
        print("Bye")
        sys.exit()


def play():
    """Main loop that calls all other functions"""
    secret_word = random.choice(word_bank)
    good_guesses = []
    bad_guesses = []
    strikes = strike_calculator(secret_word)

    while True:
        clear()
        draw(bad_guesses, good_guesses, secret_word, strikes)
        guess = get_guess(bad_guesses, good_guesses)

        # Add letter to good guesses and check if player wins
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(set(secret_word)):
                draw(bad_guesses, good_guesses, secret_word, strikes)
                print("You win! The secret word was {}.".format(secret_word))
                break

        # Add letter to bad guesses and check if player loses
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == strikes:
                draw(bad_guesses, good_guesses, secret_word, strikes)
                print("You lose! The secret word was {}".format(secret_word))
                break

    # Allow the user to play again or not
    play_again = input("Would you like to play again?\nY / n ") 
    if not play_again or play_again[0].lower().strip() != "n":
        return play()
    else:
        print("Goodbye!")
        sys.exit()


if __name__ == "__main__":
    welcome()
    play()
