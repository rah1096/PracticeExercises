'''
The computer will pick a number between 1 and 100. (You can choose any high number you want.)
The purpose of the game is to guess the number the computer picked in as few guesses as possible.

The user will enter his or her guess until the correct number is guessed.

The program will keep asking the user to guess until he or she gets the number correct. Then the
program will print how many guesses were required.
'''
from random import randrange


def guess_number():
    print "Time to play a guessing game."
    number = int(raw_input("Enter a number between 1 and 100: "))
    rand_num = randrange(1, 6)
    count = 1
    while number != rand_num:
        count += 1
        if number > rand_num:
            number = int(raw_input("Too high. Try again: "))
        else:
            number = int(raw_input("Too low. Try again: "))
    else:
        print "Congratulations!  You got it in {} guesses." .format(count)

guess_number()