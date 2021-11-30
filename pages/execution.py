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
        self.appliances_req = wx.StaticText(parent=self, label="Appliances Required:", pos=(80, 100))
        self.ingredients_req = wx.StaticText(parent=self, label="Ingredients Required:", pos=(80, 180))
        #the following fields will be filled with user data
        self.recipe_name = wx.StaticText(parent=self, label="TEST Simple Poutine TEST", pos=(60, 70))
        self.appliances = wx.TextCtrl() #not sure if this is the correct
        self.ingredients = wx.TextCtrl()
        # load in user dataManagement
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass