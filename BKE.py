#  Import library's
import os

#  Create variable's
board1 = "*"
board2 = "*"
board3 = "*"
board4 = "*"
board5 = "*"
board6 = "*"
board7 = "*"
board8 = "*"
board9 = "*"

turn = 0

coX = 0
coY = 0

winCondition = False


#  Define functions
def drawGrid():
    print(board1 + board2 + board3)
    print(board4 + board5 + board6)
    print(board7 + board8 + board9)


def placeToken(coX,coY):
    global board1
    global board2
    global board3
    global board4
    global board5
    global board6
    global board7
    global board8    
    global board9

    beurtGelukt = False

    while not beurtGelukt:
        if coX == 1:
            if coY == 1:
                if board1 == "*":
                    if turn == 1:
                        board1 = "X"
                    elif turn == 0:
                        board1 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
            elif coY == 2:
                if board2 == "*":
                    if turn == 1:
                        board2 = "X"
                    elif turn == 0:
                        board2 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
            elif coY == 3:
                if board3 == "*":
                    if turn == 1:
                        board3 = "X"
                    elif turn == 0:
                        board3 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
        if coX == 2:
            if coY == 1:
                if board4 == "*":
                    if turn == 1:
                        board4 = "X"
                    elif turn == 0:
                        board4 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
            elif coY == 2:
                if board5 == "*":
                    if turn == 1:
                        board5 = "X"
                    elif turn == 0:
                        board5 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
            elif coY == 3:
                if board6 == "*":
                    if turn == 1:
                        board6 = "X"
                    elif turn == 0:
                        board6 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
        if coX == 3:
            if coY == 1:
                if board7 == "*":
                    if turn == 1:
                        board7 = "X"
                    elif turn == 0:
                        board7 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
            elif coY == 2:
                if board8 == "*":
                    if turn == 1:
                        board8 = "X"
                    elif turn == 0:
                        board8 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")
            elif coY == 3:
                if board9 == "*":
                    if turn == 1:
                        board9 = "X"
                    elif turn == 0:
                        board9 = "O"
                    beurtGelukt = True
                else:
                    print("This spot is taken, try again.")

def checkWinCondition():
    global winCondition
    global board1
    global board2
    global board3
    global board4
    global board5
    global board6
    global board7
    global board8    
    global board9
    
    if (board1 and board2 and board3) == "x":
        winCondition = True
    elif (board4 and board5 and board6) == "x":
        winCondition = True
    elif (board7 and board8 and board9) == "x":
        winCondition = True
    elif (board1 and board4 and board7) == "x":
        winCondition = True
    elif (board2 and board5 and board8) == "x":
        winCondition = True
    elif (board3 and board6 and board9) == "x":
        winCondition = True
    elif (board1 and board5 and board9) == "x":
        winCondition = True
    elif (board7 and board5 and board3) == "x":
        winCondition = True
    elif (board1 and board2 and board3) == "O":
        winCondition = True
    elif (board4 and board5 and board6) == "O":
        winCondition = True
    elif (board7 and board8 and board9) == "O":
        winCondition = True
    elif (board1 and board4 and board7) == "O":
        winCondition = True
    elif (board2 and board5 and board8) == "O":
        winCondition = True
    elif (board3 and board6 and board9) == "O":
        winCondition = True
    elif (board1 and board5 and board9) == "O":
        winCondition = True
    elif (board7 and board5 and board3) == "O":
        winCondition = True
       
       
#  Main program
while winCondition == False:
    if turn == 0:
        drawGrid()
        coX = int(input("In welke rij wil je plaatsen? > "))
        coY = int(input("In welke kolom wil je plaatsen? > "))
        placeToken(coX,coY)
        turn = turn + 1
        checkWinCondition()
    else:
        drawGrid()
        coX = int(input("In welke rij wil je plaatsen? > "))
        coY = int(input("In welke kolom wil je plaatsen? > "))
        placeToken(coX,coY)
        turn = turn - 1
        checkWinCondition()

if turn == 0:
    drawGrid()
    print("Cross wins!")
else:
    drawGrid()
    print("Dots wins!")