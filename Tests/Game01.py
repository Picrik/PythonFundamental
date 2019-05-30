# First try for a "guess a number game"


def ask_for_number(invite):
    while True:
        saisie = input(invite)
        try:
            saisie = int(saisie)
        except:
            print("Only numericals !", file=sys.stderr)
        else:
            return saisie


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


def ask_for_number_unknow():
    return ask_for_number("Type the number to guess")


def fix_boundary():
    while True:
        minimum = ask_for_number("What's the min ?")
        maximum = ask_for_number("What's the max ?")
        if maximum > minimum:
            return minimum, maximum


def play():
    minimum, maximum = fix_boundary()
    number = ask_for_number_unknow()
    play_game(number, minimum, maximum)


if __name__ == "__main__":
    play()