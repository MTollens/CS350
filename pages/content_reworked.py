import wx
from dataManagement import recipe


class ContentScroller(wx.Panel):
    def __init__(self, parent, size=(600, 355), pos=(0, 100)):
        wx.Panel.__init__(self, parent=parent, size=size, pos=pos)#,
                                                    # style=wx.SIMPLE_BORDER)

        self.render_status = 0

        self.parent = parent

        # a neutral light gray
        # self.SetBackgroundColour((120, 120, 120))

        # what page of results are we on
        self.page = 0

        self.sizer = wx.GridBagSizer()
        self.image_size = (200, 200)
        self.info_size = (200, 50)

        # left
        self.left_image = wx.BitmapButton(self, size=self.image_size)
        self.left_image.SetLabel("left_image")
        self.left_image.Bind(wx.EVT_BUTTON, self.left_pressed)
        self.sizer.Add(self.left_image, pos=(0, 0), flag=wx.ALL, border=5)

        self.left_info = wx.Button(self, size=self.info_size)
        self.left_info.SetLabel("left_info")
        self.left_info.Bind(wx.EVT_BUTTON, self.left_pressed)
        self.sizer.Add(self.left_info, pos=(1, 0), flag=wx.ALL, border=5)
        self.left_recipe = recipe.Recipe()

        # mid
        self.mid_image = wx.BitmapButton(self, size=self.image_size)
        self.mid_image.SetLabel("mid_image")
        self.mid_image.Bind(wx.EVT_BUTTON, self.mid_pressed)
        self.sizer.Add(self.mid_image, pos=(0, 1), flag=wx.ALL, border=5)

        self.mid_info = wx.Button(self, size=self.info_size)
        self.mid_info.SetLabel("mid_info")
        self.mid_info.Bind(wx.EVT_BUTTON, self.mid_pressed)
        self.sizer.Add(self.mid_info, pos=(1, 1), flag=wx.ALL, border=5)
        self.mid_recipe = recipe.Recipe()

        # right
        self.right_image = wx.BitmapButton(self, size=self.image_size)
        self.right_image.SetLabel("right_image")
        self.right_image.Bind(wx.EVT_BUTTON, self.right_pressed)
        self.sizer.Add(self.right_image, pos=(0, 2), flag=wx.ALL, border=5)

        self.right_info = wx.Button(self, size=self.info_size)
        self.right_info.SetLabel("right_info")
        self.right_info.Bind(wx.EVT_BUTTON, self.right_pressed)
        self.sizer.Add(self.right_info, pos=(1, 2), flag=wx.ALL, border=5)

        # navigation
        self.previous = wx.Button(self, size=self.info_size)
        self.previous.SetLabel("previous")
        self.sizer.Add(self.previous, pos=(2, 0), flag=wx.ALL, border=5)
        self.previous.Bind(wx.EVT_BUTTON, self.previous_pressed)

        self.next = wx.Button(self, size=self.info_size)
        self.next.SetLabel("next")
        self.sizer.Add(self.next, pos=(2, 2), flag=wx.ALL, border=5)
        self.next.Bind(wx.EVT_BUTTON, self.next_pressed)

        self.SetSizerAndFit(self.sizer)

        # start hidden as the panels that rely on this will show it when they are called
        self.Hide()

        # self.Bind(wx.EVT_IDLE, self.__on_idle)

    # takes into consideration the page, and how many tiles are on screen
    def reload_recipes(self):
        pass


    # buttons call this when a recipe has been selected
    def selected(self, title):
        print("selection made:")
        print(title)

        if title == "Next Page":
            self.page += 1
            self.reload_recipes()
            self.render_status = 1
        elif title == "Previous Page":
            if self.page > 0:
                self.page += -1
                self.reload_recipes()
            self.render_status = 1
        elif title == "End of Results":
            return 0
        else:
            pass
            # this is where the selection will be handled

    # makes a request to the database and returns a recipe and a status report
    # status, recipe = self.__request(item_number)
    def __request(self, item):
        # # make a request here
        # # send the following number to the database handler so it knows which result of its search we are on
        # position = self.page * self.rows * self.columns + item
        pass


    def resize_main(self, event=None, size_external=None, position_external=None):
        self.render_status = 0
        if size_external:
            self.SetSize(size_external)

        if position_external:
            self.SetPosition(position_external)
            self.page = 0
            self.Hide()
            self.Show()

        size = self.GetSize()

        temp = int((size[0]-50)/3)
        self.image_size = (temp, temp)
        self.info_size = (temp, int(.25*temp))

        self.left_image.SetSize(self.image_size)
        self.left_image.SetPosition((5, self.image_size[1]*0 + 5))
        self.left_info.SetSize(self.info_size)
        self.left_info.SetPosition((5, self.image_size[1]+10))

        self.mid_image.SetSize(self.image_size)
        self.mid_image.SetPosition((self.image_size[0]+10, self.image_size[0]*0 + 5))
        self.mid_info.SetSize(self.info_size)
        self.mid_info.SetPosition((self.image_size[0]+10, self.image_size[1]+10))

        self.right_image.SetSize(self.image_size)
        self.right_image.SetPosition((2*(self.image_size[0]+10), self.image_size[0]*0 + 5))
        self.right_info.SetSize(self.info_size)
        self.right_info.SetPosition((2*(self.image_size[0]+10), self.image_size[1] + 10))

        self.previous.SetSize(self.info_size)
        self.previous.SetPosition((5, self.image_size[1]+self.info_size[1]+20))
        self.next.SetSize(self.info_size)
        self.next.SetPosition((2*(self.image_size[0]+10), self.image_size[1]+self.info_size[1]+20))


    # button for either of the left tile buttons
    def left_pressed(self, event=None):
        pass

    def mid_pressed(self, event=None):
        pass

    def right_pressed(self, event=None):
        pass

    def previous_pressed(self, event=None):
        if self.page > 0:
            self.page -= 1

    def next_pressed(self, event=None):
        self.page += 1



