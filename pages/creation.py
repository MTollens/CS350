import wx
import os
from resources import lists
from dataManagement import ingredients
from pages import custom_widgets as cw
from dataManagement import recipe as recipe
import warnings
import shutil
from dataManagement import common_utils
from pages import theme

# not yet implemented in any way
# saving this one for someone else to do, so I dont do all the UI

class Creation(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        font_Title = wx.Font(18, family=wx.FONTFAMILY_MODERN, style=0, weight=100,
                       underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font_Sub = wx.Font(14, family=wx.FONTFAMILY_MODERN, style=0, weight=100,
                       underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)

        self.sub = 0
        # to give the user one more chance to change things before they submit
        self.are_you_sure = False

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.controls_box = wx.StaticBox(self, pos=(50,50), size=(220,525))

        self.page_name = wx.StaticText(parent=self, label="Recipe Editor", pos=(60, 10), size=(200,30))
        self.page_name.SetFont(font_Title)

        self.image = wx.Button(self, pos=(60,70), size=(160, 160), label="add image")
        self.image.Bind(wx.EVT_BUTTON, self.image_select)
        self.image_path = ""

        self.web_image = wx.Button(self, pos=(225, 195), label="🌐", size=(35, 35))
        self.web_image.SetFont(font_Sub)
        self.web_image.Bind(wx.EVT_BUTTON, self.find_web_image)

        # UI implementation here:
        self.Title_box = wx.TextCtrl(parent=self, pos=(60, 240), size=(200,30))
        self.Title_box.SetHint("Title")

        self.MakesFor = wx.TextCtrl(parent=self, pos=(60, 280), size=(200,30))
        self.MakesFor.SetHint("How many servings?")

        self.Preptime = wx.TextCtrl(parent=self, pos=(60, 320), size=(200,30))
        self.Preptime.SetHint("How long to prepare?")

        self.ingredients_sub = wx.Button(self, pos=(60, 370), size=(150,40), label="Edit Ingredients", style=wx.BU_LEFT)
        self.ingredients_sub.Bind(wx.EVT_BUTTON, self.edit_ingredients)
        self.instructions_sub = wx.Button(self, pos=(60, 420), size=(150, 40), label="Edit Instructions", style=wx.BU_LEFT)
        self.instructions_sub.Bind(wx.EVT_BUTTON, self.edit_instructions)
        self.tags_sub = wx.Button(self, pos=(60, 470), size=(150, 40), label="Edit Tags", style=wx.BU_LEFT)
        self.tags_sub.Bind(wx.EVT_BUTTON, self.edit_tags)
        self.tools_sub = wx.Button(self, pos=(60, 520), size=(150, 40), label="Edit Tools", style=wx.BU_LEFT)
        self.tools_sub.Bind(wx.EVT_BUTTON, self.edit_tools)

        self.error_message = wx.StaticText(self, pos=(500, 15), label="", style=wx.TE_RICH)
        self.error_message.Hide()
        self.error_message.SetForegroundColour(wx.RED)

        self.preview = wx.Button(self, pos=(60, 590), label="Preview", size=(150, 40))
        self.preview.Bind(wx.EVT_BUTTON, self.preview_recipe)
        self.finish = wx.Button(self, pos=(60, 640), label="Finish", size=(150, 40))
        self.finish.Bind(wx.EVT_BUTTON, self.finish_recipe)

        # end of STATIC UI elements

        # web image box

        self.web_image_box = wx.TextCtrl(self, pos=(280, 200), size=(300, 40), style=wx.TE_PROCESS_ENTER)
        self.web_image_box.SetHint("Enter an Image URL here")
        self.web_image_box.Hide()
        self.web_image_box.Bind(wx.EVT_TEXT_ENTER, self.check_web_image)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # ingredients
        self.ingredients_list = ingredients.Ingredients()
        self.ingredients_title = wx.StaticText(self, pos=(300, 14), label="Ingredients", size=(150,50))
        self.ingredients_title.SetFont(font_Sub)

        self.ingredients_category_selector = cw.PromptingComboBox(self, choices=list(lists.all.keys()))
        self.ingredients_category_selector.SetPosition((300, 80))
        self.ingredients_category_selector.SetSize((150, 40))
        self.ingredients_category_selector.SetHint("Refine by Category")
        self.ingredients_category_selector.Master = True

        self.ingredients_item_selector = cw.PromptingComboBox(self, choices=[])
        self.ingredients_item_selector.SetPosition((460, 80))
        self.ingredients_item_selector.SetSize((150, 40))
        self.ingredients_item_selector.SetHint("Ingredient")
        self.ingredients_item_selector.Bind(wx.EVT_COMBOBOX, self.set_ingredient_unit)

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
        self.instructions_title = wx.StaticText(self, pos=(300, 14), label="Instructions", size=(150,50))
        self.instructions_title.SetFont(font_Sub)

        self.instructions_display = wx.TextCtrl(self, pos=(300, 100), size=(450, 200),
                                               style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER, value="- ")
        self.instructions_display.Bind(wx.EVT_TEXT_ENTER, self.instructions_enter)

        self.instructions_timer = wx.Button(self, pos=(300, 400), size=(100,40), label="add Timer")
        self.instructions_timer.Bind(wx.EVT_BUTTON, self.add_timer)

        # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        # tags
        self.tags_title = wx.StaticText(self, pos=(300, 14), label="Tags",size=(150,50))
        self.tags_title.SetFont(font_Sub)

        self.tags_entry = wx.TextCtrl(self, pos=(300, 100), size=(200, 70),
                                               style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER, value="")
        self.tags_entry.SetHint("Enter tags here")
        self.tags_entry.Bind(wx.EVT_TEXT_ENTER, self.tags_enter)

        self.tags_entered = wx.StaticText(self, pos=(300, 170), size=(200, 50),
                                               style=wx.TE_MULTILINE, label="")
        self.tags_list = []
        self.tags_remove_last = wx.Button(self, pos=(510, 100), size=(100,30), label="Remove last")
        self.tags_remove_last.Bind(wx.EVT_BUTTON, self.tags_remove_one)
        self.tags_remove_all = wx.Button(self, pos=(510, 140), size=(100, 30), label="Remove all")
        self.tags_remove_all.Bind(wx.EVT_BUTTON, self.tags_remove_every)

        #WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
        #tools
        self.tools_title = wx.StaticText(self, pos=(300, 14), label="Tools", size=(150, 50))
        self.tools_title.SetFont(font_Sub)

        self.tools_list = []

        self.tools_category_selector = cw.PromptingComboBox2(self, choices=list(lists.all_tools.keys()))
        self.tools_category_selector.SetPosition((300, 80))
        self.tools_category_selector.SetSize((150, 40))
        self.tools_category_selector.SetHint("Refine by Category")
        self.tools_category_selector.Master = True

        self.tools_item_selector = cw.PromptingComboBox2(self, choices=[])
        self.tools_item_selector.SetPosition((460, 80))
        self.tools_item_selector.SetSize((150, 40))
        self.tools_item_selector.SetHint("Tool")

        self.tools_add = wx.Button(self, pos=(705, 80), size=(100, 40), label="add Tool")
        self.tools_add.Bind(wx.EVT_BUTTON, self.tools_submit)

        self.tools_clear = wx.Button(self, pos=(705, 130), size=(100, 40), label="Reset")
        self.tools_clear.Bind(wx.EVT_BUTTON, self.tools_reset)

        self.tools_delete = wx.Button(self, pos=(705, 180), size=(100, 40), label="Delete Last")
        self.tools_delete.Bind(wx.EVT_BUTTON, self.tools_remove)

        self.tools_display = wx.TextCtrl(self, pos=(300, 130), size=(395, 200),
                                         style=wx.TE_MULTILINE | wx.TE_READONLY)

        # load in user dataManagement
        self.update_subs()
        self.update_user()


        if theme.enable and self.parent.user.platform == "Windows":
            if theme.dark_theme:
                self.SetBackgroundColour(theme.dark)
                self.SetForegroundColour(theme.light)



    def find_web_image(self, event=None):
        self.sub = 0
        self.update_subs()
        self.web_image_box.Show()

    def check_web_image(self, event=None):
        self.web_image_box.Hide()
        if self.web_image_box.GetValue() in empty:
            return 0
        self.image_path = self.web_image_box.GetValue()
        self.image.SetBitmap(common_utils.web_image(self.image_path, self.image.GetSize()))
        self.image.SetLabel("")

        # common_utils.find_web_image("url")

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
        self.tools_sub.SetSize(default_size)

        # then we will hide all the things that can be selected between
        self.web_image_box.Hide()

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

        self.tools_title.Hide()
        self.tools_category_selector.Hide()
        self.tools_item_selector.Hide()
        self.tools_add.Hide()
        self.tools_clear.Hide()
        self.tools_delete.Hide()
        self.tools_display.Hide()

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
        elif self.sub == 4:
            self.tools_sub.SetSize(selected_size)
            self.tools_title.Show()
            self.tools_category_selector.Show()
            self.tools_item_selector.Show()
            self.tools_add.Show()
            self.tools_clear.Show()
            self.tools_delete.Show()
            self.tools_display.Show()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        self.sub = 0
        # if self.parent.user.metric != self.ingredients_list.metric():
        #     self.ingredients_list.convert_unit()

    def display_error(self, message):
        self.error_message.Show()
        # not needed since the error was moved to the top
        # self.error_message.SetLabel(wordwrap(message, 100))
        self.error_message.SetLabel(message)

    def image_select(self, event=None):
        # code referenced from https://www.programcreek.com/python/example/3163/wx.FileDialog
        filename = ""

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
            self.image.SetBitmap(common_utils.load_image(dlg.GetPath(), self.image.GetSize()))
            self.image_path = dlg.GetPath()
            self.image.SetLabel("")
        else:
            self.image.SetLabel("Image couldnt\nbe loaded")

    # this is where changes are commited, data that was entered on the page is put into a recipe class
    # and the class is passed to the storage handler
    def finish_recipe(self, event=None):
        final = self.make_recipe()
        if final == 0:
            return 0
        if not self.are_you_sure:
            self.are_you_sure = True
            self.display_error("Press [Finish] once more to confirm you are done")
            return 0
        else:
            self.are_you_sure = False

        self.display_error("")
        # copy the image files to the images directory
        source = final.image
        destination = "images/{}".format(os.path.basename(source))
        if not os.path.exists(destination):
            shutil.copy(source, destination)
            # set the new file location as the image location
            final.image = destination
            print(source)
            print(destination)
        self.parent.user.save_recipe(final)
        self.parent.user.open_recipe = recipe.Recipe("CREATOR")
        self.parent.setHomepage()
        self.load_recipe()

    def update_ingredients_display(self):
        if self.parent.user.metric:
            self.ingredients_display.SetValue(self.ingredients_list.pretty())
        else:
            self.ingredients_display.SetValue(self.ingredients_list.pretty_imperial())

    # load the recipe from a recipe class for editing purposes
    def load_recipe(self):
        new = self.parent.user.open_recipe
        assert isinstance(new, recipe.Recipe)
        if (new.owner != self.parent.user.username) and (new.owner not in ["DEFAULT", "CREATOR"]):
            warnings.warn("user trying to edit recipe they dont own")
            return 0

        self.Title_box.SetValue(new.title)
        self.ingredients_list = new.ingredients
        self.update_ingredients_display()
        self.image_path = new.image
        self.image.SetBitmap(common_utils.load_image(self.image_path, (160,160)))
        self.image.SetLabel("")
        temp = ""
        for x in new.instructions:
            # print(x)
            temp += x + "\n"
        # print("here:")
        # print(new.instructions)
        # print(temp)
        self.instructions_display.SetValue(temp)
        self.instructions_display.SetInsertionPointEnd()
        self.tools_list = new.tools
        temp = ""
        for x in self.tools_list:
            temp += x + "\n"
        self.tools_display.SetValue(temp)
        self.MakesFor.SetLabel(str(new.servings))
        self.Preptime.SetLabel(new.prep_time)
        self.tags_list = new.tags
        temp = ""
        for x in self.tags_list:
            temp += x + ", "
        self.tags_entered.SetLabel(temp)

        self.update_subs()

    # edit buttons set the subpanel variable then update the panel
    def edit_tags(self, event=None):
        self.sub = 3
        self.update_subs()

    def edit_ingredients(self, event=None):
        self.sub = 1
        self.update_subs()

    def edit_instructions(self, event=None):
        self.sub = 2
        self.update_subs()

    def edit_tools(self, event=None):
        self.sub = 4
        self.update_subs()

    def set_ingredient_unit(self, event=None):
        temp = self.parent.user.database.getIngredientUnit(self.ingredients_item_selector.GetValue())
        print("temp: {}".format(temp))
        if temp:
            if self.parent.user.metric:
                self.ingredients_amount.SetHint(temp)
            else:
                # the unused value key here is because the function always returns 2 items
                temp, value = common_utils.convert_units_to_imperial(temp, 0)
                self.ingredients_amount.SetHint(temp)

    # specific subpanel action handlers, should be fairly obvious what they do from the names
    def ingredients_category_chosen(self):
        val = self.ingredients_category_selector.GetValue()
        self.ingredients_amount.SetHint("<UNIT>")
        self.ingredients_item_selector.SetItems(lists.all[val])

    def ingredients_reset(self, event=None):
        self.ingredients_amount.SetValue("")
        self.ingredients_category_selector.SetValue("")
        self.ingredients_item_selector.SetValue("")
        self.error_message.Hide()

    def ingredients_submit(self, event=None):
        first = self.ingredients_item_selector.GetValue()
        second = self.ingredients_amount.GetValue()
        third = self.ingredients_amount.GetHint()
        if first not in lists.ingredients:
            self.display_error("Unknown ingredient")
            return 0

        try:
            float(second)
        except:
            self.display_error("Enter a number for ingredient amounts")
            return 0

        self.ingredients_list.add_item([first, second, third])
        self.update_ingredients_display()
        self.ingredients_reset()

    def ingredients_remove(self, event=None):
        self.ingredients_list.remove_item(-1)
        self.update_ingredients_display()

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
        if temp[-1] == " ":
            temp = temp[:-1]

        self.tags_entry.SetValue("")

        if temp in self.tags_list:
            self.display_error("Tag already entered!")
            return 0

        self.tags_list.append(temp)
        temp = ""
        for x in self.tags_list:
            temp += x + ", "
        temp = wordwrap(temp, 30)
        self.tags_entered.SetLabel(temp)
        self.error_message.Hide()

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

    def tools_submit(self, event=None):
        first = self.tools_item_selector.GetValue()
        if first not in lists.tools:
            self.display_error("Unknown tool")
            return 0

        self.tools_list.append(first)
        temp = ""
        for x in self.tools_list:
            temp += x +"\n"
        self.tools_display.SetValue(temp)
        self.tools_reset()
    
    def tools_reset(self, event=None):
        self.tools_category_selector.SetValue("")
        self.tools_item_selector.SetValue("")
        self.error_message.Hide()
    
    def tools_remove(self, event=None):
        if len(self.tools_list) > 0:
            del self.tools_list[-1]
        temp = ""
        for x in self.tools_list:
            temp += x +"\n"
        self.tools_display.SetValue(temp)

    def tools_category_chosen(self, event=None):
        val = self.tools_category_selector.GetValue()
        self.tools_item_selector.SetItems(lists.all_tools[val])

    # pulls data from all the fields on the page, and returns a recipe object
    def make_recipe(self):
        item = recipe.Recipe()
        item.image = self.image_path
        if not os.path.exists(item.image):
            self.display_error("Using default image since none was supplied")
            item.image = "resources/nofile.png"
        item.owner = self.parent.user.username
        item.ingredients = self.ingredients_list
        temp = item.ingredients.validate()
        # ignore the warning here, because the previous function returns true if true, and a number if false
        if not (temp == True):
            # allows for a secondary validation of ingredients
            self.display_error("ingredient number {} was incorrect".format(temp+1))
            # some way to supply more info here
            return 0

        item.title = self.Title_box.GetValue()
        if item.title in empty:
            self.display_error("Invalid title, give it a standout name!")
            return 0
        item.tools = self.tools_list
        if item.tools in empty:
            self.display_error("Please enter all the tools require to make this dish")
            return 0
        item.tags = self.tags_list
        if item.tags in empty:
            self.display_error("please enter at least one tag, it really helps out those who want to find this recipe")
            return 0
        item.origin = "creator"
        item.prep_time = self.Preptime.GetValue()
        if item.prep_time in empty:
            self.display_error("please enter the time it takes to make this recipe")
            return 0
        item.instructions = self.instructions_display.GetValue().split("\n")
        try:
            item.servings = float(self.MakesFor.GetValue())
        except:
            self.display_error("Servings should be a valid number")
            return 0
        return item

    # opens the recipe in the execution screen
    def preview_recipe(self, event=None):
        item = self.make_recipe()
        if item == 0:
            return
        self.parent.user.open_recipe = item
        self.parent.setExecution()

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

empty = [" ","",None]
