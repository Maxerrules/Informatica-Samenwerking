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

turn = 1

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

    while beurtGelukt == False:
        coX = int(input("In welke rij wil je plaatsen? > "))
        coY = int(input("In welke kolom wil je plaatsen? > "))
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
    beurtGelukt = True

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
    
    if board1 == "X" and board2 == "X" and board3 == "X":
        winCondition = True
    elif board4 == "X" and board5 == "X" and board6 == "X":
        winCondition = True
    elif board7 == "X" and board8 == "X" and board9 == "X":
        winCondition = True
    elif board1 == "X" and board4 == "X" and board7 == "X":
        winCondition = True
    elif board2 == "X" and board5 == "X" and board8 == "X":
        winCondition = True
    elif board3 == "X" and board6 == "X" and board9 == "X":
        winCondition = True
    elif board1 == "X" and board5 == "X" and board9 == "X":
        winCondition = True
    elif board7 == "X" and board5 == "X" and board3 == "X":
        winCondition = True
    elif board1 == "O" and board2 == "O" and board3 == "O":
        winCondition = True
    elif board4 == "O" and board5 == "O" and board6 == "O":
        winCondition = True
    elif board7 == "O" and board8 == "O" and board9 == "O":
        winCondition = True
    elif board1 == "O" and board4 == "O" and board7 == "O":
        winCondition = True
    elif board2 == "O" and board5 == "O" and board8 == "O":
        winCondition = True
    elif board3 == "O" and board6 == "O" and board9 == "O":
        winCondition = True
    elif board1 == "O" and board5 == "O" and board9 == "O":
        winCondition = True
    elif board7 == "O" and board5 == "O" and board3 == "O":
        winCondition = True
       
       
#  Main program
while winCondition == False:
    if turn == 0:
        drawGrid()
        placeToken(coX,coY)
        turn = turn + 1
        checkWinCondition()
    else:
        drawGrid()
        placeToken(coX,coY)
        turn = turn - 1
        checkWinCondition()

if turn == 0:
    drawGrid()
    print("Cross wins!")
else:
    drawGrid()
    print("Dots wins!")