import wx
import wx.lib.scrolledpanel
from pages.custom_widgets import RecipeBox as RecipeBox


class ContentScroller(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, size=(600, 355), pos=(0, 100)):
        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent, size=size, pos=pos)#,
                                                    # style=wx.SIMPLE_BORDER)
        self.parent = parent
        self.SetBackgroundColour((120,120,120))
        self.SetupScrolling(True)
        # self.SetAutoLayout(True)
        self.Hide()

        self.bSizer = wx.BoxSizer(wx.VERTICAL)

        columns = 4
        cur_col = 0
        cur_row = 0


        # self.bSizer = wx.GridSizer(columns, 12, 10)
        icons_per_page = 25
        for x in range(0, icons_per_page):
            # bSizer.Add(wx.Button(self, label="Button {}".format(x)), x, wx.ALL, 5)
            temp = RecipeBox(self, (210 * cur_col+10, 260*cur_row+10))
            temp.Bind(wx.EVT_SIZE, temp.OnResize)
            if x == (icons_per_page -1):
                temp.next_page()
            elif x == (icons_per_page -2):
                temp.previous_page()
            else:
                temp.dummy()
            self.bSizer.Add(temp, x, wx.ALL, 5)
            cur_col += 1
            if cur_col > columns:
                cur_col = 0
                cur_row += 1
        # self.bSizer.SetCols(3)

        self.SetSizer(self.bSizer)

    # commit the changes to the item positions
    def compile_contents(self):
        pass

    # generates the positions of the internal objects
    def precompile(self):
        pass


    def resize_main(self, event=None, size_external=None, position_external=None):
        if size_external:
            self.SetSize(size_external)
            # self.bSizer.SetMinSize()

        if position_external:
            self.SetPosition(position_external)

        self.Layout()
        # gets the size of the current window, so we can scale everything to it
        size = self.parent.GetSize()



    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass
