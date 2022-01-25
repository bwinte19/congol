import random
import time
from copy import deepcopy

class Board:
  def setSquares(self):
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        filln = ""
        if self.board[i][j]:
          filln = 'black'
        else:
          filln = 'white'
        self.canvas.itemconfig(self.squares[i][j], fill=filln)
  
  def swapTile(self, i, j):
    self.board[i][j] += 1
    self.board[i][j] %= 2
    self.setSquaresByList([(i, j)])
  
  def setSquaresByList(self, list):
    for t in list:
      filln = ""
      if self.board[t[0]][t[1]]:
        filln = 'black'
      else:
        filln = 'white'
      self.canvas.itemconfig(self.squares[t[0]][t[1]], fill=filln)

  def __init__(self, count, squares, canvas):
    self.board = []
    self.squares = squares
    self.canvas = canvas
    for i in range(count):
      self.board.append([])
      for j in range(count):
        self.board[i].append(0)
    #print(self.board)
    print("length of board" + str(len(self.board)))
    self.setSquares()

  def neighborCount(self, board, i, j):
    count = 0
    length = len(self.board)
    for y in range(i-1, i+2):
      for x in range(j-1, j+2):
        count += board[(y+length)%length][(x+length)%length]
    count -= board[i][j]
    return count



  def updateNext(self):
    oldBoard = deepcopy(self.board)
    changes = []
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        nsum = self.neighborCount(oldBoard, i, j)
        if nsum == 3:
          self.board[i][j] = 1
          changes.append((i, j))
        if nsum > 3 or nsum < 2:
          self.board[i][j] = 0
          changes.append((i, j))
    
    self.setSquaresByList(changes)
    #self.setSquares()


  def randomizeBoard(self):
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        self.board[i][j] = random.randint(0, 1)
    self.setSquares()
  
  def clearBoard(self):
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        self.board[i][j] = 0
    self.setSquares()
  
  
        
    