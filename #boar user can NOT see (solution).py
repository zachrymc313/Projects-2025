import random

#board user can NOT see (solution)
board = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
#board user can see
boardDisplay = [[-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1]]

def checkMinesAround(row, col):
    t=0 #total mines around spot
    i=row - 1
    while i <= row+1:
        if i>=0 and i<5:
            j=col - 1
            while j<=col +1:
                if j>=0 and j<5:
                     t = t+board[i][j]  
                j=j+1 
        i=i+1
    return t


#add mines
numMines = int(input("How many mines? "))
if numMines > 25:
    print("Impossible. Setting to 5 default.")
    numMines = 5
num = 0 #num mines
while num < numMines:
    row= random.randint(0,4)
    col= random.randint(0,4)
    if board[row][col] == 0:
        board[row][col] = 1  #add mine
        num=num+1

def displaySol():
    for row in range(0,5):
        for col in range(0,5):
            print(board[row][col], end=" ")
        print("")

def displayBoard():
    print("-"*21)   
    for row in range(0,5):
        print("|", end="")
        for col in range(0,5):
            if boardDisplay[row][col] == -1:
                print(" ", end=" | ")
            else:
                print(boardDisplay[row][col], end=" | ")
        print("")
        print("-"*21)   

displaySol()
displayBoard()

guess=0
while guess < (25 - numMines):
    row = int(input("Guess a row(1-5): "))-1
    col = int(input("Guess a col(1-5): "))-1
    if board[row][col] ==1:
        print("Booom! You hit a mine!") 
        displaySol()
    else:
        boardDisplay[row][col] = checkMinesAround(row, col) 
        displayBoard()
        guess = guess + 1   