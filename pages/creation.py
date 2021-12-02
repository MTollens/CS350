import wx
import os
from resources import lists
from dataManagement import ingredients
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

        self.controls_box = wx.StaticBox(self, pos=(50,50), size=(220,510))

        self.page_name = wx.StaticText(parent=self, label="Recipe Editor", pos=(70, 60))

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
        self.ingredients_sub.Bind(wx.EVT_BUTTON, self.edit_ingredients)
        self.instructions_sub = wx.Button(self, pos=(60, 420), size=(150, 40), label="Edit Instructions")
        self.instructions_sub.Bind(wx.EVT_BUTTON, self.edit_instructions)
        self.tags_sub = wx.Button(self, pos=(60, 470), size=(150, 40), label="Edit Tags")
        self.tags_sub.Bind(wx.EVT_BUTTON, self.edit_tags)

        self.error_message = wx.StaticText(self, pos=(60, 520), label="")
        self.error_message.Hide()

        # end of STATIC UI elements

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # ingredients
        self.ingredients_list = ingredients.Ingredients()
        self.ingredients_title = wx.StaticText(self, pos=(300, 60), label="Ingredients")

        self.ingredients_category_selector = cw.PromptingComboBox(self, choices=list(lists.all.keys()))
        self.ingredients_category_selector.SetPosition((300, 80))
        self.ingredients_category_selector.SetSize((150, 40))
        self.ingredients_category_selector.SetHint("Refine by Category")
        self.ingredients_category_selector.Master = True

        self.ingredients_item_selector = cw.PromptingComboBox(self, choices=[])
        self.ingredients_item_selector.SetPosition((460, 80))
        self.ingredients_item_selector.SetSize((150, 40))
        self.ingredients_item_selector.SetHint("Ingredient")

        self.ingredients_amount = wx.TextCtrl(self, pos=(620, 80), size=(75, 40))
        self.ingredients_amount.SetHint("amount")

        self.ingredients_add = wx.Button(self, pos=(705, 80), size=(100, 40), label="add ingredient")
        self.ingredients_add.Bind(wx.EVT_BUTTON, self.ingredients_submit)

        self.ingredients_clear = wx.Button(self, pos=(705, 130), size=(100, 40), label="Reset")
        self.ingredients_clear.Bind(wx.EVT_BUTTON, self.ingredients_reset)

        self.ingredients_delete = wx.Button(self, pos=(705, 180), size=(100, 40), label="Delete Last")
        self.ingredients_delete.Bind(wx.EVT_BUTTON, self.ingredients_remove)

        self.ingredients_display = wx.TextCtrl(self, pos=(300, 130), size=(395,200), style=wx.TE_MULTILINE|wx.TE_READONLY)

        # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        # instructions
        self.instructions_title = wx.StaticText(self, pos=(300, 60), label="Instructions")

        self.instructions_display = wx.TextCtrl(self, pos=(300, 100), size=(450, 200),
                                               style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER, value="- ")
        self.instructions_display.Bind(wx.EVT_TEXT_ENTER, self.instructions_enter)

        self.instructions_timer = wx.Button(self, pos=(300, 400), size=(100,40), label="add Timer")
        self.instructions_timer.Bind(wx.EVT_BUTTON, self.add_timer)

        # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        # tags
        self.tags_title = wx.StaticText(self, pos=(300, 60), label="Tags")

        self.tags_entry = wx.TextCtrl(self, pos=(300, 100), size=(200, 50),
                                               style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER, value="")
        self.tags_entry.SetHint("Enter tags here")
        self.tags_entry.Bind(wx.EVT_TEXT_ENTER, self.tags_enter)

        self.tags_entered = wx.StaticText(self, pos=(300, 160), size=(200, 50),
                                               style=wx.TE_MULTILINE, label="")
        self.tags_list = []
        self.tags_remove_last = wx.Button(self, pos=(510, 100), size=(100,30), label="Remove last")
        self.tags_remove_last.Bind(wx.EVT_BUTTON, self.tags_remove_one)
        self.tags_remove_all = wx.Button(self, pos=(510, 140), size=(100, 30), label="Remove all")
        self.tags_remove_all.Bind(wx.EVT_BUTTON, self.tags_remove_every)


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
        self.update_subs()
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()
        self.ingredients_display.SetSize((395, size[1] - 200))
        self.instructions_display.SetSize((450, size[1] - 200))
        self.instructions_timer.SetPosition((300, size[1] - 90))

    # for updating the subcontents views
    def update_subs(self):
        # start by setting all the selector buttons to the default size
        default_size = (150, 40)
        selected_size = (200, 40)
        self.instructions_sub.SetSize(default_size)
        self.ingredients_sub.SetSize(default_size)
        self.tags_sub.SetSize(default_size)

        # then we will hide all the things that can be selected between
        self.ingredients_title.Hide()
        self.ingredients_category_selector.Hide()
        self.ingredients_item_selector.Hide()
        self.ingredients_amount.Hide()
        self.ingredients_add.Hide()
        self.ingredients_clear.Hide()
        self.ingredients_display.Hide()
        self.ingredients_delete.Hide()

        self.instructions_title.Hide()
        self.instructions_display.Hide()
        self.instructions_timer.Hide()

        self.tags_title.Hide()
        self.tags_entry.Hide()
        self.tags_entered.Hide()
        self.tags_remove_all.Hide()
        self.tags_remove_last.Hide()

        # finally we will update the sizes of the buttons, and show the content
        if self.sub == 1:
            self.ingredients_sub.SetSize(selected_size)
            self.ingredients_title.Show()
            self.ingredients_category_selector.Show()
            self.ingredients_item_selector.Show()
            self.ingredients_amount.Show()
            self.ingredients_add.Show()
            self.ingredients_clear.Show()
            self.ingredients_display.Show()
            self.ingredients_delete.Show()
        elif self.sub == 2:
            self.instructions_sub.SetSize(selected_size)
            self.instructions_title.Show()
            self.instructions_display.Show()
            self.instructions_timer.Show()
        elif self.sub == 3:
            self.tags_sub.SetSize(selected_size)
            self.tags_title.Show()
            self.tags_entry.Show()
            self.tags_entered.Show()
            self.tags_remove_all.Show()
            self.tags_remove_last.Show()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        self.sub = 0
        if self.parent.user.metric != self.ingredients_list.metric():
            self.ingredients_list.convert_unit()

    def display_error(self, message):
        self.error_message.Show()
        self.error_message.SetLabel(message)


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
        self.sub = 3
        self.update_subs()

    def edit_ingredients(self, event=None):
        self.sub = 1
        self.update_subs()

    def edit_instructions(self, event=None):
        self.sub = 2
        self.update_subs()

    def ingredients_category_chosen(self):
        val = self.ingredients_category_selector.GetValue()
        self.ingredients_amount.SetHint("<UNIT>")
        self.ingredients_item_selector.SetItems(lists.all[val])

    def ingredients_reset(self, event=None):
        self.ingredients_amount.SetLabel("")
        self.ingredients_category_selector.SetLabel("")
        self.ingredients_item_selector.SetLabel("")
        self.error_message.Hide()

    def ingredients_submit(self, event=None):
        first = self.ingredients_item_selector.GetValue()
        second = self.ingredients_amount.GetValue()
        third = self.ingredients_amount.GetHint()
        if first not in lists.ingredients:
            self.display_error("Unknown ingredient")
            return 0

        try:
            int(second)
        except:
            self.display_error("Enter a number for \ningredient amounts")
            return 0

        self.ingredients_list.add_item([first, second, third])
        self.ingredients_display.SetValue(self.ingredients_list.pretty())
        self.ingredients_reset()

    def ingredients_remove(self, event=None):
        self.ingredients_list.remove_item(-1)

    def instructions_enter(self, event=None):
        temp = self.instructions_display.GetValue() + "\n- "
        self.instructions_display.SetValue(temp)
        self.instructions_display.SetInsertionPointEnd()

    def add_timer(self, event=None):
        temp = self.instructions_display.GetValue() + " [TIMER:5min] "
        self.instructions_display.SetValue(temp)
        self.instructions_display.SetInsertionPointEnd()

    def tags_enter(self, event=None):
        temp = self.tags_entry.GetValue().lower()
        if temp[-1] is " ":
            temp = temp[:-1]
        self.tags_entry.SetValue("")
        self.tags_list.append(temp)
        temp = ""
        for x in self.tags_list:
            temp += x + ", "
        temp = wordwrap(temp, 30)
        self.tags_entered.SetLabel(temp)

    def tags_remove_every(self, event=None):
        self.tags_list = []
        self.tags_entered.SetLabel("")

    def tags_remove_one(self, event=None):
        if len(self.tags_list) > 0:
            del self.tags_list[-1]
        temp = ""
        for x in self.tags_list:
            temp += x + ", "
        temp = wordwrap(temp, 30)
        self.tags_entered.SetLabel(temp)


# when passed a string, will wrap the text after the given number of characters
# used for text boxes that dont wrap for if you need it.
# takes in [string] >> the text to be wrapped
# takes in [int] >> the number of characters per line before it starts trying to wrap
# returns [string] >> formatted
# looks for a space and inserts a \n when the character limit is reached
def wordwrap(text, chars):
    assert isinstance(text, str), "you must pass a string"
    counter = 0
    new = ""
    for x in range(0, len(text)):
        if (counter > chars) and (text[x] == " "):
            new = new + '\n '
            counter = 0
        else:
            new = new + text[x]
            counter += 1
    return new
