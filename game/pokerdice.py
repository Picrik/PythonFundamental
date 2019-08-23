# source : inside linux spécial python magazin
# pokerdice the video game

import random
from itertools import groupby

neuf = 1
dix = 2
valet = 3
reine = 4
roi = 5
As = 6

names = {neuf:"9", dix:"10", valet:"J", reine:"Q", roi:"K", As:"A"}

player_score = 0
computer_score = 0

def start():
    print("Jouons au jeu de Poker, mais avec des dés")
    while game():
        pass
    scores()

def game():
    print("L'ordinateur va vous aider à lancer les dés")
    throws()
    return play_again()

def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print("Dice : " + str(i+1) + ";" + names[dice[i]])

    result = hand(dice)
    print("vous avez actuellement" + result)

    while True:
        rerolls = input("Combien de dés souhaitez vous relancer ?")
        try:
            if rerolls in (1,2,3,4,5):
                break
        except ValueError:
            pass
        print("Je n'ai pas comprit. Veillez saisir 1,2,3,4 ou 5.")
    if rerolls == 0:
        print("Vous terminez avec" + result)
    else:
        roll_number = rerolls
        dice_rerolls = roll(roll_number)
        dice_changes = range(rerolls)
        print("Saisissez le nombre de dés à rejour :")
        iteration = 0
        while iteration < rerolls:
            itertation += 1
            while True:
                selection = input("")
                try:
                    if selection in (1,2,3,4,5):
                        break
                except ValueError:
                    pass
                print("Je n'ai pas comprit. Veillez saisir 1,2,3,4 ou 5.")
            dice_change[iteration-1] = selection-1
            print("Vous avez changé de dé", selection)
        iteration = 0
        while iteration < rerolls:
            iteration += 1
            replacement = dice_rerolls[iterations-1]
            dice[dice_changes[iteration-1]] = replacement
        dice.sort()
        for i in range(len(dice)):
            print("Dé" + str(i+1) + ":" + names[dice[i]])
        result = hand(dice)
        print("Vous terminez avec " + result)

def roll(roll_number):
    numbers = range(1,7)
    dice = range(roll_number)
    iteration = 0
    while iteration < roll_number:
        iteration += 1
        dice[iteration-1] = random.choice(numbers)
    return dice

def hand(dice):
    dice_hand = [len(list(group)) for key, group in groupyby(dice)]
    dice_hand.sort(reverse=True)
    straigth1 = [1,2,3,4,5]
    straigth2 = [2,3,4,5,6]

    if dice == straigth1 or dice == straigth2:
        return "Une suite !"
    elif dice_hand[0] == 5:
        return "Cinq cartes identiques !"
    elif dice_hand[0] == 4:
        return "Poker !"
    elif dice_hand[0] ==3:
        if dice_hand[1] == 2:
            return "Full !"
        else:
            return "Brelan"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "Deux paires"
        else:
            return "Une paire"
    else:
        return "une carte haute"

def play_again():
    answer = input("Voulez-vous rejouez ? o/n")
    if answer in ("o", "O", "oui", "Oui", "Bien sûr !"):
        return answer
    else:
        print("Merci d'avoir joué !")

def scores():
    global player_score, computer_score
    print("Meilleurs scores")
    print("Joueur : " + str(player_score))
    print("Ordinateur : " + str(computer_score))

if __name__ == '__main__':
    start()
