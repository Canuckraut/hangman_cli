import os
import sys

def main():
    print("====================================")
    print("   WELCOME TO THE CLI HANGMAN GAME  ")
    print("====================================")
    print("Initializing engine setup...")
    
    # Just a simple sanity check input to prove the terminal loop handles pause/input
    user_ready = input("Are you ready to play? (y/n): ").strip().lower()
    
    if user_ready == 'y':
        print("Framework loaded successfully. Ready for Phase 1 logic!")
    else:
        print("Exiting framework check.")
        sys.exit(0)

if __name__ == "__main__":
    main()