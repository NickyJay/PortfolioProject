import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press enter to pick a card or Q then enter to quit: \n")
    if user_input == "":
        card_chosen = random.choice(diamonds)
        hand.append(card_chosen)
        diamonds.remove(card_chosen)
        print("Your Hand: ", hand)
        print("Remaining Cards: ", diamonds, "\n")
    elif user_input =="Q" or user_input == "q":
        break
    else:
        print("Enter a valid choice and try again")
if not diamonds:
    print("There are no more cards left")
    
