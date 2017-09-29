import wx
from Shape import Shape
from Tetrominoes import Tetrominoes

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
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoes.NoShape)

    def OnPaint(self,event):
        pass
    def OnKeyDown(self, event):
        pass

    def OnTimer(self, event):
        if event.GetId() == Board.ID_TIMER:
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
        else:
            event.Skip()

    def dropDown(self):
        pass

    def oneLineDown(self):
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        pass
    def removeFullLines(self):
        pass

    def newPiece(self):
        self.curPiece = self.nextPiece
        statusbar = self.GetParent().statusbar
        self.nextPiece.setRandomShape()
        self.curX = Board.BoardWidth / 2 + 1
        self.curY = Board.BoardHeight -1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoes.NoShape)
            self.timer.Stop()
            self.isStarted = False
            statusbar.SetStatusText('Game Over')

    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY + newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
            if self.shapeAt(x,y) != Tetrominoes.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.Refresh()

        return True

    def drawSquare(self, dc, x, y, shape):
        pass
