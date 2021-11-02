import wx


# this is a test page, just to try things out in a clean enviroment

class Test(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.dropdown = wx.ComboBox(parent=self, pos=(100,100), size=(150,50))
        self.dropdown.SetItems(["first", "second", "third"])

        # load in user dataManagement
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        # gets the size of the current window, so we can scale everything to it
        size = self.GetSize()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass