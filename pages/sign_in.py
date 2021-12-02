import wx

# a very simple sign in page
class Sign(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Username_title = wx.StaticText(parent=self, label="Username:", pos=(75, 80), size=(100, 30))
        self.Password_title = wx.StaticText(parent=self, label="Password:", pos=(75, 120), size=(100, 30))
        self.Confirm_title = wx.StaticText(parent=self, label=" Confirm:", pos=(75, 156), size=(100, 30))
        self.Confirm_title.Hide()

        self.Username = wx.TextCtrl(parent=self, pos=(175, 75), size=(200, 30))
        # the style = wx.TE_PASSWORD is what makes the password field be dots instead of characters
        self.Password = wx.TextCtrl(parent=self, pos=(175, 115), size=(200, 30), style=wx.TE_PASSWORD)
        self.Confirm_Password = wx.TextCtrl(parent=self, pos=(175, 155), size=(200, 30), style=wx.TE_PASSWORD)
        self.Confirm_Password.Hide()

        self.box = wx.StaticBox(parent=self, pos=(50, 50), size=(400, 220))

        # if cancel is chosen, then we just go back to the account page
        self.Cancel = wx.Button(parent=self, label="Cancel", pos=(80, 210), size=(100, 50))
        self.Cancel.Bind(wx.EVT_BUTTON, self.cancel)

        self.Guest = wx.Button(parent=self, label="Guest", pos=(200, 210), size=(100, 50))
        self.Guest.Bind(wx.EVT_BUTTON, self.guest)

        # if submit is chosen then we will send some dataManagement to the user class to validate the login
        self.Confirm = wx.Button(parent=self, label="Login", pos=(320, 210), size=(100, 50))
        self.Confirm.Bind(wx.EVT_BUTTON, self.example)

        self.Create_account = wx.Button(parent=self, label="Create account", pos=(500, 60), size=(160, 50))
        self.Create_account.Bind(wx.EVT_BUTTON, self.account_create)

        self.Submit = wx.Button(parent=self, label="Submit", pos=(500, 120), size=(160, 50))
        self.Submit.Bind(wx.EVT_BUTTON, self.submit)
        self.Submit.Hide()

        self.error = wx.StaticText(parent=self, label="", pos=(500, 180))

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()


    # runs the example, which loads the dummy user demo dataManagement
    # we also need to remember to switch panels as well as send the dataManagement
    def example(self, event=None):
        self.parent.user.example_login()
        self.parent.setAccount()

    def submit_credentials(self):
        pass

    def update_user(self):
        pass

    def account_create(self, event=None):
        self.clear_inputs()
        self.Confirm.Hide()
        self.Confirm_Password.Show()
        self.Confirm_title.Show()
        self.Submit.Show()
        self.Create_account.Hide()

    def submit(self, event=None):
        # passwords match
        if self.Password.GetValue() != self.Confirm_Password.GetValue():
            print(self.Password.GetValue())
            print(self.Confirm_Password.GetValue())
            self.error.SetLabel("Passwords do not match")
            return 0

        # password long enough
        if len(self.Password.GetValue()) < 4:
            self.error.SetLabel("Passwords must exceed\n four characters")
            return 0

        # other password requirements

        if self.Password.GetValue() in empty:
            self.error.SetLabel("Username Invalid")
            return 0

        # if username taken
        self.return_to_default()

    def return_to_default(self):
        self.Confirm.Show()
        self.Confirm_Password.Hide()
        self.Confirm_title.Hide()
        self.Submit.Hide()
        self.Create_account.Show()
        self.clear_inputs()

    def clear_inputs(self):
        self.Password.SetValue("")
        self.Confirm_Password.SetValue("")
        self.Username.SetValue("")

    def cancel(self, event=None):
        self.return_to_default()
        self.clear_inputs()
        self.parent.setPrevious()


    def guest(self, event=None):
        self.return_to_default()
        self.clear_inputs()
        self.parent.setHomepage()


empty = [" ","",None]