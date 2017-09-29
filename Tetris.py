import wx
from Board import Board

# Tetris App Frontend

class Tetris(wx.Frame):
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(180,380))
        self.initFrame()

    def initFrame(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('0')
        self.board = Board(self)
        self.board.start()

        self.Centre()
        self.Show(True)
