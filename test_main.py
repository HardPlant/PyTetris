import main
import wx
import unittest

class MyDialog(wx.Dialog):
    def __init__(self,parent):
        wx.Dialog.__init__(self,parent,-1,'Text')
        wx.Button(self,wx.ID_OK)

class TestFrame(unittest.TestCase):
    def setUp(self):
        self.app = wx.App()
        self.frame = wx.Frame(None)
        self.frame.Show()

    def tearDown(self):
        wx.CallAfter(self.app.Exit)
        self.app.MainLoop()

    def testDialog(self):
        def clickOK():
            pass
        wx.CallAfter(clickOK)
        self.ShowDialog()

    def ShowDialog(self):
        self.dlg = MyDialog(self.frame)
        self.dlg.ShowModal()
        self.dlg.Destroy()

if __name__ == '__main__':
    unittest.main()

