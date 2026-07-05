import os
import sys
import random
from ascii_art import hangman_title, noose_art, hangman_stages


words = ["able", "about", "account", "acid", "across", "act", "addition", "adjustment", "advertisement", "after", "again", "against", "agreement", "air", "all", "almost", "among",
          "amount", "amusement", "and"]
ascii_art = hangman_stages

def main():
    print(hangman_title)
    
    secret_word = random.choice(words)
    correct_choices = set()
    incorrect_choices = set()
    while True:
        #print(f"debug mode: {secret_word}")
        user_guess = input("Please guess a letter: ").strip().lower()

        if len(user_guess) != 1:
            print("Please enter exactly one letter")
            continue

        if not user_guess.isalpha():
            print("Please enter only letters from the english alphabet")
            continue

        if user_guess in correct_choices or user_guess in incorrect_choices:
            print("You already guessed this letter, genius!")
            continue

        if user_guess in secret_word:
            print("Great guess! You are one step closer")
            correct_choices.add(user_guess)
        else:
            print("Ouch! That was wrong. You are one step closer to death!")
            incorrect_choices.add(user_guess)

        display_word = " ".join([letter if letter in correct_choices else "_" for letter in secret_word])
        print(display_word)
        print(ascii_art[len(incorrect_choices)])
        print("incorrect guesses:", *sorted(incorrect_choices))

        if set(secret_word) == correct_choices:
            print("==========================================")
            print(f"CONGRATULATIONS! YOU HAVE GUESSED THE WORD \nThe secret word was: {secret_word}")
            print("==========================================")
            input("\nPress Enter to exit...")
            break

        if len(incorrect_choices) == len(ascii_art) -1:
            print("====================================")
            print(f"CONDOLENCES YOU HAVE LOST THE GAME! \nThe secret word was: {secret_word}")
            print("====================================")
            input("\nPress Enter to exit...")
            break



if __name__ == "__main__":
    main()