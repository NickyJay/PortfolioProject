wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 600

dragon_hp = 300
dragon_damage = 50

game_play = True

while game_play:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    print("Or 5 to stop")
    character = input("Choose your character: ")
    character = character.lower()
    if character == "1" or character =="wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character =="elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character =="human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4" or character =="orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif character =="5":
        game_play = False
        print("Goodbye")
        break
    else:
        print("Unknown Character")
if game_play == True:
    print("You have chosen the character: ", character)
    print("Health: ", my_hp)
    print("Damage: ", my_damage)
while game_play:
    dragon_hp = dragon_hp - my_damage
    print("The " , character, "damaged the Dragon!")
    print("The dragons hitpoints are now ", dragon_hp)
    print("")

    if dragon_hp <= 0:
        print("The dragon has lost the battle")
        print("")
        break
    my_hp = my_hp - dragon_damage
    print("The dragon strikes back at " ,character)
    print("The ", character, "hitpoints are now", my_hp)
    print("")

    if my_hp <= 0:
        print("The ", character, "has lost the battle")
        print("")
        break




    
