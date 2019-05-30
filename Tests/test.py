def ask_for_number(invite):
    while True:
        saisie = input(invite)
        try:
            saisie = int(saisie)
        except:
            print("Only numericals !", file=sys.stderr)
        else:
            return saisie


number = ask_for_number("Give me a number")
print(number)
print("=" * 20)


def fix_boundary():
    while True:
        minimum = ask_for_number("What's the min ?")
        maximum = ask_for_number("What's the max ?")
        if maximum > minimum:
            return minimum, maximum


score1, score2 = fix_boundary()

print("score1 : " + str(score1) + " score2 : " + str(score2))


def play_turn(number, minimum, maximum):
    essai = ask_for_number("Try to guess")
    if essai < number:
        print("too little !")
        minimum = essai + 1
        win = False
    elif essai > number:
        print("too big !")
        maximum = essai - 1
        win = False
    else:
        print("Win !")
        win = True
        minimum = maximum = essai
    return win, minimum, maximum


def play_game(number, minimum, maximum):
    win = False
    while not win:
        win, minimum, maximum = play_turn(number, minimum, maximum)


play_game(number, score1, score2)

