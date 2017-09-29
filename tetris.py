import wx
import random

if __name__ == '__main__':
    app = wx.App()
    Tetris(None, title = 'Tetris')
    app.MainLoop()

class Tetris(wx.Frame):
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(180,380))

        self.initFrame()

    def initFrame(self):
        pass

class Board(wx.Panel):
    pass
