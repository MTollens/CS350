import wx
from pages import custom_widgets as cw


# this is a test page, just to try things out in a clean enviroment

class Test(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        # self.dropdown = wx.ComboBox(parent=self, pos=(100,100), size=(150,50))
        # self.dropdown.SetItems(["first", "second", "third"])

        # self.start = wx.Button(parent=self, label="New", pos=(50, 50), size=(50, 50))
        # self.start.Bind(wx.EVT_BUTTON, self.add_button)
        # self.list = []
        # self.list_y_start = 100
        # self.list_increment = 50
        # self.list_count = 0
        # self.list_x_start = 100
        # self.test = cw.RecipeBox(self, (100,100))
        # self.test.dummy()



        # load in user dataManagement
        # self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        # gets the size of the current window, so we can scale everything to it
        size = self.GetSize()
        # self.test.reposition((150,150))

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass

    # def add_button(self, event=None):
    #     temp = wx.Button(parent=self, label="{}".format(self.list_count),
    #                      pos=(self.list_x_start, self.list_y_start+self.list_increment*self.list_count), size=(50, 50))
    #     self.list_count += 1
    #     self.list.append(temp)