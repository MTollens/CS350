#the main UI library
import wx

# main class, contains all the others
class Frame(wx.Frame):
    def __init__(self):
        # creates window using system API
        wx.Frame.__init__(self, None, wx.ID_ANY, "RecipeBuddy", size=(500, 400))



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