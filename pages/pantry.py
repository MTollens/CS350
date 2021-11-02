import wx
from main import wordwrap as wr

class Pantry(wx.Panel):
    def __init__(self, parent): #, inline=False): # see below for why this is commented
        super().__init__(parent)
        # saving the parent for later because it is needed outside of init for this panel
        self.parent = parent

        # this is supposed to be used to designate inline mode, which would be when the contents are at the bottom of
        # the account, but that is not used currently
        # self.inline = inline

        #UI delclaration here
        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        # if not self.inline:
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.Home_button = wx.Button(parent=self, label="Home", pos=(350, 0), size=(80, 50))
        self.Home_button.Bind(wx.EVT_BUTTON, parent.setHomepage)

        # main content window, this is where the actual ingredients go
        self.ingredients_list = wx.TextCtrl(parent=self, pos=(60, 60), size=(200, 100), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.ingredients_list.Show()

        # this is where the tools are actually diplayed
        self.tools_list = wx.TextCtrl(parent=self, pos=(280, 60), size=(200, 50), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.tools_list.Show()

        # this is all the stuff below the main text window
        self.ingredient_add = wx.Button(parent=self, label="Add", pos=(0, 0), size=(50, 50))
        self.ingredient_box = wx.TextCtrl(parent=self, pos=(0, 0), size=(50, 50))
        self.ingredient_del = wx.Button(parent=self, label="Del", pos=(0, 0), size=(50, 50))

        # this is the content below the tools list box
        self.tool_add = wx.Button(parent=self, label="Add", pos=(0, 0), size=(50, 50))
        self.tool_del = wx.Button(parent=self, label="Del", pos=(0, 0), size=(50, 50))

        # part of the unused inline mode
        # self.inline_update()

        # load content
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()
        self.Home_button.SetPosition((size[0]-80, 0))
        self.ingredients_list.SetPosition((50, 50))
        self.ingredients_list.SetSize(int(size[0]/2)-40, size[1]-140)
        self.tools_list.SetPosition((int(size[0]/2)+20, 50))
        self.tools_list.SetSize(int(size[0]/2)-40, size[1] - 140)
        self.ingredient_add.SetPosition((int(size[0] * .25) - 70, size[1] - 80))
        self.ingredient_del.SetPosition((int(size[0] * .25) + 80, size[1] - 80))
        self.tool_add.SetPosition((int(size[0] * .70) - 70, size[1] - 80))
        self.tool_del.SetPosition((int(size[0] * .70) + 80, size[1] - 80))
        self.ingredient_box.SetPosition((int(size[0] * .25) - 20, size[1] - 80))
        self.ingredient_box.SetSize(100, 50)

    # unused inline mode
    # def inline_update(self):
    #     if self.inline:
    #         self.Back_Button.Hide()
    #         self.tool_add.Hide()
    #         self.tool_del.Hide()
    #         self.ingredient_add.Hide()
    #         self.ingredient_del.Hide()
    #     else:
    #         self.Back_Button.Show()
    #         self.tool_add.Show()
    #         self.tool_del.Show()
    #         self.ingredient_add.Show()
    #         self.ingredient_del.Show()


    def update_user(self):
        self.ingredients_list.SetValue(self.parent.user.pantry)
        self.tools_list.SetValue(self.parent.user.tools)