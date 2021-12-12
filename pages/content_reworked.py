import wx
from dataManagement import recipe
from dataManagement import common_utils


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

        self.sizer = wx.BoxSizer()
        self.image_size = (200, 200)
        self.info_size = (200, 50)

        # left
        self.left_image = wx.BitmapButton(self, size=self.image_size)
        # self.left_image.SetLabel("left_image")
        self.left_image.Bind(wx.EVT_BUTTON, self.left_pressed)
        self.sizer.Add(self.left_image, flag=wx.ALL, border=5)

        self.left_info = wx.Button(self, size=self.info_size)
        self.left_info.SetLabel("left_info")
        self.left_info.Bind(wx.EVT_BUTTON, self.left_pressed)
        self.sizer.Add(self.left_info, flag=wx.ALL, border=5)
        self.left_recipe = recipe.Recipe("dummy")

        # mid
        self.mid_image = wx.BitmapButton(self, size=self.image_size)
        # self.mid_image.SetLabel("mid_image")
        self.mid_image.Bind(wx.EVT_BUTTON, self.mid_pressed)
        self.sizer.Add(self.mid_image, flag=wx.ALL, border=5)

        self.mid_info = wx.Button(self, size=self.info_size)
        self.mid_info.SetLabel("mid_info")
        self.mid_info.Bind(wx.EVT_BUTTON, self.mid_pressed)
        self.sizer.Add(self.mid_info, flag=wx.ALL, border=5)
        self.mid_recipe = recipe.Recipe("dummy")

        # right
        self.right_image = wx.BitmapButton(self, size=self.image_size)
        # self.right_image.SetLabel("right_image")
        self.right_image.Bind(wx.EVT_BUTTON, self.right_pressed)
        self.sizer.Add(self.right_image, flag=wx.ALL, border=5)

        self.right_info = wx.Button(self, size=self.info_size)
        self.right_info.SetLabel("right_info")
        self.right_info.Bind(wx.EVT_BUTTON, self.right_pressed)
        self.sizer.Add(self.right_info, flag=wx.ALL, border=5)
        self.right_recipe = recipe.Recipe("dummy")

        # navigation
        self.previous = wx.Button(self, size=self.info_size)
        self.previous.SetLabel("<<<   Previous")
        self.sizer.Add(self.previous, flag=wx.ALL, border=5)
        self.previous.Bind(wx.EVT_BUTTON, self.previous_pressed)

        self.next = wx.Button(self, size=self.info_size)
        self.next.SetLabel("Next   >>>")
        self.sizer.Add(self.next, flag=wx.ALL, border=5)
        self.next.Bind(wx.EVT_BUTTON, self.next_pressed)

        self.current_page = wx.StaticText(self, size=self.info_size, style=wx.ALIGN_CENTRE_HORIZONTAL)
        self.current_page.SetLabel("Page 1")
        self.sizer.Add(self.current_page, flag=wx.ALL, border=5)

        self.SetSizer(self.sizer)

        self.reload_recipes()

    # takes into consideration the page, and how many tiles are on screen
    def reload_recipes(self):
        if self.page < 0:
            self.page = 0

        self.current_page.SetLabel("Page {}".format(self.page+1))
        # left panel starts at 1
        item1 = recipe.Recipe("dummy").no_more_results()
        item2 = recipe.Recipe("dummy").no_more_results()
        item3 = recipe.Recipe("dummy").no_more_results()

        status, item1 = self.__request(self.page * 3 + 1)

        # Check if search results found
        if not item1:
            item1 = recipe.Recipe("dummy").no_more_results()
            self.current_page.SetLabel("No results found!")

        self.left_image.SetBitmap(common_utils.load_image(item1.image, self.left_image.GetSize()))
        self.left_info.SetLabel(item1.generate_description(64))
        self.left_recipe = item1

        # if the first status check returned true, then we can request another
        if status:
            status, item2 = self.__request(self.page * 3 + 2)
        # if the second status request returned true as well, then all three get real values
        if status:
            status, item3 = self.__request(self.page * 3 + 3)


        self.mid_image.SetBitmap(common_utils.load_image(item2.image, self.mid_image.GetSize()))
        self.mid_info.SetLabel(item2.generate_description(64))
        self.mid_recipe = item2

        self.right_image.SetBitmap(common_utils.load_image(item3.image, self.right_image.GetSize()))
        self.right_info.SetLabel(item3.generate_description(64))
        self.right_recipe = item3


        # if all status checks returned true then we can show it
        if status:
            self.next.Show()
        # if we recieved a false status at any point then we should not show the next button
        else:
            self.next.Hide()

        # previous button should not show up unless we are on page > 0
        if self.page == 0:
            self.previous.Hide()
        else:
            self.previous.Show()

    def update_user(self, event=None):
        if not self.parent.first_sign_in:
            self.reload_recipes()

    # makes a request to the database and returns a recipe and a status report
    # status, recipe = self.__request(item_number)
    # returns TRUE as the status report, if there remain some results to display
    # returns FALSE if there are no more results, the returned recipe is tha last one available
    def __request(self, item):
        # # make a request here
        # # send the following number to the database handler so it knows which result of its search we are on
        # Handle homepage request. Currently based on highest executions
        if self.parent.user.current_search == "":
            results = self.parent.user.load_featured_recipes()
            isntLast = item != len(results)
            if item <= len(results):
                return isntLast, results[item-1]
            else:
                # i forgot, you dont need to pass a recipe if you are returning false
                return isntLast, None
        # TODO Implement this properly to handle searching
        else:
            results = self.parent.user.load_searched_recipes()
            isntLast = item != len(results)
            if item <= len(results):
                return isntLast, results[item - 1]
            else:
                # i forgot, you dont need to pass a recipe if you are returning false
                return False, None

        # can return invalid if applicable

    def resize_main(self, event=None, size_external=None, position_external=None):
        if size_external:
            self.SetSize(size_external)

        if position_external:
            self.SetPosition(position_external)
            self.page = 0
            # self.Hide()
            # self.Show()

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
        self.current_page.SetSize(self.info_size)
        self.current_page.SetPosition((self.image_size[0]+10, self.image_size[1]+self.info_size[1]+20))
        self.next.SetSize(self.info_size)
        self.next.SetPosition((2*(self.image_size[0]+10), self.image_size[1]+self.info_size[1]+20))

    # button for either of the left tile buttons
    def left_pressed(self, event=None):
        # print("left pressed")
        if self.left_recipe.title not in dont_open:
            self.open_recipe(self.left_recipe)

    def mid_pressed(self, event=None):
        # print("mid pressed")
        if self.mid_recipe.title not in dont_open:
            self.open_recipe(self.mid_recipe)

    def right_pressed(self, event=None):
        # print("right pressed")
        if self.right_recipe.title not in dont_open:
            self.open_recipe(self.right_recipe)

    def previous_pressed(self, event=None):
        if self.page > 0:
            self.page -= 1
        self.reload_recipes()

    def next_pressed(self, event=None):
        self.page += 1
        self.reload_recipes()

    def open_recipe(self, recipe):
        # validation (if needed) should be performed in the main class at the function below
        self.parent.open_recipe(recipe)



empty = [" ","",None]
dont_open = ["INVALID", "", " ", "end of results", None]

