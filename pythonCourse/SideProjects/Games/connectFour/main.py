import random
print("Welcome to Connect 4")
print("-----------------------")



table = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""],
         ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]
rows = 6
cols = 7
# print(table)

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end ="")
    for x in range(rows):
        print("\n  +----+----+----+----+----+----+----+")
        print(x, "|", end ="")
        for y in range(cols):
            if(table[x][y] =="R"):
                print("", table[x][y], end=" |")
            elif(table[x][y]=="B"):
                print("", table[x][y], end=" |")
            else:
                print(" ", table[x][y], end = "  |")
    
    print("\n  +----+----+----+----+----+----+----+")


def checkLine(chip, startRow, startCol, deltaRow, deltaCol):
    for i in range(i):
        row = (startRow + i)*deltaRow
        col = (startCol + i)*deltaRow
        
        if not(0 <= row< rows and 0<= col < cols and table[row][col] == chip):
            return False
    return True;



# printGameBoard()            
def modifyTurn(spacePicked, turn):
    table[spacePicked[0]][spacePicked[1]] = turn
    
def checkForWinner(chip):
    for y in range(rows):
        for x in range(cols - 3):
            if x<= cols - 4 and checkLine(chip, y, x, 0,1): # Horizontal
                return True
            if y <= rows - 4 and checkLine(chip, y, x, 1, 0):  # Vertical
                return True
            if x <= cols - 4 and y <= rows - 4 and checkLine(chip, y, x, 1, 1):  # Diagonal - left to right
                return True
            if x <= cols - 4 and y >= 3 and checkLine(chip, y, x, -1, 1):  # Diagonal right to left
                return True

    return False

                
                
firstMove = input("Do you want to go first? (yes/no): ").strip().lower()
turnCounter = 0

if firstMove == 'no':
    cpuCol = random.randint(0, cols - 1)
    while not modifyTurn(cpuCol, "B"):
        cpuCol = random.randint(0, cols - 1)
    turnCounter += 1 

while True:
    printGameBoard()
    
    if turnCounter % 2 ==0:
        currentTurn = "R"
        userInp = input("It's your turn, place your piece.").strip().lower()
        userInd = ord(userInp) - ord('A')
    else:
        currentTurn = "B"
        userInd = random.randint(0, cols - 1)
        while not modifyTurn(userInd, currentTurn):
            userInd = random.randint(0, cols - 1)
        print("AI played in column", chr(userInd + ord('A')))

    if 0 <= userInd < cols:
        if modifyTurn(userInd, currentTurn):
            if checkForWinner(currentTurn):
                printGameBoard()
                print(f"Player {currentTurn} wins!")
                break
            turnCounter += 1
        else:
            print("Column is full! Choose another column.")
            if currentTurn == "R":
                continue  # Prompt the user again for a valid move
    else:
        print("Invalid column! Please choose between A and G.")
    
    
    
    #--- Do Something--#