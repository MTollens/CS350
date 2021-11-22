# import wx
# import wx.lib.scrolledpanel
#
#
# class GUI(wx.Frame):
#
#     def __init__(self, parent, id, title):
#         # First retrieve the screen size of the device
#         screenSize = wx.DisplaySize()
#         screenWidth = screenSize[0]
#         screenHeight = screenSize[1]
#
#         # Create a frame
#         wx.Frame.__init__(self, parent, id, title, size=screenSize, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
#
#         panel1 = wx.Panel(self, size=(screenWidth, 28), pos=(0, 0), style=wx.SIMPLE_BORDER)
#         panel1.SetBackgroundColour('#FDDF99')
#         self = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(screenWidth, 400), pos=(0, 28),
#                                                     style=wx.SIMPLE_BORDER)
#         self.SetupScrolling()
#         self.SetBackgroundColour('#FFFFFF')
#
#         button1 = wx.Button(self, label="Button 1", pos=(0, 50), size=(50, 50))
#         button2 = wx.Button(self, label="Button 2", pos=(0, 100), size=(50, 50))
#         button3 = wx.Button(self, label="Button 3", pos=(0, 150), size=(50, 50))
#         button4 = wx.Button(self, label="Button 4", pos=(0, 200), size=(50, 50))
#         button5 = wx.Button(self, label="Button 5", pos=(0, 250), size=(50, 50))
#         button6 = wx.Button(self, label="Button 6", pos=(0, 300), size=(50, 50))
#         button7 = wx.Button(self, label="Button 7", pos=(0, 350), size=(50, 50))
#         button8 = wx.Button(self, label="Button 8", pos=(0, 400), size=(50, 50))
#
#         self.bSizer = wx.BoxSizer(wx.VERTICAL)
#         self.bSizer.Add(button1, 0, wx.ALL, 5)
#         self.bSizer.Add(button2, 0, wx.ALL, 5)
#         self.bSizer.Add(button3, 0, wx.ALL, 5)
#         self.bSizer.Add(button4, 0, wx.ALL, 5)
#         self.bSizer.Add(button5, 0, wx.ALL, 5)
#         self.bSizer.Add(button6, 0, wx.ALL, 5)
#         self.bSizer.Add(button7, 0, wx.ALL, 5)
#         self.bSizer.Add(button8, 0, wx.ALL, 5)
#         self.SetSizer(self.bSizer)
#
#
# if __name__ == '__main__':
#     app = wx.App()
#     frame = GUI(parent=None, id=-1, title="Test")
#     frame.Show()
#     app.MainLoop()

import wx
import wx.lib.scrolledpanel
from pages.custom_widgets import RecipeBox as RecipeBox


class ContentScroller(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, size=(600, 355), pos=(0, 100)):
        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent, size=size, pos=pos)#,
                                                    # style=wx.SIMPLE_BORDER)
        self.parent = parent
        self.SetupScrolling(True)
        # self.SetAutoLayout(True)
        self.Hide()

        self.bSizer = wx.GridSizer(4, 10, 10, 10)


        # self.precompile()

        # regenerates the sizer of items
        # self.compile_contents()
        for x in range(3):
            self.bSizer.Add(RecipeBox(self), 0, wx.ALL, 5)
            # self.bSizer.Add(wx.Button(self), 0, wx.ALL, 5)
            # if x > 5:
            #     print("break")
            # self.bSizer.Add(RecipeBox(self), )

        self.SetSizer(self.bSizer)
        self.Layout()



    # commit the changes to the item positions
    def compile_contents(self):
        # for x in self.itemlist:
        #     self.bSizer.Detach(x)
        # self.bSizer = wx.BoxSizer(wx.VERTICAL)
        # for x in self.itemlist:
        #     self.bSizer.Add(x, 0, wx.ALL, 5)
        # self.SetSizer(self.bSizer)
        pass

    # generates the positions of the internal objects
    def precompile(self):
        pass
        # size = self.parent.GetSize()
        # # print("size[0] % 210")
        # columns = int(size[0] / 210)
        # print("{}  /  {}  = {}".format(size[0], 210, columns))
        # print(columns)
        # if columns <= 0:
        #     columns = 1
        # c_column = 0
        # c_row = 0
        #
        # for x in self.itemlist:
        #     x.SetPosition((210*c_column, 260*c_row))
        #     # self.bSizer.Add(x, 0, wx.ALL, 5)
        #     c_column += 1
        #     # print("{}  {}".format(c_column, c_row))
        #     if c_column > columns:
        #         c_row += 1
        #         c_column = 0


    def resize_main(self, event=None, size_external=None, position_external=None):
        if size_external:
            self.SetSize(size_external)
            # self.bSizer.SetMinSize()

        if position_external:
            self.SetPosition(position_external)
        # gets the size of the current window, so we can scale everything to it
        size = self.parent.GetSize()

        #
        # self.precompile()
        # self.compile_contents()

        # self.SetSize((size[0], size[1]-100))
        # for x in self.bSizer:
        #     x.SetSize((50, size[1]-20))

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass
