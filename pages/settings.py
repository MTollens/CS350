import wx

# Depreciated
"""

This Class Is no longer used for anything

"""
# Depreciated



class Settings(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Status = wx.StaticText(parent=self, pos=(50,50), size=(200,50))

        self.changes = False
        self.metric = self.parent.user.settings["Metric"]
        self.Units = wx.Button(parent=self, label="Metric", pos=(50, 100), size=(100, 50))
        self.Units.Bind(wx.EVT_BUTTON, self.change_units)
        self.update_units()

        self.Cancel = wx.Button(parent=self, label="Cancel", pos=(0, 0), size=(100, 50))
        self.Cancel.Bind(wx.EVT_BUTTON, self.discard_changes)

        self.Confirm = wx.Button(parent=self, label="Confirm", pos=(0, 0), size=(100, 50))
        self.Confirm.Bind(wx.EVT_BUTTON, self.commit_changes)
        self.Confirm.Disable()

        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()
        self.Confirm.SetPosition((size[0] - 150, size[1] - 70))
        self.Cancel.SetPosition((size[0] - 300, size[1] - 70))

    def change_units(self, event=None):
        self.temp_changes()
        self.metric = not(self.metric)
        self.update_units()

    # converts true false to Metric / Imperial
    def update_units(self):
        if self.metric:
            self.Units.SetLabel("Metric")
        else:
            self.Units.SetLabel("Imperial")

    # enables the save changes button
    def temp_changes(self):
        self.changes = True
        self.Confirm.Enable()

    def discard_changes(self, event=None):
        self.changes = False
        self.Confirm.Disable()
        self.parent.setHomepage()

    def commit_changes(self, event=None):
        self.parent.setHomepage()
        self.changes = False
        self.Confirm.Disable()

    def update_user(self):
        self.Status.SetLabel("Settings for user: {}".format(self.parent.user.username))
        self.metric = self.parent.user.settings["Metric"]
        self.update_units()

    def debug(self, event=None):
        print("being stopped by debug process")
        print("NOW!")