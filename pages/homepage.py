import wx
from wx import html

empty = ["", " ", None]

class Homepage(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # simple button declaration
        self.Pantry = wx.Button(parent=self, label="Pantry", pos=(0, 0), size=(60, 50))
        self.Pantry.Bind(wx.EVT_BUTTON, parent.setPantry)

        self.New_recipe = wx.Button(parent=self, label="New \nRecipe", pos=(60, 0), size=(60, 50))
        self.New_recipe.Bind(wx.EVT_BUTTON, parent.setCreation)

        self.Search = wx.Button(parent=self, label="Search", pos=(120, 0), size=(110, 50))
        self.Search.Bind(wx.EVT_BUTTON, self.search)

        # creates the font for the searchbar
        font_searchtext = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=100,
                       underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        #create the searchbar
        self.Searchbar = wx.TextCtrl(parent=self, pos=(230,1), size=(220,48))
        self.Searchbar.Bind(wx.EVT_KEY_DOWN, self.searchbar_keypress)
        # set the font as the search font
        self.Searchbar.SetFont(font_searchtext)

        #more button declarations
        # self.Settings = wx.Button(parent=self, label="Settings", pos=(255, 0), size=(70, 50))
        # self.Settings.Bind(wx.EVT_BUTTON, parent.setSettings)

        self.Account = wx.Button(parent=self, label="Account", pos=(350, 0), size=(80, 50))
        self.Account.Bind(wx.EVT_BUTTON, parent.setAccount)

        self.Favorites = wx.Button(parent=self, label="Picks", pos=(0, 100), size=(50, 50))
        self.Recent = wx.Button(parent=self, label="Recent", pos=(0, 150), size=(50, 50))
        self.Help = wx.Button(parent=self, label="Help", pos=(0, 50), size=(50, 50))
        self.Help.Bind(wx.EVT_BUTTON, parent.setHelp)
        # self.Test = wx.Button(parent=self, label="Test", pos=(0, 200), size=(50, 50))
        # self.Test.Bind(wx.EVT_BUTTON, parent.setTest)

        txt_style = wx.VSCROLL | wx.HSCROLL | wx.BORDER_SIMPLE
        self.Recipe_main = wx.html.HtmlWindow(self, -1,
                                       size=(400, 200),
                                       style=txt_style,
                                               pos=(50,50))

        self.Recipe_main.LoadFile("resources/lorem.html")

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        # get the new window size after the resize event
        size = self.GetSize()
        #apply the new size to the window layout,
        #much of the items do not need to be changed since they stay on the sidebar or topbar
        self.Recipe_main.SetSize((size[0]-50, size[1]-50))
        self.Searchbar.SetSize((size[0]-310, 48))
        # self.Settings.SetPosition((size[0] - 150, 0))
        self.Account.SetPosition((size[0]-80, 0))

    # handles all the keypresses of the searchbar
    # checks the keypress event, if it is the enter key (return)
    # it will perform the search function, else it will be handled normally
    def searchbar_keypress(self, event):
        if event.GetKeyCode() == 13:
            self.search()
        else:
            event.Skip()

    # stores the search string in the users.py file, so that it is acessable to all the relevant classes
    # and so that all the various search places use the same interface
    def search(self, event=None):
        if self.Searchbar.GetValue() not in empty:
            self.parent.anon_search(self.Searchbar.GetValue())
            self.Searchbar.SetValue("")
        else:
            self.Searchbar.SetHint("Enter a search Here!")

    # all pages must implement this, even if they dont use it
    def update_user(self):
        pass