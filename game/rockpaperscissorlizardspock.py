# source : inside linux spécial python magazin
# Rock, Paper & Scissors the video game

import random
import time

names = ["rock", "paper", "scissors", "lizard", "spock"]
rules = {"rock": ["scissors", "lizard"], "paper": ["rock", "spock"], "scissors": ["paper", "lizard"], "lizard": ["spock", "paper"], "spock": ["scissors", "rock"]}
winning = {
"rock":{"lizard" : "Rock crushes Lizard", "scissors": "Rock crushes Scissors"},
"scissors" : {"paper" : "Scissors cut Paper", "lizard": "Scissors decapitate Lizard"},
"paper" : {"rock" : "Paper covers Rock", "spock" : "Paper disproves Spock"},
"lizard":{"spock": "Lizard poisons Spock", "paper" : "Lizard eats Paper"},
"spock" : {"scissors": "Spock smashes Scissors", "rock" : "Spock vaporizes Rock"}
}

player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Rock, Paper, Scissors, Lizard, Spock.")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(0,4)
    computer = names[computer]
    result(player, computer)
    return play_again()

def move():
    while True:
        #player = input("Rock = 1\nPaper = 2\nScissors = 3\nLizard = 4\nSpock = 5\nMake a move:")
        player = input("Rock\nPaper\nScissors\nLizard\nSpock\nMake a move:")
        try:
            player = str(player).lower()
            if player in ("rock", "paper", "scissors", "lizard", "spock"):
                return player
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter rock, paper, scissors, lizard or Spock.")

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print("Computer threw {0} !".format(computer))
    global player_score, computer_score
    if player == computer:
        print("Tie game.")
    else:
        if computer in rules[player]:
            print("Your victory has been assured.")
            print("Since :")
            print(winning[player][computer])
            player_score += 1
        else:
            print("The computer laughs as you realise yuo have been deefated.")
            print("Since :")
            print(winning[computer][player])
            computer_score += 1

def play_again():
    scores()
    answer = input("Would you like to play again? y/n : ")
    if answer in ["Y", "y", "yes", "Of course"]:
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")

def scores():
    global  player_score, computer_score
    print("High Scores")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

if __name__ == '__main__':
    start()
