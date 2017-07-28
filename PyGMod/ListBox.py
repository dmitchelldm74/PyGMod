from TextBox import *

# TODO: Arrow key scrolling

class ListBox(TextBox):
    textboxes = []
    selected = -1
    Selected = Blob()
    onClicks = []
    def __init__(self, *args, **kwargs):
        self.lines = kwargs["lines"]
        if "focus_color" not in kwargs:
            kwargs["focus_color"] = (100,100,200)
        self.args = args
        self.strings = [" "] * self.lines
        for a in args:
            if isinstance(a, str):
                self.strings = a.split("\n") + self.strings
                break
        self.kwargs = kwargs
        del kwargs["lines"]
        self.render_textbox()
        
    def render_textbox(self):
        for l in range(0, self.lines):
            tb = TextBox(*self.args, **self.kwargs)
            tb.radius = 0.0
            tb.rect[1] += tb.rect[3]*l
            tb.text = tb.placeholder = tb.value = self.strings[l]
            tb.generate_rectangle()
            tb.render_text()
            tb.onSubmit = self.onEnter
            tb.onClick = self.IndexChange
            tb.editable = False
            tb.onBackspace = lambda tb, self=self: self[getattr(self, 'selected')-1]
            self.onClicks.append(lambda tb: None)
            self.textboxes.append(tb)
            
    def onEnter(self, tb):
        self.Selected = tb
        tb.click()
            
    def onDown(self, tb):
        if self.selected+1 < len(self.textboxes):
            self.selected += 1
            self.textboxes[self.selected].click()
            
    def IndexChange(self, tb):
        self.selected = self.textboxes.index(tb)
        self.Selected = tb
        self.onClicks[self.selected](tb)
        
    def __getitem__(self, index):
        self.selected = index
        if self.selected < len(self.textboxes):
            self.textboxes[self.selected].click()
            
    def clear(self):
        for tb in self.textboxes:
            tb.clear()
        
    def __getattr__(self, name):
        if name == 'value':
            return self.Selected.value
        elif name == 'rect':
            if self.textboxes != []:
                return self.textboxes[-1].rect
            return [0,0,0,0]
            
