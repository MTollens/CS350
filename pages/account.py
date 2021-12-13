import wx
from pages import theme

class Account(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.pantry_ingredients = wx.StaticText(self, label="Pantry contents", pos=(50, 355))
        self.pantry_tools = wx.StaticText(self, label="Pantry tools", pos=(50, 355))
        self.recipes = wx.StaticText(self, label="Recipes", pos=(50, 355))

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.Sign_in = wx.Button(parent=self, label="Sign out", pos=(350, 0), size=(80, 50))
        self.Sign_in.Bind(wx.EVT_BUTTON, self.sign_out)

        self.Home_button = wx.Button(parent=self, label="Home", pos=(350, 0), size=(80, 50))
        self.Home_button.Bind(wx.EVT_BUTTON, parent.setHomepage)

        self.box = wx.StaticBox(parent=self, pos=(50, 50), size=(250, 200))

        self.Units = wx.Button(parent=self, label="NULL", pos=(70, 140), size=(100, 50))
        self.Units.Bind(wx.EVT_BUTTON, self.change_units)

        self.Public = wx.Button(parent=self, label="NULL", pos=(180, 140), size=(100, 50))
        self.Public.Bind(wx.EVT_BUTTON, self.change_public)

        self.recipe_list = wx.TextCtrl(parent=self, pos=(60, 60), size=(200, 100), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.recipe_open = wx.Button(self, label="Open")
        self.recipe_open.Bind(wx.EVT_BUTTON, self.make_recipe)
        self.recipe_edit = wx.Button(self, label="Edit")
        self.recipe_edit.Bind(wx.EVT_BUTTON, self.edit_recipe)
        self.recipe_input = wx.TextCtrl(self)
        self.recipe_input.SetHint("Enter a number to modify that recipe")
        self.recipe_delete = wx.Button(self, label="Delete")
        self.recipe_delete.Bind(wx.EVT_BUTTON, self.delete_recipe)

        # must be true to delete a recipe
        self.delete_confirm = False
        # rememberd value for what the user wanted to delete
        self.wants_to_delete = -1

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

        if theme.enable and self.parent.user.platform == "Windows":
            if theme.dark_theme:
                self.SetBackgroundColour(theme.dark)
                self.SetForegroundColour(theme.light)
                self.pantry_tools.SetForegroundColour(theme.light)
                self.pantry_ingredients.SetForegroundColour(theme.light)
                self.recipes.SetForegroundColour(theme.light)
                self.recipe_list.SetBackgroundColour(theme.dark)
                self.recipe_list.SetForegroundColour(theme.light)
                self.ingredients_list.SetForegroundColour(theme.light)
                self.ingredients_list.SetBackgroundColour(theme.dark)
                self.tools_list.SetBackgroundColour(theme.dark)
                self.tools_list.SetForegroundColour(theme.light)
                self.Account_age.SetForegroundColour(theme.light)
                self.Account_name.SetForegroundColour(theme.light)

            self.ingredient_add.SetBackgroundColour(theme.primary)
            self.ingredient_del.SetBackgroundColour(theme.primary)
            self.tool_add.SetBackgroundColour(theme.primary)
            self.tool_del.SetBackgroundColour(theme.primary)
            self.recipe_edit.SetBackgroundColour(theme.accent)
            self.recipe_delete.SetBackgroundColour(theme.primary)
            self.recipe_open.SetBackgroundColour(theme.secondary)
            self.Units.SetBackgroundColour(theme.secondary)
            self.Public.SetBackgroundColour(theme.secondary)
            self.Back_Button.SetBackgroundColour(theme.secondary)
            self.Home_button.SetBackgroundColour(theme.primary)
            self.Sign_in.SetBackgroundColour(theme.secondary)



    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()
        self.Home_button.SetPosition((size[0]-80, 0))
        self.Sign_in.SetPosition((size[0] - 160, 0))

        self.ingredients_list.SetPosition((50, 380))
        self.ingredients_list.SetSize(int(size[0]/2)-40, size[1]-450)
        self.tools_list.SetPosition((int(size[0]/2)+20, 380))
        self.tools_list.SetSize(int(size[0]/2)-40, size[1] - 450)

        self.recipe_list.SetPosition((int(size[0] / 2) + 20, 60))
        self.recipe_list.SetSize(int(size[0] / 2) - 40, 220)
        self.recipe_input.SetPosition((int(size[0] / 2) + 180, 60 + 225))
        self.recipe_input.SetSize(int(size[0] / 2) - 195-60, 50)
        self.recipe_edit.SetPosition((int(size[0] / 2) + 100, 60 + 225))
        self.recipe_edit.SetSize((75, 50))
        self.recipe_open.SetPosition((int(size[0] / 2) + 20, 60 + 225))
        self.recipe_open.SetSize((75, 50))
        self.recipe_delete.SetPosition((size[0]-70, 60 + 225))
        self.recipe_delete.SetSize(50,50)

        self.ingredient_add.SetPosition((int(size[0] * .25) - 70, size[1] - 60))
        self.ingredient_del.SetPosition((int(size[0] * .25) + 80, size[1] - 60))
        self.tool_add.SetPosition((int(size[0] * .70) - 70, size[1] - 60))
        self.tool_del.SetPosition((int(size[0] * .70) + 80, size[1] - 60))
        self.ingredient_box.SetPosition((int(size[0] * .25) - 20, size[1] - 60))
        self.ingredient_box.SetSize(100, 50)

        self.recipes.SetPosition((int(size[0]/2) + 20, 30))
        self.pantry_tools.SetPosition((int(size[0]/2) + 20, 355))

    # updates the fields with user dataManagement if it is available
    def update_user(self):
        self.Account_name.SetLabel("Name: {}".format(self.parent.user.username))
        self.Account_age.SetLabel("Account age: {}".format(self.parent.user.account_age))
        self.tools_list.SetValue(self.parent.user.get_tool_names())
        self.ingredients_list.SetValue(self.parent.user.get_pantry_names())
        self.recipe_list.SetValue(self.parent.user.get_recipe_names())
        self.get_unit_label()
        self.get_private_label()
        self.recipe_input.SetValue("")

    def delete_recipe(self, event=None):
        # print("confirm : {}  wants to : {}".format(self.delete_confirm, self.wants_to_delete))
        if not self.delete_confirm:
            self.wants_to_delete = self.recipe_input.GetValue()
            self.recipe_input.SetValue("")
            self.recipe_input.SetHint("Type CONFIRM to confirm delete\nthen press delete again")
            self.delete_confirm = True
        else:
            if self.recipe_input.GetValue() == "CONFIRM":
                print(self.wants_to_delete)
                # print("deleting a recipe!")
                self.parent.user.delete_recipe((int(self.wants_to_delete) - 1))
                self.recipe_list.SetValue(self.parent.user.get_recipe_names())
            self.recipe_input.SetValue("")
            self.recipe_input.SetHint("Enter a number to modify that recipe")
            self.wants_to_delete = -1
            self.delete_confirm = False


    # Sets default button value
    def get_unit_label(self):
        if self.parent.user.metric:
            self.Units.SetLabel("Metric")
        else:
            self.Units.SetLabel("Imperial")

    # Sets default button value
    def get_private_label(self):
        if self.parent.user.public:
            self.Public.SetLabel("Public")
        else:
            self.Public.SetLabel("Private")

    # called on button press
    def change_units(self, event=None):
        self.parent.user.change_units()
        self.get_unit_label()

    def change_public(self, event=None):
        self.parent.user.change_public()
        self.get_private_label()

    # BELOW MAY BE USELESS!

    # changes the units in the GUI
    def update_units(self):
        if self.parent.user.metric:
            self.Units.SetLabel("Metric")
        else:
            self.Units.SetLabel("Imperial")
        #TODO some code here to send the units update to the server, using the user class

    # similar function as metric but for setting public/private account
    def update_public(self):
        if self.parent.user.public:
            self.Public.SetLabel("Public")
        else:
            self.Public.SetLabel("Private")
        #TODO some code here to send the update to the server, using the user class

    # # to be replaced by real function, this is for demo purposes only
    # def Sign_in_example(self, event):
    #     if self.parent.user.signed_in:
    #         self.parent.user.example_guest()
    #         self.parent.setSignin()
    #     self.update_user()
    def sign_out(self, event=None):
        self.parent.user.logout()
        self.parent.first_sign_in = True
        self.parent.setSignin()


    def make_recipe(self, event=None):
        if self.recipe_position_is_valid():
            self.parent.user.open_recipe = self.parent.user.recipes[int(self.recipe_input.GetValue())-1]
            self.parent.setExecution()
        self.recipe_input.SetValue("")

    def edit_recipe(self, event=None):
        if self.recipe_position_is_valid():
            self.parent.user.open_recipe = self.parent.user.recipes[int(self.recipe_input.GetValue())-1]
            self.parent.setEdit()
        self.recipe_input.SetValue("")

    def recipe_position_is_valid(self):
        try:
            return len(self.parent.user.recipes) >= int(self.recipe_input.GetValue())
        except:
            print("invalid recipe index\nfor length:")
            print(len(self.parent.user.recipes))
            print("got : {}".format(self.recipe_input.GetValue()))
            return False
