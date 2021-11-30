import wx
import wx.lib.scrolledpanel
from pages.custom_widgets import RecipeBox as RecipeBox


class ContentScroller(wx.Panel):
    def __init__(self, parent, size=(600, 355), pos=(0, 100)):
        wx.Panel.__init__(self, parent=parent, size=size, pos=pos)#,
                                                    # style=wx.SIMPLE_BORDER)
        self.parent = parent
        self.SetBackgroundColour((120,120,120))

        # self.SetAutoLayout(True)
        self.Hide()

        # self.bSizer = wx.BoxSizer(wx.VERTICAL)

        self.columns = 4
        self.rows = 2

        self.items = [RecipeBox(self, position=(10,10))]


    def resize_main(self, event=None, size_external=None, position_external=None):
        if size_external:
            self.SetSize(size_external)

        if position_external:
            self.SetPosition(position_external)

        # self.Layout()
        # gets the size of the current window, so we can scale everything to it
        size = self.GetSize()

        # calculate the number of rows and columns that we can fit
        self.columns = int((size[0]-20)/210)
        self.rows = int((size[1]-50)/270)
        # print("int((size[0]-160)/270)")
        # print("size[0]: {}".format(size[0]))
        # print(size[0]-160)
        print(self.rows)

        # we must always have at least one object
        # so correct for somehow getting a negative or 0
        if self.columns <= 0:
            self.columns = 1
        if self.rows <= 0:
            self.columns = 1

        # if we can fit more items than we currently have, then add more until it is correct
        if len(self.items) < (self.columns * self.rows):
            while len(self.items) < (self.columns * self.rows):
                self.items.append(RecipeBox(self, position=(0,0)))

        # alternatively remove items until we dont have too many
        elif len(self.items) > (self.columns * self.rows):
            while len(self.items) > (self.columns * self.rows):
                del self.items[0]

        # for each column
        for x in range(0, self.columns):
            # for each row
            for y in range(0, self.rows):
                # reposition every widget
                self.items[x*self.rows+y].reposition((x*210 + 10, y*270+10))

        # print("len")

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass
