from random import randint

board = []
for i in range(0,5):
    board.append(["O"]* 5)
    
#print(board)
print("Please enter numbers between 0 to 4")

def print_board(board):
    for i in board:
        print(" ".join(i))
print_board(board) 

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)

for turn in range(4): 
    print("Turn:", turn + 1)
    

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))

    #print(ship_col)
    #print(ship_row)

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already!")
        else: 
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 4:
                print("Game Over")
                break

            print_board(board)

