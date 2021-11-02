import wx

# a very simple sign in page
class Sign(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Username_title = wx.StaticText(parent=self, label="Username:", pos=(75, 80), size=(100, 30))
        self.Password_title = wx.StaticText(parent=self, label="Password:", pos=(75, 120), size=(100, 30))
        self.Username = wx.TextCtrl(parent=self, pos=(175, 75), size=(200, 30))
        # the style = wx.TE_PASSWORD is what makes the password field be dots instead of characters
        self.Password = wx.TextCtrl(parent=self, pos=(175, 115), size=(200, 30), style=wx.TE_PASSWORD)

        self.box = wx.StaticBox(parent=self, pos=(50, 50), size=(400, 220))

        # if cancel is chosen, then we just go back to the account page
        self.Cancel = wx.Button(parent=self, label="Cancel", pos=(0, 0), size=(100, 50))
        self.Cancel.Bind(wx.EVT_BUTTON, parent.setAccount)

        # if submit is chosen then we will send some DataManagement to the user class to validate the login
        self.Confirm = wx.Button(parent=self, label="Login", pos=(0, 0), size=(100, 50))
        self.Confirm.Bind(wx.EVT_BUTTON, self.example)

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()
        self.Confirm.SetPosition((size[0] - 150, size[1] - 70))
        self.Cancel.SetPosition((size[0] - 300, size[1] - 70))

    # runs the example, which loads the dummy user demo DataManagement
    # we also need to remember to switch panels as well as send the DataManagement
    def example(self, event=None):
        self.parent.user.example_login()
        self.parent.setAccount()

    def submit_credentials(self):
        pass



    def update_user(self):
        pass


