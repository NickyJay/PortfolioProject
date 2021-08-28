import random
high_score = 0


def dice_game():
    global high_score
    dice1 = random.randint(1, 6) 
    dice2 = random.randint(1, 6)
    print("You roll a...", dice1)
    print("You roll a...", dice2)
    player_score = dice1 + dice2
    print(" \nYou have rolled a total of: ", player_score)
    if player_score > high_score:
        high_score = player_score
        print("New High Score! \n")
    return high_score

playing = True
while playing:
    print("Current High Score: ", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    player_choice = input("Enter Your choice: \n")
    if player_choice == "1":
        dice_game()
    elif player_choice == "2":
        playing = False
        print("GoodBye!")
        break

