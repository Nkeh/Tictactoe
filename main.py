import random

print("Welcome to your Tic Tac Toe")
print("---------------------------")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3],[4,5,6],[7,8,9]]

rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print("\n+-----+-----+-----+")
        print("|", end="")
        for y in range(cols):
            print(" ", gameBoard[x][y], end="  |")
    print("\n+-----+-----+-----+\n")

def modifyArray(num, turn):
    num -= 1
    if (num == 0):
        gameBoard[0][0] = turn
    elif (num == 1):
        gameBoard[0][1] = turn
    elif (num == 2):
        gameBoard[0][2] = turn
    elif (num == 3):
        gameBoard[1][0] = turn
    elif (num == 4):
        gameBoard[1][1] = turn
    elif (num == 5):
        gameBoard[1][2] = turn
    elif (num == 6):
        gameBoard[2][0] = turn
    elif (num == 7):
        gameBoard[2][1] = turn
    elif (num == 8):
        gameBoard[2][2] = turn


def checkWinner(gameBoard):
    ### X axis
    if (gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[0][0] == "0" and gameBoard[0][1] == "0" and gameBoard[0][2] == "0"):
        print("You lose")
        return "0"
    elif (gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[1][0] == "0" and gameBoard[1][1] == "0" and gameBoard[1][2] == "0"):
        print("You lose")
        return "0"
    elif (gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[2][0] == "0" and gameBoard[2][1] == "0" and gameBoard[2][2] == "0"):
        print("You lose")
        return "0"
    ### Y axis
    elif (gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[0][0] == "0" and gameBoard[1][0] == "0" and gameBoard[2][0] == "0"):
        print("You lose")
        return "0"
    elif (gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[0][1] == "0" and gameBoard[1][1] == "0" and gameBoard[2][1] == "0"):
        print("You lose")
        return "0"
    elif (gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[0][2] == "0" and gameBoard[1][2] == "0" and gameBoard[2][2] == "0"):
        print("You lose")
        return "0"
    ### Cross axis
    elif (gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[0][0] == "0" and gameBoard[1][1] == "0" and gameBoard[2][2] == "0"):
        print("You lose")
        return "0"
    elif (gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X"):
        print("You won")
        return "X"
    elif (gameBoard[0][2] == "0" and gameBoard[1][1] == "0" and gameBoard[2][0] == "0"):
        print("You lose")
        return "0"

leaveLoop = False
turnCounter = 0

while (leaveLoop == False):
        
        printGameBoard() 
        if (checkWinner(gameBoard) == "X" or checkWinner(gameBoard) == "0"):
            leaveLoop = True
            break

        else:
            ### player turn   
            if (turnCounter % 2 ==1):
                
                numberpicked = int(input("\nChoose a number [1-9]: "))
                if (numberpicked >=1 and numberpicked <=9):
                    modifyArray(numberpicked, "X")
                    possibleNumbers.remove(numberpicked)
                    turnCounter += 1
                else:
                    print("\nInvalid input try again")
            ### computer turn
            else:
                while(True):
                    cpuChoice = random.choice(possibleNumbers)
                    if (cpuChoice in possibleNumbers):
                        modifyArray(cpuChoice, "0")
                        possibleNumbers.remove(cpuChoice)
                        turnCounter += 1
                        break
        
         
        