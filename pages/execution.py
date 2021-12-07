import sys
import regex
import wx

# not yet implemented in any way
# saving this one for someone else to do, so I dont do all the UI

class Execution(wx.Panel):
    #init method, initial constructor, this is what is run when it is first called
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.recipe = self.parent.user.open_recipe

        # UI implementation here:
        self.page_name = wx.StaticText(parent=self, label="Make a Recipe", pos=(120, 20))
        self.tools_req = wx.StaticText(parent=self, label="Tools Required:", pos=(10, 100))
        self.ingredients_req = wx.StaticText(parent=self, label="Ingredients Required:", pos=(10, 180))
        self.instructions_text = wx.StaticText(parent=self, label="Instructions:", pos=(10, 280))

        #the following fields will be filled with user data
        self.recipe_name = wx.StaticText(parent=self, pos=(20, 70))

        self.tools_list = wx.TextCtrl(parent=self, pos=(10, 120), size=(200, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.tools_list.Show()

        self.ingredients_list = wx.TextCtrl(parent=self, pos=(10, 200), size=(200, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.ingredients_list.Show()

        #placeholder to get an idea for what kind of space we have to work with
        self.image = wx.StaticBox(parent=self, pos=(600, 20), size=(200,200))

        self.instructions_list = wx.ListCtrl(parent=self, pos=(10, 300), size=(700, 300), style=wx.LC_REPORT)
        self.instructions_list.InsertColumn(col=0, heading='Step')
        self.instructions_list.InsertColumn(col=1, heading='Instructions')
        self.instructions_list.SetBackgroundColour(wx.Colour(175,175,175))

        self.next_instruction = wx.Button(parent=self, label="Next Step", pos=(600, 220), size=(100,50))
        self.next_instruction.Bind(wx.EVT_BUTTON, self.go_next_step)

        self.prev_instruction = wx.Button(parent=self, label="Prev Step", pos=(500, 220), size=(100,50))
        self.prev_instruction.Bind(wx.EVT_BUTTON, self.go_prev_step)

        self.Units = wx.Button(parent=self, label=self.get_unit_label(), pos=(700, 220), size=(100,50))
        self.Units.Bind(wx.EVT_BUTTON, self.change_units)

        self.time_start = wx.Button(parent=self, label="Start Timer", pos=(10,625))
        self.time_start.Bind(wx.EVT_BUTTON, self.start_timer)

        self.time_pause = wx.Button(parent=self, label="Pause Timer", pos=(220,625))
        self.time_pause.Bind(wx.EVT_BUTTON, self.pause_timer)
        self.time_pause.Hide()

        self.timer_status = wx.TextCtrl(parent=self, pos=(100,625))

        # load in user dataManagement
        self.update_user()

    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()

    # gets called when a panel is reloaded, not required to do anything but must be here
    # this is where user information should be loaded in
    def update_user(self):
        self.recipe = self.parent.user.open_recipe
        self.recipe_name.SetLabel(self.recipe.title)

        self.tools_parse = ""
        for x in self.recipe.tools:
            self.tools_parse += x + '\n'
        self.tools_list.SetValue(self.tools_parse)

        self.ingredients_list.SetValue(self.recipe.ingredients.pretty())

        #timer functionality will have to be added
        self.steps = enumerate(self.recipe.instructions, start=1)

        self.instructions_list.DeleteAllItems()
        for x in self.steps:
            index = self.instructions_list.InsertItem(sys.maxsize, x[0])
            self.instructions_list.SetItem(index, 0, str(x[0]))
            self.instructions_list.SetItem(index, 1, x[1])
        self.instructions_list.SetColumnWidth(col=1, width=wx.LIST_AUTOSIZE)

        self.current_step = self.instructions_list.GetTopItem()
        self.go_next_step()
        self.go_prev_step()

        #self.image = (self.recipe.image)

    def go_next_step(self, event=None):
        if(self.instructions_list.GetNextItem(self.current_step, wx.LIST_NEXT_BELOW) == -1):
            pass
        else:
            self.instructions_list.SetItemBackgroundColour(self.current_step, wx.Colour(175, 175, 175))
            self.current_step = self.instructions_list.GetNextItem(item=self.current_step, geometry=wx.LIST_NEXT_BELOW, state=wx.LIST_STATE_DONTCARE)
            self.instructions_list.SetItemBackgroundColour(self.current_step, wx.Colour(255, 219, 41))

    def go_prev_step(self, event=None):
        if(self.instructions_list.GetNextItem(self.current_step, wx.LIST_NEXT_ABOVE) == -1):
            pass
        else:
            self.instructions_list.SetItemBackgroundColour(self.current_step, wx.Colour(175, 175, 175))
            self.current_step = self.instructions_list.GetNextItem(item=self.current_step, geometry=wx.LIST_NEXT_ABOVE, state=wx.LIST_STATE_DONTCARE)
            self.instructions_list.SetItemBackgroundColour(self.current_step, wx.Colour(255, 219, 41))

    def change_units(self, event=None):
        self.parent.user.metric = not(self.parent.user.metric)
        self.parent.user.change_units()
        self.Units.SetLabel(self.get_unit_label())
        self.ingredients_list.SetValue(self.recipe.ingredients.pretty())

    def get_unit_label(self):
        if self.parent.user.metric:
            return "Metric"
        else:
            return "Imperial"

    def pause_timer(self, event=None):
        if self.parent.user.timer_status():
            self.parent.user.pause_timer()
            self.time_pause.SetLabel("Resume Timer")
        else:
            self.time_pause.SetLabel("Pause Timer")
            self.parent.user.timer_resume()

    def start_timer(self, event=None):
        if not self.parent.user.timer_status():
             self.parent.user.start_timer(10, self.timer_status)
             self.time_start.SetLabel("Stop")
             self.time_pause.Show()
        else:
             self.parent.user.end_timer()
             self.time_start.SetLabel("Start")
             self.time_pause.Hide()