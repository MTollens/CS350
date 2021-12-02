from dataManagement import recipe as rcp
import wx

# by default RecipeBox instances are 200 pixels wide, and 250 tall, (200,250)
class RecipeBox(wx.Window):
    #default constructor, no arguments given
    def __init__(self, parent, position=(0,0)):
        self.size = (200, 250) # can be changed, but intended to be static
        wx.Window.__init__(self, parent=parent, pos=position, size=self.size)
        self.parent = parent
        self.position = position

        self.no_image = wx.StaticBitmap(self.parent, -1, self.scale_bitmap(wx.Image("resources/nofile.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), 200,200), self.position)
        # self.image_file = "resources/nofile.png"
        # self.no_image = self.load_image("resources/nofile.png")
        # self.no_image.SetSize(self.size)
        self.box = wx.StaticBox(parent=parent)
        self.make_button = wx.Button(parent=parent, pos=(10, 260), size=(200,50))
        self.make_button.SetLabel("<>")
        # self.image = wx.BitmapButton()

        self.image = wx.Button(self.parent, -1, size=(50,50), pos=self.position)
        self.title = "None"
        self.reposition(self.position)

        # bind the buttons
        self.rebind()
        self.image.Hide()
        self.make_button.Hide()

        self.image.Show()
        self.make_button.Show()


    def reposition(self, root_position):
        # assert isinstance(self.image, wx.BitmapButton)
        self.Hide()
        self.SetPosition(root_position)
        self.position = root_position

        self.box.SetPosition(self.position)
        self.box.SetSize(self.size)

        self.image.Hide()
        self.image.SetPosition(self.position)
        self.image.SetSize((self.size[0], self.size[1]-50))

        self.make_button.Hide()
        self.make_button.SetPosition((self.position[0], self.position[1]+self.size[1]-50))
        self.make_button.SetSize((self.size[0], 50))

        self.Show()
        self.image.Show()
        self.make_button.Show()

    def rebind(self):
        #both of the buttons do the same thing, but they dont have to
        self.make_button.Bind(wx.EVT_BUTTON, self.pressed)
        self.image.Bind(wx.EVT_BUTTON, self.pressed)

    # load from a recipe class
    def fill(self, recipe):
        assert isinstance(recipe, rcp.Recipe),"must pass an instance of recipe.py - > Recipe"
        self.title = recipe.title
        rating = "({})".format(recipe.number_of_ratings)
        temp = int(recipe.average_rating)
        assert temp <= 5, "incorrect rating value should be 0-5 got: {}".format(temp)
        star = "★"
        unfilled = "☆"

        # rating should be out of five stars
        rating = rating + " " + temp*star + unfilled*(5-temp)
        #        rating of stars  ^             ^ enough stars to get it to 5

        # the string should be [some number of characters that will fit on the button] +newline+ rating # + stars
        temp = self.title[:int(self.size[0]/2)] + "\n" + rating
        self.make_button.SetLabel(temp)

        # self.image_file = recipe.image
        try:
            self.image.SetBitmap(self.load_image(recipe.image))
        except:
            print("image '{}' not found".format(recipe.image))
            self.image.SetBitmap(self.no_image)


    # fills the object with dummy data for testing purposes
    def dummy(self):
        self.title = "Baked Fish and Chips"
        rating = "(5)"
        star = "★"
        unfilled = "☆"
        rating = rating + " " + star*4 + unfilled
        temp = self.title[:int(self.size[0]/2)] + "\n" + rating
        self.make_button.SetLabel(temp)
        # self.image_file = "resources/fishandchips.jpg"
        self.image.SetBitmap(self.load_image("resources/fishandchips.jpg"))

    # fills the boxes with information so that the status is clear when there are no results
    def empty(self):
        self.title = "End of Results"
        rating = "(0)"
        star = "★"
        unfilled = "☆"
        rating = rating + " " + unfilled*5
        temp = self.title[:int(self.size[0]/2)] + "\n" + rating
        self.make_button.SetLabel(temp)
        # self.image_file = "resources/nofile.png"
        # self.image.SetBitmap(self.load_image("resources/fishandchips.jpg"))

    # this is to give some visual feedback if there is some problem with the layout such as:
    # "window too small" <- in the case where only one tile can fit on screen, which will be hard to navigate
    def error(self, warning):
        self.empty()
        self.make_button.SetLabel(warning)

    # here the false argument means that we have actually reached the end of the results, and we should
    # not give the option of a next page
    def next_page(self, status=True):
        if status:
            self.title = "Next Page"
            self.make_button.SetLabel(self.title)
            self.image.SetBitmap(self.load_image("resources/arrow_right.png"))
            # self.image_file = "resources/arrow_right.png"
        else:
            self.empty()

    def previous_page(self):
        self.title = "Previous Page"
        self.make_button.SetLabel(self.title)
        self.image.SetBitmap(self.load_image("resources/arrow_left.png"))
        # self.image_file = "resources/arrow_left.png"

    # load file bitmap and return it as a bitmap object
    # for use with the "image" object
    def load_image(self, filename):
        temp = 0
        try:
            temp = wx.Bitmap(filename, wx.BITMAP_TYPE_ANY)
        except:
            temp = wx.Bitmap("resources/fishandchips.jpg", wx.BITMAP_TYPE_ANY)

        return self.scale_bitmap(temp, self.size[0], self.size[1] - 50)

    # scales bitmap, shouldnt need to be touched at all
    def scale_bitmap(self, bitmap, width, height):
        image = wx.Bitmap.ConvertToImage(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    def pressed(self, event=None):
        print("debug : {}".format(self.title))
        self.parent.selected(self.title)