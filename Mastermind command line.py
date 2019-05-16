import random
import sys


def computerguess():
    # get computer's code guess
    for x in range(4):
        a = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
        code.append(a)
    return code


def drawboard(playerguesses, clues):
    hline = "+-----+-----+-----+-----+----------"

    print()
    print("X - correct letter and position")
    print("Y - correct letter but in the wrong position")
    print()

    for i in range(len(playerguesses)):  # cycle through right amount of lines
        print(hline)
        for j in range(4):
            print("| ", playerguesses[i][j], " ", end='')
        print("| ", clues[i])
        print(hline)


def movevalid(guess):
    if len(guess) != 4:
        return False
    else:
        for i in range(4):  # checking if it is 4 letters and between A and F
            if guess[i] not in 'ABCDEF':
                return False
        return True


def getplayerguess():
    while True:
        guessStr = input("Guess the 4 letter code, using letters A - F. No spaces.")
        guess = guessStr.upper()
        if movevalid(guess):
            return guess
        else:
            print("That is not a valid code. Try again.")


def checkguess(guess, code):
    clues = []
    temp = code.copy()  # need to use copy method, otherwise it will change the computers code!

    holdguess = list(guess)

    # loop to check for black pegs
    for i in range(4):
        if holdguess[i] == code[i]:
            clues.append("X")  # black peg-correct letter and position
            temp[i] = "M"  # remove correct location from checking
            holdguess[i] = "Q"  # take out of guess so not counted as white peg

    # loop to check for white pegs
    for j in range(4):
        if temp[j] in holdguess:
            clues.append("O")  # white peg-correct letter, wrong position
            holdguess.remove(temp[j])  # remove from check so not counted twice

    clues.sort(reverse=True)  # sort so X's are always first so player can't tell which are correct
    clue = ''.join(clues)  # convert list to a string with no spaces and return

    return clue


#game loop
while True:

    playerguesses = []
    code = []
    clues = []

    code = computerguess()
    codeStr = ''.join(code)  # make string version of the code with no spaces
    turn = 0
    wongame = False

    while turn < 10:
        guess = getplayerguess()
        playerguesses.append(list(guess))
        clue = checkguess(guess, code)
        clues.append(clue)
        drawboard(playerguesses, clues)
        if guess == codeStr:
            wongame = True
            print("You got it!!!")
            break
        turn += 1

    if wongame:
        print("You guessed the code in", turn + 1, "tries.")
    else:
        print("Sorry, you didn't guess it correctly in 10 tries.")
        print("The correct code is ", codeStr)

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        sys.exit()
