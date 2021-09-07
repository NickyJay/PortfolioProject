import random

generated_word= ""

def WordList():
    global generated_word
    word_list =["blue", "green", "tiger", "dog", "black", "white", "monkey", "bat"]
    generated_word = random.choice(word_list)
    print(generated_word)
    return generated_word

def BlankWord():
    blank_word = len(generated_word) * "_ "
    print(blank_word)


WordList()
BlankWord()
#letterReplace()
