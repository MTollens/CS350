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

        self.recipe = self.parent.user.open_recipe

        # UI implementation here:
        self.page_name = wx.StaticText(parent=self, label="Make a Recipe", pos=(120, 20))
        self.tools_req = wx.StaticText(parent=self, label="Tools Required:", pos=(10, 100))
        self.ingredients_req = wx.StaticText(parent=self, label="Ingredients Required:", pos=(10, 180))
        self.instructions_text = wx.StaticText(parent=self, label="Instructions:", pos=(10, 280))
        #the following fields will be filled with user data
        self.recipe_name = wx.StaticText(parent=self, pos=(20, 70))
        self.tools_list = wx.TextCtrl(parent=self, pos=(10, 120), size=(200, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.tools_list.Show()
        self.ingredients_list = wx.TextCtrl(parent=self, pos=(10, 200), size=(200, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.ingredients_list.Show()
        self.image = wx.StaticBox(parent=self, pos=(400, 20), size=(200,200))
        self.instructions_list = wx.TextCtrl(parent=self, pos=(10, 300), size=(500, 200), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.instructions_list.Show()

        # load in user dataManagement
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        self.recipe = self.parent.user.open_recipe
        self.recipe_name.SetLabel(self.recipe.title)

        self.tools_temp = ""
        for x in self.recipe.tools:
            self.tools_temp += x + '\n'
        self.tools_list.SetValue(self.tools_temp)

        self.ingredients_temp = ""
        for x in self.recipe.ingredients:
            self.ingredients_temp += x + '/n'
        self.ingredients_list.SetValue(self.ingredients_temp)

        #self.image = (self.recipe.image)
