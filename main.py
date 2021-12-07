#the main UI library
import wx
import wx.lib.scrolledpanel
# the panels from the pages sub directory
from pages import sign_in as sn, search as sh, pantry as pn, homepage as hp, execution as ex, \
    creation as cr, account as ac, test_page as tt, help as hl, content_reworked as cs

# the user class that handles interactions between the dataManagement and the UI
from dataManagement import user as user
from dataManagement import recipe as RCP


# main class, contains all the others
class Frame(wx.Frame):
    def __init__(self):
        # creates window using system API
        wx.Frame.__init__(self, None, wx.ID_ANY, "RecipeBuddy", size=(1000, 800))
        # the user is instantiated inside the main because all the other panels need to reference it, and main is the parent
        self.user = user.User()

        # important that it is declared before self.__panels
        # secondary panel that handles the content view, is rendered on top of specified panels
        self.__ContentScroller = cs.ContentScroller(self)

        # panels list, do not change the order of this list, or all the panels will reference the wrong ones
        self.__panels = [hp.Homepage(self), ac.Account(self), sn.Sign(self), pn.Pantry(self), sh.Search(self),
                         cr.Creation(self), ex.Execution(self), tt.Test(self), hl.Help(self)]

        self.__ContentScroller.Hide()
        # self.__ContentScroller.Bind(wx.EVT_SIZE, self.__ContentScroller.resize_main)

        # list of panels that should show the ContentScroller
        self.secondary = [0, 4]

        # defaults to True, will be changed to false as soon as the first sign in page is exited
        # alters behaviour concerning the account page, but only on the first interaction
        self.first_sign_in = True


        # used to manage the back button, as well as to know what panel we should be on
        self.current_panel = 2
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
        if panel in self.secondary:
            self.__ContentScroller.Show()
        else:
            self.__ContentScroller.Hide()
        self.Layout()

    # used to resize the content window on panels that utilize it
    def resize_secondary(self, size, position):
        self.__ContentScroller.resize_main(None, size, position)

    # this allows the reuse of the search function that the search page uses, so the homepage code isnt unique
    def anon_search(self, keyword, tags=None):
        self.user.current_search_tags = tags
        self.user.search(keyword)
        self.setSearch()

    # can be called from anywhere, just pass the recipe, will automatically redirect to the proper page
    def open_recipe(self, recipe):
        assert isinstance(recipe, RCP.Recipe), "was not passed an instance of recipe class. was: {}".format(type(recipe))
        self.user.open_recipe = recipe
        self.setExecution()

    # performs the function of a back button
    def setPrevious(self, event=None):
        panel = self.previous_panel
        if panel == 2:
            panel = 0
        self.__setPanel_visible(panel)
        self.previous_panel = 0

    # for setting a specific panel, mostly to simplify use from within a panel
    # to avoid needing to send arguments, and to simplify the process for developing
    def setHomepage(self, event=None):
        self.first_sign_in = False
        panel = 0
        self.user.current_search = ""
        self.user.current_search_tags = []
        self.__setPanel_visible(panel)

    def setAccount(self, event=None):
        # by default redirect to the sign in page, as the user should not be able to view the account witout being signed in
        panel = 2
        # if the user has signed in then they can redirect to the proper page
        if self.user.signed_in:
            panel = 1
        # if the user has just signed in for the fist time this session then they should actually be redirected to the
        # homepage
        if self.first_sign_in:
            panel = 0
            self.first_sign_in = False
        self.__setPanel_visible(panel)

    def setSignin(self, event=None):
        panel = 2
        self.__setPanel_visible(panel)

    def setPantry(self, event=None):
        panel = 3
        self.__setPanel_visible(panel)

    def setSettings(self, event=None):
        # settings panel was depreciated, will send to account
        panel = 1
        self.__setPanel_visible(panel)

    def setSearch(self, event=None):
        panel = 4
        self.__setPanel_visible(panel)

    def setCreation(self, event=None):
        panel = 5
        if not self.user.signed_in:
            panel = 2
        self.__setPanel_visible(panel)

    def setExecution(self, event=None):
        panel = 6
        if not self.user.signed_in:
            panel = 2
        self.__setPanel_visible(panel)

    def setTest(self, event=None):
        panel = 7
        self.__setPanel_visible(panel)

    def setHelp(self, event=None):
        panel = 8
        self.__setPanel_visible(panel)

    def setEdit(self, event=None):
        panel = 5
        if not self.user.signed_in:
            panel = 2
        else:
            self.__panels[panel].load_recipe()
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