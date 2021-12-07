import wx
import os
import subprocess



# this is a test page, just to try things out in a clean enviroment

class Test(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.button = wx.Button(self, pos=(200,200), label="alert")
        self.button.Bind(wx.EVT_BUTTON, self.send_alert)


        self.button2 = wx.Button(self, pos=(200,100), label="start timer")
        self.button2.Bind(wx.EVT_BUTTON, self.start_timer)

        self.timer_status = wx.StaticText(self, pos=(300, 100), label="")

        self.button3 = wx.Button(self, pos=(400,100), label="pause timer")
        self.button3.Bind(wx.EVT_BUTTON, self.pause_timer)
        self.button3.Hide()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        # print("running")
        # gets the size of the current window, so we can scale everything to it
        size = self.GetSize()




    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass

    def send_alert(self, event=None):
        subprocess.run(['python', 'pages/timer_done.py', 'resources/alert_chimes.wav'])
        # subprocess.run(["python3", "pages/timer_done.py"])
        # subprocess.run("pages/timer_done.py")
        # os.startfile("pages/timer_done.py")

    def start_timer(self, event=None):
        if not self.parent.user.timer_status():
            self.parent.user.start_timer(10, self.timer_status)
            self.button2.SetLabel("Stop")
            self.button3.Show()
        else:
            self.parent.user.end_timer()
            self.button2.SetLabel("Start")
            self.button3.Hide()

    def pause_timer(self, event=None):
        if self.parent.user.timer_status():
            self.parent.user.pause_timer()
            self.button3.SetLabel("resume timer")
        else:
            self.button3.SetLabel("pause timer")
            self.parent.user.timer_resume()
