import random


boardSize = 10
board = []


# test
words = ["cat", "dog"]

# humanities
# words = [ "artifact", "immigration", "goldrush", "migration", "generation", "chinese", "mexican", "bracero", "depression", "segregation", "slavery", "civilrights" ]

# math
# words = ["cat", "dog"]

# science
# words = ["cat", "dog"]

# scratch
# words = ["cat", "dog"]

# sel
# words = ["cat", "dog"]

# swi
# words = ["cat", "dog"]

# pe
# words = ["cat", "dog"]

# head
# words = ["cat", "dog"]

# laraine
# words = ["cat", "dog"]


directions = ["right"]


def main():
    initilizeBoard()
    printBoard()
    insertWords()
    printBoard()
#    replaceDot()
    printBoard()


def initilizeBoard():
    for row in range(boardSize):
        board.append([])
        for _ in range(boardSize):
            board[row].append('.')

def printBoard():
    print()
    print()
    for row in range(boardSize):
        for column in range(boardSize):
            print(board[row][column], end=" ")
        print()
    print()
    print()

def insertWords():
    for word in words:
        while True:
            row = random.randint(0, boardSize - 1)
            column = random.randint(0, boardSize - 1)
            direction = random.choice(directions)
            valid = isValid(word, row, column, direction)
            if valid == False:
                continue
            insertWord(word, row, column, direction)
            break

def isValid(word, row, column, direction):
    for ch in word:
        if column >= boardSize:
            return False
        if row >= boardSize:
            return False
        if board[row][column] != ".":
            if board[row][column] != ch:
                return False
        column = column + 1
    return True

def insertWord(word, row, column, direction):
    for ch in word:
        board[row][column] = ch.upper()
        column = column + 1

def replaceDot():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for row in range(boardSize):
        for column in range(boardSize):
            letterPut = random.choice(letters)
            if board[row][column] == ".":
                board[row][column] = letterPut

main()
