import main
import wx
import unittest


class TestFrame(unittest.TestCase):
    def setUp(self):
        self.app = wx.App()
        self.frame = wx.Frame(None)
        self.frame.Show()


    def tearDown(self):
        wx.CallAfter(self.app.Exit)
        self.app.MainLoop()

    def testFrame(self):
        pass
