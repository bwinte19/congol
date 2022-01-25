import tkinter
import sys
from Board import Board
import time

# CONSTANTS
SQUARE_SIZE = 10 #pixels
NUM_SQUARES = 75
MAX_SPEED = 0.01
MIN_SPEED = 5



class Conway:
    def windowClose(self): #Not quite working.
        self.main.destroy()
        sys.exit()
        
    
    def incrementSpeed(self):
        if (self.speed <= MAX_SPEED): return
        self.speed /= 2
        self.speedLabel['text'] = "Speed: " + str(self.speed)
        self.main.update()

    def decrementSpeed(self):
        if (self.speed >= MIN_SPEED): return
        self.speed *= 2
        self.speedLabel['text'] = "Speed: " + str(self.speed)
        self.main.update()
    
    def randomize(self):
        self.board.randomizeBoard()
        self.main.update()
        print("randomizing board")

    def clearBoard(self):
        self.board.clearBoard()
        self.main.update()
        print("clearing board")

    def tileClicked(self, row, column):
        self.board.swapTile(row, column)
        self.main.update()

    def __init__(self):
        self.running = False
        self.quit = False
        self.speed = 0.01
        self.main = tkinter.Tk()
        self.main.title("Conways Game of Life")
        #Set Canvas
        self.canvas = tkinter.Canvas(self.main, height=NUM_SQUARES*SQUARE_SIZE, width=NUM_SQUARES*SQUARE_SIZE)
        self.canvas.grid(row=0, column=0, padx=(10, 0), pady=(10, 10))
        #Set Button Frame
        self.commandFrame = tkinter.Frame(self.main)
        self.commandFrame.grid(row=0, column=1, padx=(10, 10))
        #Set Buttons
        currIndex = 0
        self.runButton = tkinter.Button(self.commandFrame, command=self.run, text="Run Conway")
        self.runButton.grid(row=currIndex, column=0)
        currIndex += 1
        self.randomizeButton = tkinter.Button(self.commandFrame, command=self.randomize, text="Randomize Board")
        self.randomizeButton.grid(row=currIndex, column=0)
        currIndex += 1
        self.clearBoardButton = tkinter.Button(self.commandFrame, command=self.clearBoard, text="Clear Board")
        self.clearBoardButton.grid(row=currIndex, column=0)
        currIndex += 1
        self.speedUpButton = tkinter.Button(self.commandFrame, command=self.incrementSpeed, text="Speed Up")
        self.speedUpButton.grid(row=currIndex, column=0)
        currIndex += 1
        self.speedDownButton = tkinter.Button(self.commandFrame, command=self.decrementSpeed, text="Slow Down")
        self.speedDownButton.grid(row=currIndex, column=0)
        currIndex += 1
        self.speedLabel = tkinter.Label(self.commandFrame, text=("Speed: " + str(self.speed)))
        self.speedLabel.grid(row=currIndex, column=0)
        currIndex += 1
        #Set shutdown on window close
        self.main.protocol("WM_DELETE_WINDOW", self.windowClose)

        self.initBoard()
        self.main.mainloop()

    def initBoard(self):
        square_objects = []
        for ii in range(NUM_SQUARES):
            square_objects.append([])
            for jj in range(NUM_SQUARES):
                next = self.canvas.create_rectangle(jj*SQUARE_SIZE, ii*SQUARE_SIZE, (jj+1)*SQUARE_SIZE, (ii+1)*SQUARE_SIZE, fill='white')
                square_objects[ii].append(next)
                self.canvas.tag_bind(next, "<1>", lambda event, row=ii, column=jj: self.tileClicked(row, column)) 
        self.board = Board(NUM_SQUARES, square_objects, self.canvas)

    def run(self):
        if (self.running):
            self.running = False
            self.runButton['text'] = "Run Conway"
            self.main.mainloop()
        else:
            self.running = True
            self.runButton['text'] = "Stop Conway"
            while 1:
                startTime = time.time()
                self.main.update()
                endTime = time.time()
                #print("update UI time: " + str(endTime-startTime))
                time.sleep(self.speed)
                startTime = time.time()
                self.board.updateNext()
                endTime = time.time()
                #print("update squares time: " + str(endTime-startTime))

conway = Conway()
#conway.run()
