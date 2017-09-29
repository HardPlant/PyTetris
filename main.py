import wx
import random
from Tetris import Tetris

if __name__ == '__main__':
    app = wx.App()
    Tetris(None, title = 'Tetris')
    app.MainLoop()



