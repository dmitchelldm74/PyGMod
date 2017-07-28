from objects import *
from EventManager import *
from drawingtools import *


class TextBox():
    def __init__(self, parent=None, rect=(0,0,0,0), text="Type Here...", color=(200,200,200), font="freesansbold.ttf", padding=10, fg=(255,255,255), focus_color=(170,170,170), event_manager=Events(), value="", onSubmit=lambda junk: None):
        self.parent = parent
        self.rect = pygame.Rect(rect)
        self.text = text
        self.placeholder = text
        self.value = value
        self.color = color
        self.back_color = color
        self.focus_color = focus_color
        self.radius = 0.15
        self.fontname = font
        self.padding = padding
        self.fg = fg
        self.onSubmit = onSubmit
        self.onClick = lambda tb:None  
        self.editable = True      
        self.event_manager = event_manager
        self.event_manager.click_events.append(self)
        self.generate_rectangle()
        self.generate_font()
        self.draw()
        
    def generate_rectangle(self):
        self.rectangle, self.pos = AAfilledRoundedRect(self.rect, self.color, self.radius)
        
    def generate_font(self):
        self.fontsize = self.rect[3]-10
        self.font = pygame.font.Font(self.fontname,self.fontsize)
        
    def render_text(self):
        size = self.rect[3]-10
        limit = (self.rect[2] / self.fontsize*2)
        start = 0
        tlen = len(self.text)
        if tlen >= limit:
            start = tlen-limit
        self.label = self.font.render(self.text[start:limit+start], 1, self.fg)
        rect = self.label.get_rect(center=(self.label.get_width()/2+10, self.rectangle.get_height()/2)) # self.rect[0]+10
        self.labelrect = add_rect(rect, self.rect)
        
    def draw(self):  
        self.parent.blit(self.rectangle, self.pos)
        self.render_text()
        self.parent.blit(self.label, self.labelrect)
        
    def click(self):
        self.onClick(self)
        self.event_manager.focus = self
        if self.value == "":
            self.text = ""
        self.color = self.focus_color
        self.generate_rectangle()
        self.draw()
        
    def focus(self):
        self.click()
        
    def unfocus(self):
        self.color = self.back_color
        self.generate_rectangle()
        self.draw()
        
    def Submit(self):        
        self.event_manager.focus = Blob()
        self.color = self.back_color
        self.onSubmit(self)
        self.generate_rectangle()
    
    def set_text(self, text):
        self.text = text
        self.render_text()
        
    def get_text(self):
        return self.text   
        
    def set_color(self, color, TYPE="BG"):
        if isinstance(color, (tuple)) and len(color) == 3 and color[0] <= 255 and color[1] <= 255 and color[2] <= 255:
            if TYPE == "BG":
                self.back_color = color
                self.generate_rectangle()
            elif TYPE == "FG":
                self.fg = color
                self.generate_font()
            elif TYPE == "FC":
                self.focus_color = color
            return 
        raise ValueError("Value must be a tuple with three elements, each less than or equal to 255. (R,G,B)")  
        
    def get_color(self):
        return self.color
        
    def clear(self):
        self.text = self.placeholder
        self.value = ""  
