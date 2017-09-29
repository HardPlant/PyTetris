import wx
from Shape import Shape


class Board(wx.Panel):
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300
    ID_TIMER = 1

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.initBoard()

    def initBoard(self):
        self.timer = wx.Timer(self, Board.ID_TIMER)
        self.isWaitingAfterLine = False
        self.curPiece = Shape()
        self.nextPiece = Shape()
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.isStarted = False
        self.isPaused = False

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_TIMER, self.onTimer, id=Board.ID_TIMER)

        self.clearBoard()

    def shapeAt(self, x, y):
        pass
    def setShapeAt(self,x,y):
        pass
    def squareWidth(self):
        pass
    def sqareHeight(self):
        pass

    def start(self):
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.newPiece()
        self.timer.Start(Board.Speed)

    def pause(self):
        pass
    def clearBoard(self):
        pass
    def OnPaint(self,event):
        pass
    def OnKeyDown(self, event):
        pass
    def OnTimer(self, event):
        pass
    def dropDown(self):
        pass
    def oneLineDown(self):
        pass
    def pieceDropped(self):
        pass
    def removeFullLines(self):
        pass
    def newPiece(self):
        pass
    def tryMove(self, newPiece, newX, newY):
        pass
    def drawSquare(self, dc, x, y, shape):
        pass
