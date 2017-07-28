from objects import *
from drawingtools import *

class Events():
    focus = Blob()
    def __init__(self):
        self.click_events = []
        self.keymap = {39:34, 44:60, 45:95, 46:62, 47:63, 48:41, 49:33, 50:64, 51:35, 52:36, 53:37, 61:43, 91:123, 92:124, 93:125, 54:94, 55:38, 56:42, 57:40, 59:58, 96:126}
        
    def button_check(self):
        if not isinstance(self.focus, (Blob)):                                        
            self.focus.unfocus()
        self.focus = Blob()
        pos = pygame.mouse.get_pos()
        for c in self.click_events:
            if c.rect.collidepoint(pos):
                c.click()
                
    def delete(self, obj):
        self.click_events.pop(self.click_events.index(obj))
                  
    def draw(self):
        for c in self.click_events:
            c.draw()
            
    def send(self, entry, TYPE="KEY"):
        if TYPE == "KEY":
            keys = pygame.key.get_pressed()
            if 1 in keys:
                if keys[304] == 1:
                    SHIFT = True
                else:
                    SHIFT = False
            if entry < 256:
                if entry == 8 and self.focus.editable:
                    value = list(self.focus.value)
                    if value != []:
                        value.pop(-1)
                        value = "".join(value)
                        self.focus.value = value
                        self.focus.text = value
                    elif not isinstance(self.focus, Blob):
                        self.focus.unfocus()
                        if hasattr(self.focus, 'onBackspace'):
                            self.focus.onBackspace(self.focus)
                        else:
                            self.focus = Blob()
                elif entry == 8 and not isinstance(self.focus, Blob):
                    self.focus.unfocus()
                    if hasattr(self.focus, 'onBackspace'):
                        self.focus.onBackspace(self.focus)
                    else:
                        self.focus = Blob()
                elif entry == 9 and self.focus.editable:
                    value = " "*4
                    self.focus.value += value
                    self.focus.text += value
                elif entry == 13:
                    self.focus.Submit()
                elif self.focus.editable:
                    if SHIFT == True and entry-32 >= 0:
                        if entry in self.keymap:
                            entry = self.keymap[entry]
                        else:
                            entry -= 32
                    key = chr(entry)
                    self.focus.value += key
                    self.focus.text += key
