import wx
import wx.adv
import os

# this one gets run when the file is run externally
file = "resources/alert_chime.wav"

# this file is for a very simple WX app that will run when the timer is done, and play a sound
class Frame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos,
                         style=wx.STAY_ON_TOP|(wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)),
                         size=(300,200))
        self.parent = parent
        self.Panel = Main(self)


class Main(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        #self.now = datetime.datetime.now()

        self.title = wx.StaticText(self, id=wx.ID_ANY, label="Recipe Timer Done!", pos=(75, 50), style=wx.TE_CENTER)
        self.button = wx.Button(self, pos=(200, 120), size=(75,30), label="Ok")
        self.button.Bind(wx.EVT_BUTTON, quit)
        # print("file exists?")
        print(os.path.exists(file))
        # print(os.getcwd())
        wx.adv.Sound(file).Play(flags=wx.adv.SOUND_ASYNC|wx.adv.SOUND_LOOP)



def main():
    print(os.getcwd())
    app = wx.App(False)
    frame = Frame(parent=None, title="Timer Done", pos=(500, 500))
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    # file = "../resources/alert_chime.wav"
    main()