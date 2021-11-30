import wx
import os


# not yet implemented in any way
# saving this one for someone else to do, so I dont do all the UI

class Creation(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # if this is set to true, then the page will ask you if you intended to leave, and that it will destroy progress
        # may not be needed, we shall see if it is an issue
        self.modifications = False

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.page_name = wx.StaticText(parent=self, label="Recipe Editor", pos=(120, 20))


        # UI implementation here:
        self.Title_box = wx.TextCtrl(parent=self, pos=(60,60), size=(200,30))
        self.Title_box.SetHint("Title")

        self.MakesFor = wx.TextCtrl(parent=self, pos=(60,100), size=(200,30))
        self.MakesFor.SetHint("How many servings?")

        self.Preptime = wx.TextCtrl(parent=self, pos=(60, 140), size=(200,30))
        self.Preptime.SetHint("How long to prepare?")

        self.Ingredient_type_selector = wx.ComboBox(parent=self, pos=(50, 200), size=(200,40))
        self.Ingredient_type_selector.SetHint("select type")
        self.Ingredient_selector = wx.ComboBox(parent=self, pos=(50, 250), size=(200,40))
        self.Ingredient_selector.SetHint("select ingredient")
        self.Ingredient_list = wx.StaticText(parent=self, pos=(50, 360), label="ingredients:")

        self.Add_ingredient = wx.Button(parent=self, pos=(50, 300), label="Add Ingredient")

        self.image = wx.Button(self, pos=(300,50), size=(150, 150), label="add image")
        self.image.Bind(wx.EVT_BUTTON, self.image_select)
        self.image_path = ""

        self.Instructions_list = wx.TextCtrl(parent=self, pos=(300, 220), size=(260, 220), style=wx.TE_MULTILINE)
        self.Add_timer = wx.Button(parent=self, label="add Timer", pos=(150, 360))

        # self.Tags = wx.TextCtrl(parent=self, pos=(50, 350))
        # self.Tags.SetHint(hint="add as many or as few tags as you like \n seperate tags with a comma!")



        # load in user dataManagement
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass

    def image_select(self, event=None):
        # code referenced from https://www.programcreek.com/python/example/3163/wx.FileDialog
        filename = "/home/matt/PycharmProjects/CS350/resources/fishandchips.jpg"
        # TODO clean this up, i dont understand it and it doesnt perfom completly correct
        defDir, defFile = '', ''
        if filename is not None:
            defDir, defFile = os.path.split(filename)

        dlg = wx.FileDialog(self,
                            'Open File',
                            defDir, defFile,
                            'rfmon files (*.rfmon)|*.rfmon',
                            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_CANCEL:
            return

        if os.path.exists(dlg.GetPath()):
            self.image.SetBitmap(self.load_image(dlg.GetPath(), self.image.GetSize()))
            self.image_path = dlg.GetPath()
            self.image.SetLabel("")
        else:
            self.image.SetLabel("Image couldnt\nbe loaded")

    # load file bitmap and return it as a bitmap object
    # for use with the "image" object
    def load_image(self, filename, size):
        # TODO add file extension checking
        temp = 0
        try:
            temp = wx.Bitmap(filename, wx.BITMAP_TYPE_ANY)
            temp = self.scale_bitmap(temp, size[0], size[1])
        except:
            temp = wx.Bitmap("resources/nofile.png", wx.BITMAP_TYPE_ANY)
            temp = self.scale_bitmap(temp, size[0], size[1])

        return temp

    # scales bitmap, shouldnt need to be touched at all
    def scale_bitmap(self, bitmap, width, height):
        image = wx.Bitmap.ConvertToImage(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result
