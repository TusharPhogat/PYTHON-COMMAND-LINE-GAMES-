"""
Hi, This is your friend . Here i am going to make a classic game of Hangman.
Hangman --> How it works
It's still a work in progress
"""
import time
def split(word):
    for char in word:
        return [char for char in word]  

def ask():
    word = "test"
    word_chars = split(word)
    word_chars = ['t','e','s']
    guess = []
    turns = 7
    guesses = []
    print("Do you want to continue(y/n):", end="")
    ans = input()
    if ans.lower() == "y" or ans.lower() == "yes":
        while turns > 0:
            if guesses != word_chars:
                if turns == len(word)+3:
                    chars = input("Enter a char of word:")
                    guess.append(chars)
                    guesses.append(chars)
                else:
                    chars = input("\nEnter a char of word:")
                    guess.append(chars)
                    guesses.append(chars)
                if len(chars) == 1:
                    for char in word:
                        if char in guess:
                            print(char, end="")
                        else:
                            print("-", end="")
                    turns -= 1
                else:
                    print("You need to enter a single character")
            else:
                print("\nYou Won!!!!")
                print("Congratulations")
                turns = 0
            if turns == 0 and guesses != word_chars:
                print("\nYou Lose!!")
                print("Restart to play")
    elif ans.lower() == 'n' or ans.lower() == 'no':
        print("Exiting Hangman", end="")
        for i in range(0,3):
            time.sleep(.2)
            print(".", end="")
    else:
        print("Enter a valid character")

def game():
    ask()
game()


