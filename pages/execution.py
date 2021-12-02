import wx

# not yet implemented in any way
# saving this one for someone else to do, so I dont do all the UI

class Execution(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        # UI implementation here:
        self.page_name = wx.StaticText(parent=self, label="Make a Recipe", pos=(120, 20))
        self.tools_req = wx.StaticText(parent=self, label="Tools Required:", pos=(10, 100))
        self.ingredients_req = wx.StaticText(parent=self, label="Ingredients Required:", pos=(10, 180))
        #the following fields will be filled with user data
        self.recipe_name = wx.StaticText(parent=self, label="", pos=(20, 70))
        self.tools_list = wx.TextCtrl(parent=self, pos=(10, 120), size=(200, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.tools_list.Show()
        self.ingredients_list = wx.TextCtrl(parent=self, pos=(10, 200), size=(200, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.ingredients_list.Show()

        # load in user dataManagement
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        #self.tools_list.SetValue( LOADED FROM RECIPE )
        #self.ingredients_list.SetValue( LOADED FROM RECIPE )
        pass