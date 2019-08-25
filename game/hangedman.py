# source : inside linux spécial python magazin
# Hangman the video game

from random import *
import pandas as pd

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
    """
        +------+
        |
        |
        |
        |
        |
    ==============
    """,
    """
        +------+
        |      |
        |      O
        |
        |
        |
    ==============
    """,
    """
        +------+
        |      |
        |      O
        |     -|
        |
        |
    ==============
    """,
    """
        +------+
        |      |
        |      O
        |     -|-
        |
        |
    ==============
    """,
    """
        +------+
        |      |
        |      O
        |     -|-
        |     /
        |
    ==============
    """,
    """
        +------+
        |      |
        |      O
        |     -|-
        |     / \\
        |
    ==============
    """
    ]
    print(graphic[hangman-1])
    return

def start():
    print("Jouons au jeux du pendu !")
    while game():
        pass
    scores()

def game():
    df = pd.read_excel("game/datahangedman/words.xlsx")
    dictonary = df.words.values
    word = choice(dictonary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("Vous avez déjà joué ", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry " + letter + "isn't what we're looking for")
                else:
                    print("Félicitations ," + letter + " est correcte.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Un autre choix ?")

        hangedman(letters_wrong)
        print(" ".join(clue))
        print("Guesses: " + str(letters_tried))

        if letters_wrong == tries:
            print("fin du jeu")
            print("le mots était :" + word)
            computer_score += 1
            break

        if "".join(clue) == word:
            print("Gagné !")
            print("Le mot était :" + word)
            player_score += 1
            break

    return play_again()

def guess_letter():
    print("Trouvez le mot mystère !")
    letter = input("Une lettre ?")
    letter = letter.strip()
    letter = letter.lower()
    return letter

def play_again():
    answer = input("Souhaitez-vous rejouer ? o/n : ")
    if answer in ["O", "o", "oui", "Oui", "Bien sûr"]:
        return answer
    else:
        print("Merci d'avoir jouer et à très bientôt")

def scores():
    global player_score, computer_score
    print("Meilleurs scores")
    print("Joueur : " + str(player_score))
    print("Ordinateur : " + str(computer_score))

if __name__ == '__main__':
    start()
