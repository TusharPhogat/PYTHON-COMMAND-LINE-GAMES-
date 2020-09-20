"""
Hi, This is your friend . Here i am going to make a classic game of Hangman.
Hangman --> How it works

"""
import time

def ask():
    word = "test"
    guess = []
    turns = len(word)+3
    guessed_word = []
    print("Do you want to continue(y/n):", end="")
    ans = input()
    if ans.lower() == "y" or ans.lower() == "yes":
        while turns > 0 and guessed_word != word:
            if turns == len(word)+3:
                chars = input("Enter a char of word:")
                guess.append(chars)
            else:
                chars = input("\nEnter a char of word:")
                guess.append(chars)
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
        print("Exiting Hangman", end="")
        for i in range(0,3):
            time.sleep(.2)
            print(".", end="")

def game():
    ask()
game()


