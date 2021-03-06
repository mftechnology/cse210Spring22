#Program development by Marcelo Duarte
# W02 Prove: Developer - Solo Code Submission
# BYU Worldwide 2022


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
        print('-+-')
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
        

def verifywinner(board,size):
    status = False
  # verify horizontal 0 = 1 or 2 = 3
  # verify vertical  0 = 2 or 1 = 3
  # verify diagonal 0 = 3 or 1 = 2 
    if size == 6 :
      if (board[0] == board[1] or board[2] == board[3] or
          board[0] == board[2] or board[1] == board[3] or
          board[0] == board[3] or board[1] == board[2] ):
          print("We have a winner!")
          print();
          status = True;
    elif size == 9:
      if (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6] ):
          print("We have a winner!")
          print();
          status = True;
    
    return status
          
def main():
  exit = False
  answer = "y"
  
  while exit == False and answer == "y":
    # obtaint the size of the grid
    size = int(input("Whats size of grid [Insert 6 to (2x2) or 9 to (3x3) ]: "))
  
    # tratament to loop
    if size == 6 :
     nloop = 2
    elif size == 9: 
      nloop = 5
    else:
      exit = True

    # create the grid
    board = create_board(size)
  
    # display the grid
    display_board(board,size)
 
    # make a loop between the size of the grid
    for i in range(nloop):
      print(i)
      # option for X value  
      Xchoice = int(input("X's turn to choose a square (1-9) or (1-5): "))
      board[Xchoice - 1] = "x" 
    
      # display grid 
      display_board(board,size)

      #verify winner
      check = verifywinner(board,size)
      if check == True:
        break

      # leave loop because all options were attended
      if i == 4:
        break

      # option 0 value
      Ochoice = int(input("O's turn to choose a square (1-9) or (1-5): "))
      board[Ochoice - 1] = "O" 

      # display grid
      display_board(board,size)
    
      #verify winner
      check = verifywinner(board,size)
      if check == True:
        break

    answer = input("Do you want, try again? [yes = y or not = n]")

  # Message final!
  print("Good game. Thanks for playing!") 
  print()
       
if __name__ == "__main__":
    main()