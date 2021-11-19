import wx
import wx.lib.scrolledpanel

empty = ["", " ", None]

class Search(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # simple button declaration
        self.Search = wx.Button(parent=self, label="Search", pos=(0, 0), size=(110, 50))
        self.Search.Bind(wx.EVT_BUTTON, self.search)

        # creates the font for the searchbar
        font_searchtext = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=100,
                       underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        #create the searchbar
        self.Searchbar = wx.TextCtrl(parent=self, pos=(110,1), size=(220,48), style=wx.TE_PROCESS_ENTER)
        # set the font as the search font
        self.Searchbar.Bind(wx.EVT_KEY_DOWN, self.searchbar_keypress)
        self.Searchbar.SetFont(font_searchtext)

        #more button declarations
        # self.Settings = wx.Button(parent=self, label="Settings", pos=(255, 0), size=(70, 50))
        # self.Settings.Bind(wx.EVT_BUTTON, parent.setSettings)

        self.Home = wx.Button(parent=self, label="Home", pos=(350, 0), size=(80, 50))
        self.Home.Bind(wx.EVT_BUTTON, parent.setHomepage)

        # IMPORTANT
        # the search panel does not implement the content scroll by itself, it uses the parent rendering another frame to do it
        # so dont expect to find it here


    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        # get the new window size after the resize event
        size = self.GetSize()
        #apply the new size to the window layout,
        #much of the items do not need to be changed since they stay on the sidebar or topbar
        # self.Recipe_main.SetSize((size[0], size[1]-50))
        # self.Scroller.SetSize((size[0], size[1]-100))
        self.Searchbar.SetSize((size[0]-190, 48))
        # self.Settings.SetPosition((size[0] - 150, 0))
        self.Home.SetPosition((size[0]-80, 0))

    # all pages must implement this, even if they dont use it
    def update_user(self):
        self.Searchbar.SetHint(self.parent.user.current_search)

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
            #use the offical search channel
            self.parent.anon_search(self.Searchbar.GetValue())
            # clear the input so it is visible that something happened
            self.Searchbar.SetValue("")
        else:
            self.Searchbar.SetHint("Enter a search Here!")