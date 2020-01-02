# source : inside linux spécial python magazin
# Hangman the video game

from tkinter import *
from tkinter.ttk import *
from random import *
import pandas as pd

word = 0
word_length = 0
clue = 0

def gui():
    global word, word_length, clue
    df = pd.read_excel("game/datahangedman/words.xlsx")
    dictonary = df.words.values
    word = choice(dictonary)
    word_length = len(word)
    clue = ["_"] * word_length
    tries = 6

    def start():
        while game():
            pass

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
        graphic_set = graphic[hangman-1]
        hm_graphic.set(graphic_set)


    def game():
        letters_wrong = incorrecet_guesses.get()
        letter = guess_letters()
        first_index = word.find(letter)
        if first_index == -1:
            letters_wrong += 1
            incorrecet_guesses.set(letters_wrong)
        else:
            for i in range(word_length):
                if letter == word[i]:
                    clue[i] = letter
        hangedman(letters_wrong)
        clue_set = " ".join(clue)
        word_output.set(clue_set)
        if letters_wrong == tries:
            result_text = "fin du jeu. Le mot étai " + word
            result_set.set(result_text)
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)
        if "".join(clue) == word:
            result_text = "Gagné ! le mot était " + word
            result_set.set(result_text)
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)

    def guess_letters():
        letter = letter_guess.get()
        letter.strip()
        letter.lower()
        return letter

    def reset_game():
        global word, word_length, clue
        incorrecet_guesses.set(0)
        graphic_set = hangedman(0)
        hm_graphic.set(graphic_set)
        result_set.set("")
        letter_guess.set("")
        word = choice(dictonary)
        word_length = len(word)
        clue = ["_"] * word_length
        new_clue = " ".join(clue)
        word_output.set(new_clue)

    hm_window = Toplevel()
    hm_window.title("Jouons au pendu")
    incorrecet_guesses = IntVar()
    incorrecet_guesses.set(0)
    player_score = IntVar()
    computer_score = IntVar()
    result_set = StringVar()
    letter_guess = StringVar()
    word_output = StringVar()
    hm_graphic = StringVar()

    hm_frame = Frame(hm_window, padding = "3 3 12 12", width = 300)
    hm_frame.grid(column=0, row=0, sticky=(N,W,E,S))
    hm_frame.columnconfigure(0, weight=1)
    hm_frame.rowconfigure(0, weight=1)

    Label(hm_frame, textvariable = hm_graphic).grid(column=2, row=1)
    Label(hm_frame, text="Mot").grid(column=2, row=2)
    Label(hm_frame, textvariable = word_output).grid(column=2, row=3)

    Label(hm_frame, text="Saissisez une lettre").grid(column=2, row=4)
    hm_entry = Entry(hm_frame, exportselection = 0, textvariable = letter_guess).grid(column = 2, row = 5)
    hm_entry_button = Button(hm_frame, text = "Guess", command = game).grid(column = 2, row = 6)

    Label(hm_frame, text = "Gains").grid(column = 1, row = 7, sticky = W)
    Label(hm_frame, textvariable = player_score).grid(column = 1, row = 8, sticky = W)
    Label(hm_frame, text = "Pertes").grid(column = 3, row = 7, sticky = W)
    Label(hm_frame, textvariable = computer_score).grid(column = 3, row = 8, sticky = W)
    Label(hm_frame, textvariable = result_set).grid(column = 2, row = 9)
    replay_boutton = Button(hm_frame, text = "remise à zéro", command = reset_game).grid(column = 2, row = 10)

if __name__ == '__main__':
    gui()
