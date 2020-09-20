"""
Hi, This is your friend . Here i am going to make a classic game of Hangman.
Hangman --> How it works

"""
import time
def split(word):
    for char in word:
        return char
def ask():
    word = "test"
    guess = []
    guesses =[]
    word_chars = split(word)
    turns = len(word)+3
    print("Do you want to continue(y/n):", end="")
    ans = input()
    if ans.lower() == "y" or ans.lower() == "yes":
        while turns > 0 and guesses != word_chars:
            if turns == len(word)+3:
                chars = input("Enter a char of word:")
            else:
                chars = input("\nEnter a char of word:")
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


