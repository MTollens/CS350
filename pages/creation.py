import wx
import os
from resources import lists
from pages import custom_widgets as cw


# not yet implemented in any way
# saving this one for someone else to do, so I dont do all the UI

class Creation(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.sub = 0

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.page_name = wx.StaticText(parent=self, label="Recipe Editor", pos=(70, 50))

        self.image = wx.Button(self, pos=(60,80), size=(150, 150), label="add image")
        self.image.Bind(wx.EVT_BUTTON, self.image_select)
        self.image_path = ""

        # UI implementation here:
        self.Title_box = wx.TextCtrl(parent=self, pos=(60, 240), size=(200,30))
        self.Title_box.SetHint("Title")

        self.MakesFor = wx.TextCtrl(parent=self, pos=(60, 280), size=(200,30))
        self.MakesFor.SetHint("How many servings?")

        self.Preptime = wx.TextCtrl(parent=self, pos=(60, 320), size=(200,30))
        self.Preptime.SetHint("How long to prepare?")

        self.ingredients_sub = wx.Button(self, pos=(60, 370), size=(150,40), label="Edit Ingredients")
        self.instructions_sub = wx.Button(self, pos=(60, 420), size=(150, 40), label="Edit Instructions")
        self.tags_sub = wx.Button(self, pos=(60, 470), size=(150, 40), label="Edit Tags")

        # end of STATIC UI elements

        self.ingredients_category_selector = cw.PromptingComboBox(self, choices=list(lists.all.keys()))
        self.ingredients_category_selector.SetPosition((300, 80))
        self.ingredients_category_selector.SetSize((150, 40))
        self.ingredients_category_selector.SetHint("Category")

        self.ingredients_item_selector = cw.PromptingComboBox(self, choices=[])
        self.ingredients_item_selector.SetPosition((500, 80))
        self.ingredients_item_selector.SetSize((150, 40))
        self.ingredients_item_selector.SetHint("Ingredient")


        # self.ingredients_current_clear = wx.Button(self, pos=(300, 80), size=(75, 40), label="clear")

        # self.Ingredient_type_selector = wx.ComboBox(parent=self, pos=(50, 200), size=(200,40))
        # self.Ingredient_type_selector.SetHint("select type")
        # self.Ingredient_type_selector.SetItems(list(lists.all.keys()))
        # self.Ingredient_type_selector.Bind(wx.EVT_COMBOBOX_CLOSEUP, self.type_selector_autofill)

        # self.Ingredient_selector = wx.ComboBox(parent=self, pos=(50, 250), size=(200,40))
        # self.Ingredient_selector.SetHint("select ingredient")
        # self.Ingredient_selector.SetItems([""])

        # self.Ingredient_list = wx.StaticText(parent=self, pos=(50, 360), label="ingredients:")
        #
        # self.Add_ingredient = wx.Button(parent=self, pos=(50, 300), label="Add Ingredient")


        # self.Instructions_list = wx.TextCtrl(parent=self, pos=(300, 220), size=(260, 220), style=wx.TE_MULTILINE)
        # self.Add_timer = wx.Button(parent=self, label="add Timer", pos=(150, 360))

        # self.Tags = wx.TextCtrl(parent=self, pos=(50, 350))
        # self.Tags.SetHint(hint="add as many or as few tags as you like \n seperate tags with a comma!")

        # load in user dataManagement
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()

    # for updating the subcontents views
    def update_subs(self):
        if self.sub == 0:
            pass

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        pass

    def image_select(self, event=None):
        # code referenced from https://www.programcreek.com/python/example/3163/wx.FileDialog
        filename = "/home/matt/PycharmProjects/CS350/resources/fishandchips.jpg"

        # unsure about what this does, other than set the starting DIR for the selector
        defDir, defFile = '', ''
        if filename is not None:
            defDir, defFile = os.path.split(filename)

        # list of file types that we will intentionally support, not sure about GIF, but we can change it later
        acceptable_file_types = "BMP and GIF files (*.bmp;*.gif)|*.bmp;*.gif"+\
                                "|PNG files (*.png)|*.png"+\
                                "|Jpeg files (*.jpg;*.jpeg)|*.jpg;*.jpeg"

        # create the file dialogue object
        dlg = wx.FileDialog(self,
                            'Open File',
                            defDir, defFile,
                            acceptable_file_types,
                            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        # slg.showmodal shows the screen that the user sees, and if the result is that they pressed cancel, then return 0
        if dlg.ShowModal() == wx.ID_CANCEL:
            return 0
        # since the user did not press cancel they must have selected a file

        # check if the image exists in the system
        if os.path.exists(dlg.GetPath()):
            self.image.SetBitmap(self.load_image(dlg.GetPath(), self.image.GetSize()))
            self.image_path = dlg.GetPath()
            self.image.SetLabel("")
        else:
            self.image.SetLabel("Image couldnt\nbe loaded")

    # load file bitmap and return it as a bitmap object
    # for use with the "image" object
    def load_image(self, filename, size):
        # file extension checking not required, because a failure mode is prepared
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

    # this is where changes are commited, data that was entered on the page is put into a recipe class
    # and the class is passed to the storage handler
    def finish_recipe(self, event=None):
        # image path
        # ingredients
        # instructions
        # tags
        # title
        # serving
        # etc...
        # see recipe class

        # return recipe
        pass

    # load the recipe from a recipe class for editing purposes
    def load_recipe(self, recipe):
        pass

    def edit_tags(self, event=None):
        pass

    def edit_ingredients(self, event=None):
        pass

    def edit_instructions(self, event=None):
        pass

    def ingredients_category_chosen(self):
        val = self.ingredients_category_selector.GetValue()
        # if val in list(lists.all.keys()):
        self.ingredients_item_selector.SetItems(lists.all[val])
        # else:
        #     # self.ingredients_item_selector.SetValue("")
        #     self.ingredients_item_selector.SetItems([])