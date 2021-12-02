import wx


class PromptingComboBox(wx.ComboBox):
    # code derived from
    # https://wiki.wxpython.org/Combo%20Box%20that%20Suggests%20Options?action=raw
    def __init__(self, parent, choices=[], style=0, **par):
        self.parent = parent
        wx.ComboBox.__init__(self, parent, style=style | wx.CB_DROPDOWN, choices=choices, **par)
        self.choices = choices
        self.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_CHAR, self.EvtChar)
        self.Bind(wx.EVT_COMBOBOX, self.EvtCombobox)
        self.ignoreEvtText = False


        self.Master = False

    def EvtCombobox(self, event):
        if self.Master:
            self.parent.ingredients_category_chosen()
        self.ignoreEvtText = True
        event.Skip()

    def EvtChar(self, event):
        if event.GetKeyCode() == 8:
            self.ignoreEvtText = True
        event.Skip()

    def EvtText(self, event):
        if self.ignoreEvtText:
            self.ignoreEvtText = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.choices:
            if choice.startswith(currentText):
                self.ignoreEvtText = True
                self.SetValue(choice)
                self.SetInsertionPoint(len(currentText))
                self.SetTextSelection(len(currentText), len(choice))
                found = True
                break
        if not found:
            event.Skip()
        else:
            self.parent.ingredients_category_chosen()
