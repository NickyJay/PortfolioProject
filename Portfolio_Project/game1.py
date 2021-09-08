import random
import os


def WordList():
    global generated_word
    word_list =["blue", "green", "tiger", "dog", "black", "white", "monkey", "bat", "donkey", "gold", "look"]
    generated_word = random.choice(word_list)
    return generated_word

word = WordList()

for i in word:
    print("_", end = " ")

def CheckWord(word, guessed_word, guess, incorrect_guesses):
    status = "" ""
    matches = 0
    for letter in word:
        if letter in guessed_word:
            status += letter
        else:
            status +="_ "
        
    if guess not in word:
        incorrect_guesses.append(guess)
    if matches >1:
        print(matches, guess)
    elif matches ==1:
        print("You correctly guessed: ", guess)
    return status



def hangman():
    incorrect_guesses = []
    guesses = 0
    guessed_word = []
    chances = len(word) + 5
    while(chances > 0):
        print("\nIncorrect guesses: ", incorrect_guesses)
        guess = input("Guess a Letter: ")
        chances -=1
        print("Guesses left: ", chances)
        if guess in guessed_word:
            print("You already guessed this letter")
            chances +=1
        elif len(guess) == 1 and guess.isalpha():
            guessed_word.append(guess)
            result = CheckWord(word, guessed_word, guess, incorrect_guesses)

            if result == word:
                print("Congratulations you have won")
                print("The word that was guessed was: ", word)
                break
            else:
                print(result)
        else:
            print("Invalid input")
            chances+=1
        guesses += 1
    if guesses == chances:
        print("Word is: ", word)
    if chances == 0:
        print("Sorry but you lose.")
        print("The word was: ", word)



#hangman()