import wx


class Account(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.Sign_in = wx.Button(parent=self, label="Sign out", pos=(350, 0), size=(80, 50))
        self.Sign_in.Bind(wx.EVT_BUTTON, self.Sign_in_example)

        self.Home_button = wx.Button(parent=self, label="Home", pos=(350, 0), size=(80, 50))
        self.Home_button.Bind(wx.EVT_BUTTON, parent.setHomepage)

        self.box = wx.StaticBox(parent=self, pos=(50, 50), size=(250, 200))

        self.Units = wx.Button(parent=self, label="Metric", pos=(70, 140), size=(100, 50))
        self.Units.Bind(wx.EVT_BUTTON, self.change_units)

        self.recipe_list = wx.TextCtrl(parent=self, pos=(60, 60), size=(200, 100), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # self.ingredients_list.Show()

        self.Account_name = wx.StaticText(parent=self, pos=(70, 70), size=(150, 20))
        self.Account_age = wx.StaticText(parent=self, pos=(70, 90), size=(150, 20))

        self.ingredients_list = wx.TextCtrl(parent=self, pos=(60, 60), size=(200, 100), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # self.ingredients_list.Show()

        self.tools_list = wx.TextCtrl(parent=self, pos=(280, 60), size=(200, 50), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # self.tools_list.Show()

        self.ingredient_add = wx.Button(parent=self, label="Add", pos=(0, 0), size=(50, 50))
        self.ingredient_box = wx.TextCtrl(parent=self, pos=(0, 0), size=(50, 50))
        self.ingredient_del = wx.Button(parent=self, label="Del", pos=(0, 0), size=(50, 50))

        self.tool_add = wx.Button(parent=self, label="Add", pos=(0, 0), size=(50, 50))
        self.tool_del = wx.Button(parent=self, label="Del", pos=(0, 0), size=(50, 50))

        self.update_user()

        # there is supposed to be a way to render panels inside panels, but I couldnt get it to work, might be worth looking at again
        # self.pantry = pn.Pantry(self, True)
        #
        # self.self_sizer = wx.BoxSizer()
        # self.pantry_sizer = wx.BoxSizer()
        #
        # self.pantry_sizer.Add(self.pantry, 1, wx.ALL | wx.EXPAND, 20)
        # self.self_sizer.Add(self.pantry_sizer, 1, wx.ALL | wx.EXPAND, 20)
        #
        # self.SetSizer(self.self_sizer)


    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()
        self.Home_button.SetPosition((size[0]-80, 0))
        self.Sign_in.SetPosition((size[0] - 160, 0))

        self.ingredients_list.SetPosition((50, 260))
        self.ingredients_list.SetSize(int(size[0]/2)-40, size[1]-330)
        self.tools_list.SetPosition((int(size[0]/2)+20, 260))
        self.tools_list.SetSize(int(size[0]/2)-40, size[1] - 330)

        self.recipe_list.SetPosition((int(size[0] / 2) + 20, 60))
        self.recipe_list.SetSize(int(size[0] / 2) - 40, 190)

        self.ingredient_add.SetPosition((int(size[0] * .25) - 70, size[1] - 60))
        self.ingredient_del.SetPosition((int(size[0] * .25) + 80, size[1] - 60))
        self.tool_add.SetPosition((int(size[0] * .70) - 70, size[1] - 60))
        self.tool_del.SetPosition((int(size[0] * .70) + 80, size[1] - 60))
        self.ingredient_box.SetPosition((int(size[0] * .25) - 20, size[1] - 60))
        self.ingredient_box.SetSize(100, 50)

    # updates the fields with user dataManagement if it is available
    def update_user(self):
        self.Account_name.SetLabel("Name: {}".format(self.parent.user.username))
        self.Account_age.SetLabel("Account age: {}".format(self.parent.user.account_age))
        self.tools_list.SetValue(self.parent.user.tools)
        self.ingredients_list.SetValue(self.parent.user.pantry)
        self.recipe_list.SetValue(self.parent.user.recipes)

    # called on button press
    def change_units(self, event=None):
        self.parent.user.settings["Metric"] = not(self.parent.user.settings["Metric"])
        self.update_units()

    # changes the units in the GUI
    def update_units(self):
        if self.parent.user.settings["Metric"]:
            self.Units.SetLabel("Metric")
        else:
            self.Units.SetLabel("Imperial")
        #TODO some code here to send the units update to the server, using the user class

    # to be replaced by real function, this is for demo purposes only
    def Sign_in_example(self, event):
        if self.parent.user.signed_in:
            self.parent.user.example_guest()
            self.parent.setSignin()
        self.update_user()



