import os
import sys
import random
from ascii_art import hangman_title, noose_art


words = ["able", "about", "account", "acid", "across", "act", "addition", "adjustment", "advertisement", "after", "again", "against", "agreement", "air", "all", "almost", "among",
          "amount", "amusement", "and"]


def main():
    print(hangman_title)
    
    random_word = random.choice(words)
    print(random_word)
    letter_list = list(random_word)
    print(letter_list)
    correct_choices = set()
    incorrect_choices = set()
    mistake_counter = 0
    while True:
        user_guess = input("Please guess a letter: ").strip().lower()

        if not user_guess.isalpha():
            print("Please enter only letters from the english alphabet")
            continue

        if len(user_guess) > 1:
            print("Please enter only one letter at a time")
            continue

        if user_guess in letter_list:
            if user_guess not in correct_choices:
                print("Great guess! You are one step closer")
                correct_choices.add(user_guess)
            else:
                print("You already guessed this letter genious!")
        else:
            if user_guess not in incorrect_choices:
                mistake_counter += 1
                incorrect_choices.add(user_guess)
                print("Ouch! That was wrong. You are one step closer to death!")
            else:
                print("You already made this mistake before dummy!")

        current_guess = []
        for letter in letter_list:
            if letter in correct_choices:
                print(letter + " ", end = " ")
                current_guess.append(letter)
            else:
                print("_" + " ", end = " ")
                current_guess.append("_")
        print(" ")
        print(noose_art[mistake_counter])
        print("incorrect guesses:", *sorted(incorrect_choices))

        if current_guess == letter_list:
            print("==========================================")
            print("CONGRATULATIONS! YOU HAVE GUESSED THE WORD")
            print("==========================================")
            break

        if mistake_counter == 6:
            print(f"The secret word was: {random_word}")
            print("====================================")
            print("CONDOLENCES! YOU HAVE LOST THE GAME")
            print("====================================")
            break




if __name__ == "__main__":
    main()