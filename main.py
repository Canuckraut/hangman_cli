import os
import sys
import random



words = ["able", "about", "account", "acid", "across", "act", "addition", "adjustment", "advertisement", "after", "again", "against", "agreement", "air", "all", "almost", "among",
          "amount", "amusement", "and"]

def main():
    print("====================================")
    print("   WELCOME TO THE CLI HANGMAN GAME  ")
    print("====================================")
    print("Initializing engine setup...")
    
    # Just a simple sanity check input to prove the terminal loop handles pause/input
    #user_ready = input("Are you ready to play? (y/n): ").strip().lower()
    
    #if user_ready == 'y':
    #    print("Framework loaded successfully. Ready for Phase 1 logic!")
    #else:
    #    print("Exiting framework check.")
    #    sys.exit(0)
    random_word = random.choice(words)
    print(random_word)
    letter_list = list(random_word)
    print(letter_list)
    correct_choices = set()
    incorrect_choices = set()
    mistake_counter = 0
    while True:
        user_guess = input("Please guess a letter: ").strip().lower()
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
                print(letter, end = " ")
                current_guess.append(letter)
            else:
                print("_", end = " ")
                current_guess.append("_")
        print(" ")
        print(f"The current guess is: {current_guess}")

        if current_guess == letter_list:
            print("==========================================")
            print("CONGRATULATIONS! YOU HAVE GUESSED THE WORD")
            print("==========================================")
            return




if __name__ == "__main__":
    main()