import random
from game_logic import *
import os

correct_guesses = []
incorrect_guesses = []
letter_count = len(generated_word)
guess_count = 0

while(True):
    print("------HANGMAN---------")
    print("1. To Play")
    print("2. To Quit")
    player_choice = input("Please choose an option: ")
    if player_choice == "2":
        print("Play Again Soon!")
        break
    elif player_choice =="1":
        BlankWord()
        while(True):
            print("Correct guesses: ", correct_guesses)
            print("Incorrect guesses: ", incorrect_guesses)
            guess = input("Guess a Letter: ")
            if guess.isalpha() == False:
                print("Invalid input")
            elif guess.lower() in correct_guesses:
                print("You have already guessed that letter")
            elif guess.lower() in generated_word:
                correct_guesses.append(guess)
                guess_count +=1
                os.system('clear')
                if guess_count == letter_count:
                    print("Correct Word: ", generated_word, "\nCongratulations you win!")
                    break
            elif guess.lower() not in generated_word:
                print("Incorrect")
                incorrect_guesses.append(guess)
                os.system('clear')
            else:
                print("Invalid Input")
    else:
        print("\nPlease choose a valid option\n")