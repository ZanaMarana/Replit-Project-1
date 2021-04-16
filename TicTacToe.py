def playTicTacToe(): #I created this in an IDE that needed a leading function to run
    #Program name: M4 Tic-Tac-Toe
    #Program purpose: Create a game using functions
    #Created/Revised: J. Singh on 4/14/21

    board = [[3*item+i+1 for i in range(3)] for item in range(3)] # defines an *initial* board by iterating in a row and col format
    midInput=input("Would you (O) like to play TicTacToe with a starting middle X?(y/n): ") #added this because i thought itd be more fun if user could enter in the middle
    if midInput.lower()=="y":
      board[1][1] = 'X' # sets X to take the place of 5 in the middle (1,1) is the middle due to indexing starting at 0
    elif midInput.lower()=="n":
      pass

    def drawBoard(board): #function that draws the board using the board's variable above
      print("+-------"*3+"+")
      for row in range(3): #iterates through each of 3 rows
        print("|       "*3+"|") #creates walls of each cell
        for col in range(3): #iterates through each of 3 columns
          print("|   "+str(board[row][col])+"   ",end="") #creates each number in cell, using end="" so no newline
        print("|")
        print("|       "*3,"|",sep="")
        print("+-------"*3,"+",sep="") #finishes drawing of each row

    def playerControl(board): #function that lets the user control where they place there 'O'
      while True: #loops until broken
        player=int(input("Enter your move: ")) #gets user input as integer
        if (len(str(player))==1) and (player<=0 or player>=10): #checks if between 0 and 10, while being 1 digit
          print("Please enter a number within the given range") #tells user to re-enter
          continue #continues to next iteration
        #when user enters a valid number on board...
        player = int(player) - 1 #subtracts input by 1 so indexing is proper
        row=player//3 #gets row by performing integer division by 3 because 3 cells in each row
        col=player%3 #gets column by getting remainder of division by 3
        if 'X'==board[row][col] or 'O'==board[row][col]: #checks if space already has an 'O' or 'X'
          print("Please enter an empty space value") #asks user to re-enter
          continue #continues to next iteration so there is no break
        break #breaks from loop once proper info is filled
      board[row][col]='O' #places O on board by replacing what was in the board variable

    from random import randrange #gets randrange so AI computer can be very smart (wink)
    def cpuControl(board): #allows opponent to place 'X's
      while True: #loops until broken
        row=randrange(3) #sets row to be random from 0-2, which is cells 1-3 in each row
        col=randrange(3) #sets col to be random from 0-2, which is cells 1-3 in each col
        if 'X'==board[row][col] or 'O'==board[row][col]: #checks if space already occupied by 'X' or 'O'
          continue #continues to next iteration so there is no break
        break #breaks once 'X' is placed properly
      board[row][col]='X' #places X on board by replacing what was in the board variable

    def winCondition(board): #allows a check for whether or not someone wins
      computerWin=False #sets a default variable for winning to False
      humanWin=False #sets a default variable for winning to False
      for col in range(3): #iterates 3 times so that every possibility of row and column is checked for a win
        if board[col][0]=='X' and board[col][1]=='X' and board[col][2]=='X': #checks 'X's for each of the 3 columns
          computerWin=True #sets variable to true
          break #breaks from loop
        elif board[col][0]=='O' and board[col][1]=='O' and board[col][2]=='O': #same as before for 'O's
          humanWin=True
          break
        elif board[0][col]=='X' and board[1][col]=='X' and board[2][col]=='X': #checks 'X's for each of the 3 rows
          computerWin=True
          break
        elif board[0][col]=='O' and board[1][col]=='O' and board[2][col]=='O': #same as before for 'O's
          humanWin=True
          break
        elif (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or (board[2][0]=='X' and board[1][1]=='X' and board[0][2]=='X'):
          computerWin=True
          break
          #this is meant to check if the 'X's are found to be 3 in a row diagonally, both ways
        elif (board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O') or (board[2][0]=='O' and board[1][1]=='O' and board[0][2]=='O'):
          humanWin=True
          break
          #same as before in the case the user doesn't want the middle starting X
        else: #otherwise everything results in False
          humanWin=False 
          computerWin=False
      if computerWin==True: #checks if computer resulted as a winner
        return 'x' #returns a letter
      elif humanWin==True: #checks if human resulted as a winner
        return 'o' #returns a letter
      else: #if no one has won
        return None #returns nothing


    for i in range(5): #iterates for the maximum amount of turns that the user can play
      if winCondition(board)=='x': #checks if the winCondition says computer win
        drawBoard(board) #shows the user the board
        break #breaks from loop
      elif winCondition(board)=='o': #checks if the winCondition says human win
        drawBoard(board) #shows user the board
        break #breaks from loop
      drawBoard(board) #draws the board for the initial run
      playerControl(board) #allows player to start their turn
      if i==4 and winCondition(board)==None: #checks if it has been 4 turns and there is still no winner (tie)
        break
      elif winCondition(board)=='o': #checks again if user has won directly after their turn
        drawBoard(board)
        break
      cpuControl(board) #now the computer opponent may make a move
      if winCondition(board)==None: #checks if nobody has won
        continue #continues to next iteration
    if winCondition(board)=='x': #asks the function who won one last time
      print("Computer win") #reports computer win
      pass #passes to the end of the program
    elif winCondition(board)=='o': #same but for human
      print("Human win")
      pass
    else: #in the event that the i==4 and winCondition is None (tie)
      drawBoard(board) #shows the final board
      print("Tie") #reports that there is a tie

playTicTacToe() #calls the function so that the game runs