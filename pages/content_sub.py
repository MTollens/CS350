import wx
from pages.custom_widgets import RecipeBox as RecipeBox


class ContentScroller(wx.Panel):
    def __init__(self, parent, size=(600, 355), pos=(0, 100)):
        wx.Panel.__init__(self, parent=parent, size=size, pos=pos)#,
                                                    # style=wx.SIMPLE_BORDER)

        self.render_status = 0

        self.parent = parent

        # a neutral light gray
        self.SetBackgroundColour((120, 120, 120))

        # what page of results are we on
        self.page = 0

        # start hidden as the panels that rely on this will show it when they are called
        self.Hide()

        self.columns = 2
        self.rows = 2

        # main list of items
        self.items = [RecipeBox(self, position=(10, 10)), RecipeBox(self, position=(260, 10))]

        self.Bind(wx.EVT_IDLE, self.__on_idle)

    # takes into consideration the page, and how many tiles are on screen
    def reload_recipes(self):
        # status = True means that there are still search results to be shown
        # status = False means that we have shown all the search results
        status = True

        # if we can only fit one thing on the screen, then it will pretty much be unseable
        if len(self.items) == 1:
            self.items[0].error("Window too small!")
            return 0

        # if we only have two items then we are going to forgo the "previous" button
        # in favor of having 1 recipe on screen and "next page"
        elif len(self.items) == 2:
            # this is where the data gets loaded from the database
            #self.items[0].fill(self.__request(1))
            # for now it is dummy
            self.items[0].dummy()
            self.items[1].next_page(status)
        elif len(self.items) > 2:
            # now that we know we can fit all the icons we can just use an algorithm, instead of hardcoding
            for x in self.items:
                # the x-1 here is to account for the previous button
                # remember to check if the page we are on enable the previous button or not
                # self.items[x].fill(self.__request(x))
                self.items[0].dummy()
                x.dummy()
            if self.page > 0:
                self.items[0].previous_page()
            self.items[-1].next_page(status)
        else:
            print(len(self.items))


    # called externally to resize the page when the window resizes, shouldnt need to call this
    def resize_main(self, event=None, size_external=None, position_external=None):
        self.render_status = 0
        if size_external:
            self.SetSize(size_external)

        if position_external:
            self.SetPosition(position_external)
            self.page = 0
            self.Hide()
            self.Show()

        # self.update_widgets()

    # def update_widgets(self):
    #     size = self.GetSize()
    #     # calculate the number of rows and columns that we can fit
    #     # 210 and 270 are the default size of the widget, with 10 for spacing on every side
    #     self.columns = int((size[0]-10)/210)
    #     self.rows = int((size[1]-10)/270)
    #
    #     # we must always have at least one object
    #     # so we correct for somehow getting a negative or 0
    #     if self.columns <= 0:
    #         self.columns = 1
    #     if self.rows <= 0:
    #         self.columns = 1
    #
    #     # if we can fit more items than we currently have, then add more until it is correct
    #     if len(self.items) < (self.columns * self.rows):
    #         while len(self.items) < (self.columns * self.rows):
    #             self.items.append(RecipeBox(self, position=(0, 0)))
    #
    #     # alternatively remove items until we dont have too many
    #     elif len(self.items) > (self.columns * self.rows):
    #         while len(self.items) > (self.columns * self.rows):
    #             del self.items[-1]
    #
    #
    #     # for each column
    #     for x in range(0, self.columns):
    #         # for each row
    #         for y in range(0, self.rows):
    #             # reposition every widget
    #             self.items[x*self.rows+y].reposition((x*210 + 10, y*270+10))
    #
    #     # print("expected items: {}".format(self.columns * self.rows))
    #     # print("actual items: {}".format(len(self.items)))
    #     # print(size)
    #
    #     # now that the layout has (possibly) changed, we need to fix the stuff on the tiles
    #     # for x in self.items:
    #     #     x.dummy()
    #     self.reload_recipes()
    #

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
        # make a request here
        # send the following number to the database handler so it knows which result of its search we are on
        position = self.page * self.rows * self.columns + item
        pass

    def __on_idle(self, event=None):
        # if we are not visible then we are not going to waste background processing
        if not self.IsShown():
            return 0

        size = self.GetSize()

        # reload all the widgets
        if self.render_status == -1:
            self.items = [RecipeBox(self, position=(10,10))]
            self.render_status = 0

        # regenerate metadata
        elif self.render_status == 0:
            # calculate the number of rows and columns that we can fit
            # 210 and 270 are the default size of the widget, with 10 for spacing on every side
            self.columns = int((size[0] - 10) / 210)
            self.rows = int((size[1] - 10) / 270)

            # we must always have at least one object
            # so we correct for somehow getting a negative or 0
            if self.columns <= 0:
                self.columns = 1
            if self.rows <= 0:
                self.columns = 1
            self.render_status = 1

        # add new ones
        elif self.render_status == 1:
            self.render_status = 2
            # if we can fit more items than we currently have, then add more until it is correct
            # if len(self.items) < (self.columns * self.rows):
            #         self.items.append(RecipeBox(self, position=(10, 10)))
            # else:
            #     self.render_status = 2

        # delete extras
        elif self.render_status == 2:
            # alternatively remove items until we dont have too many
            if len(self.items) > (self.columns * self.rows):
                    del self.items[-1]
            else:
                self.render_status = 3

        # move each piece
        elif self.render_status == 3:
            counter = 0
            # for each column
            for x in range(0, self.columns):
                # for each row
                for y in range(0, self.rows):
                    # reposition every widget

                    # self.items[x * self.rows + y].reposition((x * 210 + 10, y * 270 + 10))
                    self.items[counter].reposition((x * 210 + 10, y * 270 + 10))
                    counter += 1
                    if counter == 2:
                        self.render_status = 4
                        return 0
            self.render_status = 4

        elif self.render_status == 4:
            self.reload_recipes()
            self.render_status = 5

        # print(len(self.items))

