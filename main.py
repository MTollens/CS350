#the main UI library
import wx
# the panels from the Pages sub directory
from Pages import sign_in as sn, settings as st, search as sh, pantry as pn, homepage as hp, execution as ex, \
    creation as cr, account as ac

# the user class that handles interactions between the data and the UI
import user as user

# main class, contains all the others
class Frame(wx.Frame):
    def __init__(self):
        # creates window using system API
        wx.Frame.__init__(self, None, wx.ID_ANY, "RecipeBuddy", size=(600, 500))
        # the user is instantiated inside the main because all the other panels need to reference it, and main is the parent
        self.user = user.User()

        # panels list, do not change the order of this list, or all the panels will reference the wrong ones
        self.__panels = [hp.Homepage(self), ac.Account(self), sn.Sign(self), pn.Pantry(self), st.Settings(self),
                       sh.Search(self), cr.Creation(self), ex.Execution(self)]

        # used to manage the back button, as well as to know what panel we should be on
        self.current_panel = 0
        self.previous_panel = 0

        # specify that they should all have the same resize properties
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        for x in self.__panels:
            # apply the property to the panels
            self.sizer.Add(x, 1, wx.EXPAND)
            # start all of them hidden
            x.Hide()

        # set the homepage panel to be able to internally handle its own resize events
        self.__panels[self.current_panel].Bind(wx.EVT_SIZE, self.__panels[self.current_panel].resize_main)
        # show the homepage panel
        self.__panels[self.current_panel].Show()
        # apply the properties to the frame as a whole
        self.SetSizer(self.sizer)

        #handles setting the icon for the window, just change the file location to change the image
        # referring to the image in the top left of the window
        # code from: https://nedbatchelder.com/blog/200501/nice_windows_icons_with_wxpython.html
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("resources/Raindropmemory-Merry-Go-Round-Doc.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)


    # for setting an arbitrary panel as the main panel not to be used directly
    def __setPanel_visible(self, panel):
        # panel switching referenced from:
        # https://stackoverflow.com/questions/8810514/change-panel-with-button-wxpython
        self.__panels[panel].update_user()
        self.previous_panel = self.current_panel
        self.current_panel = panel
        # size = self.GetSize()
        for x in range(len(self.__panels)):
            self.__panels[x].Hide()
        self.__panels[panel].Bind(wx.EVT_SIZE, self.__panels[panel].resize_main)
        self.__panels[panel].Show()
        self.Layout()


    # performs the function of a back button
    def setPrevious(self, event=None):
        panel = self.previous_panel
        self.__setPanel_visible(panel)
        self.previous_panel = 0

    # for setting a specific panel, mostly to simplify use from within a panel
    # to avoid needing to send arguments, and to simplify the process for developing
    def setAccount(self, event=None):
        panel = 1
        self.__setPanel_visible(panel)

    def setHomepage(self, event=None):
        panel = 0
        self.__setPanel_visible(panel)

    def setSignin(self, event=None):
        panel = 2
        self.__setPanel_visible(panel)

    def setPantry(self, event=None):
        panel = 3
        self.__setPanel_visible(panel)

    def setSettings(self, event=None):
        panel = 4
        self.__setPanel_visible(panel)

    def setSearch(self, event=None):
        panel = 5
        self.__setPanel_visible(panel)

    def setCreation(self, event=None):
        panel = 6
        self.__setPanel_visible(panel)

    def setExecution(self, event=None):
        panel = 7
        self.__setPanel_visible(panel)

    #end of panel selectors



# removes newlines from a given text
# takes in [string] >> "hello,\n welcome!"
# returns [string] >> "hello, welcome!"
def textclean(text):
    assert isinstance(text, str), "you must pass a string"
    text = text.replace("\n", "")
    return text


# when passed a string, will wrap the text after the given number of characters
# used for text boxes that dont wrap for if you need it.
# takes in [string] >> the text to be wrapped
# takes in [int] >> the number of characters per line before it starts trying to wrap
# returns [string] >> formatted
# looks for a space and inserts a \n when the character limit is reached
def wordwrap(text, chars):
    assert isinstance(text, str), "you must pass a string"
    counter = 0
    new = ""
    for x in range(0, len(text)):
        if (counter > chars) and (text[x] == " "):
            new = new + '\n '
            counter = 0
        else:
            new = new + text[x]
            counter += 1
    return new


# this is the python equivelant of "int main()"
if __name__ == "__main__":
    #create the app
    app = wx.App(False)

    #create the window that we actually use
    frame = Frame()
    #show the frame
    frame.Show()
    # start the app
    app.MainLoop()