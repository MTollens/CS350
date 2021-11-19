from dataManagement import recipe as rcp
import wx

# by default RecipeBox instances are 200 pixels wide, and 250 tall, (200,250)
class RecipeBox():
    #default constructor, no arguments given
    def __init__(self, parent, position=(0,0)):
        self.parent = parent
        self.position = position
        self.size = (200, 250)
        self.box = wx.StaticBox(parent=parent)
        self.make_button = wx.Button(parent=parent)
        # self.image = wx.BitmapButton()
        bmp = self.load_image("resources/nofile.png")
        bmp.SetSize(self.size)
        self.image = wx.BitmapButton(parent=parent, bitmap=bmp)

    def reposition(self, root_position):
        assert isinstance(self.image, wx.BitmapButton)
        self.box.SetPosition(self.position)
        self.box.SetSize(self.size)

        self.image.SetPosition(self.position)
        self.image.SetSize((self.size[0], self.size[1]-50))

        self.make_button.SetPosition((self.position[0], self.position[1]+self.size[1]-50))
        self.make_button.SetSize((self.size[0], 50))


    # load from a recipe class
    def fill(self, recipe):
        assert isinstance(recipe, rcp.Recipe), "must pass an instance of recipe.py - > Recipe"

    # binds both buttons to the overall function's binding
    def Bind(self, event, function):
        self.image.Bind(event, function)
        self.make_button.Bind(event, function)

    # fills the object with dummy data for testing purposes
    def dummy(self):
        title = "Baked Fish and Chips"
        rating = "(5)"
        star = "★"
        unfilled = "☆"
        rating = rating + " " + star*4 + unfilled
        temp = title[:int(self.size[0]/2)] + "\n" + rating
        self.make_button.SetLabel(temp)
        self.image.SetBitmap(self.load_image("resources/fishandchips.jpg"))

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