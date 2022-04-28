
"""        

Program development by Marcelo Duarte
"""

def create_board(number):
    # create a grid between size that were pass of parameter
    board = []
    for i in range(number):
        board.append(i + 1)
    return board

def display_board(board,size):
    # show screen grid 2X2 or 3X3
    print()
    if size == 6:
        print()
        print(f"{board[0]}|{board[1]}")
        print('-+-+-')
        print(f"{board[3]}|{board[4]}")
        print()
    elif size == 9:
        print()
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print('-+-+-')
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print('-+-+-')
        print(f"{board[6]}|{board[7]}|{board[8]}")
        print()
    else:
        print("Grid size unable")


def main():
  
  size = int(input("Whats size of grid [Insert 6 to (2x2) or 9 to (3x3) ]: "))
  board = create_board(size)
  display_board(board,size)
  
  print("Good game. Thanks for playing!") 







##choiceX = (input("turn to choose a square (1-9): "))
##choice0 = (input("turn to choose a square (1-9): "))        


if __name__ == "__main__":
    main()