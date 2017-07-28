from objects import *
from EventManager import *
from drawingtools import *

class Label():
    def __init__(self, parent=None, rect=(0,0,0,0), text="button", onClick=lambda btn: None, font="freesansbold.ttf", fg=(0,0,0), event_manager=Events()):
        self.parent = parent
        self.onClick = onClick
        self.rect = pygame.Rect(rect)
        self.text = text
        self.fontname = font
        self.fg = fg
        self.event_manager = event_manager
        self.event_manager.click_events.append(self)
        self.generate_font()
        self.render_text()
        self.draw()
        
    def generate_font(self):
        size = self.rect[3]-10
        self.font = pygame.font.Font(self.fontname,size)
        
    def render_text(self):
        self.label = self.font.render(self.text, 1, self.fg)
        rect = self.label.get_rect(center=(self.label.get_width()/2, self.label.get_height()/2))
        self.labelrect = add_rect(rect, self.rect)
        
    def draw(self):
        #self.render_text()
        self.parent.blit(self.label, self.labelrect)
        
    def click(self):
        self.onClick(self)
        self.draw()
        
    def move(self, x=0, y=0):
        self.rect[0] = x
        self.rect[1] = y
        self.generate_rectangle()
        self.render_text()
        
    def resize(self, w=50, h=50):
        self.rect[2] = w
        self.rect[3] = h
        self.generate_rectangle()
        self.render_text()
    
    def set_text(self, text):
        self.text = text
        self.render_text()
        
    def get_text(self):
        return self.text   
        
    def set_color(self, color, TYPE="FG"):
        if isinstance(color, (tuple)) and len(color) == 3 and color[0] <= 255 and color[1] <= 255 and color[2] <= 255:
            if TYPE == "FG":
                self.fg = color
                self.generate_font()
            return 
        raise ValueError("Value must be a tuple with three elements, each less than or equal to 255. (R,G,B)")  
        
    def get_color(self, TYPE="FG"):
        if TYPE == "FG":
            return self.fg
