import pygame
import sys, time
from TextBox import *
from Button import *
from TextArea import *
from ListBox import *
from EventManager import *
from Label import *
from objects import Toggle

pygame.init()
    
class Application():
    event_map = {}
    objects = []
    id_map = {}
    def __init__(self, title, w=300, h=300, bg=(255,255,255), fontsize=40, spacing=25):
        self.bg = bg
        self.Running = True
        self.set_title(title)
        self.scr = pygame.display.set_mode((w, h))
        self.fill()
        self.evt = Events()
        self.relx = fontsize + 10
        self.rely = w
        self.x = 50
        self.y = 50
        self.spacing = spacing
        
    def set_title(self, title):
        pygame.display.set_caption(title)
        
    def fill(self):
        self.scr.fill(self.bg)
        
    def add_event(self, event_name, function):
        self.event_map[event_name] = function
        
    def delete_event(self, event_name):
        del self.event_map[event_name]
        
    def addElement(self, elname, **kwargs):
        elname = elname.lower()
        if len(self.objects) != 0:
            size = self.objects[-1]
            self.y = size.rect[1] + size.rect[3] + self.spacing
        if elname == "button":
            self.objects.append(Button(self.scr, (self.x, self.y, self.rely-(self.relx*2), kwargs.get("h", self.relx)), kwargs.get("text", "None"), kwargs.get("onClick", lambda btn:None), kwargs.get("bg",(200,200,200)), kwargs.get("rounded", 0), kwargs.get("font", "freesansbold.ttf"), fg=kwargs.get("fg", (255,255,255)), event_manager=self.evt))
        elif elname == "textbox":
            self.objects.append(TextBox(self.scr, (self.x, self.y, self.rely-(self.relx*2), kwargs.get("h", self.relx)), kwargs.get("text", "None"), onSubmit=kwargs.get("onSubmit", lambda btn:None), color=kwargs.get("bg",(200,200,200)), font=kwargs.get("font", "freesansbold.ttf"), focus_color=kwargs.get("focus_color", (170,170,170)), fg=kwargs.get("fg", (255,255,255)), value=kwargs.get("value",""), event_manager=self.evt))
        elif elname == "listbox":
            self.objects.append(ListBox(self.scr, (self.x, self.y, self.rely-(self.relx*2), kwargs.get("h", self.relx)), kwargs.get("text", "None"), onSubmit=kwargs.get("onSubmit", lambda btn:None), color=kwargs.get("bg",(200,200,200)), font=kwargs.get("font", "freesansbold.ttf"), focus_color=kwargs.get("focus_color", (100,100,200)), fg=kwargs.get("fg", (255,255,255)), value=kwargs.get("value",""), lines=kwargs.get("lines", 3), event_manager=self.evt))
        elif elname == "textarea":
            self.objects.append(TextArea(self.scr, (self.x, self.y, self.rely-(self.relx*2), kwargs.get("h", self.relx)), kwargs.get("text", "None"), onSubmit=kwargs.get("onSubmit", lambda btn:None), color=kwargs.get("bg",(200,200,200)), font=kwargs.get("font", "freesansbold.ttf"), focus_color=kwargs.get("focus_color", (170,170,170)), fg=kwargs.get("fg", (255,255,255)), value=kwargs.get("value",""), lines=kwargs.get("lines", 3), event_manager=self.evt))
        elif elname == "label":
            self.objects.append(Label(self.scr, (self.x, self.y, self.rely-(self.relx*2), kwargs.get("h", self.relx)), kwargs.get("text", "None"), kwargs.get("onClick", lambda btn:None), kwargs.get("font", "freesansbold.ttf"), fg=kwargs.get("fg", (0,0,0)), event_manager=self.evt))
        else:
            return
        self.id_map[kwargs.get("id","_temp")] = len(self.objects)-1
        
    def deleteElement(self, id):
        loc = self.id_map[id]
        self.evt.delete(self.objects[loc])
        del self.objects[loc]
            
    def getById(self, id):
        return self.objects[self.id_map[id]]
        
    def loop(self):
        while self.Running == True:
            self.scr.fill(self.bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if hasattr(self, "onFinish"):
                        self.onFinish(self)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.evt.button_check()
                elif event.type == pygame.KEYDOWN:
                    self.evt.send(event.key)
                elif event.type in self.event_map:
                    self.event_map[event.type](event)
            if hasattr(self, "inLoop"):
                self.inLoop()        
            self.evt.draw()
            pygame.display.flip()
            
    def exit(self):
        self.Running = False

#tbi = pygame.image.load("textbox.png")
#tbi = pygame.transform.scale(tbi, (tb.rect[2], tb.rect[3]))
#tbi.convert()
#tb.rectangle = tbi
# OLD CODE
"""
def n_main():
    pygame.display.set_caption("PyGraphics")
    scr = pygame.display.set_mode((800,800))
    scr.fill((255,255,255))
    evt = Events()
    toggle = Toggle(lambda button: [button.set_color((20,200,20)), button.set_text("Go!")], lambda button: [button.set_color((200,20,20)), button.set_text("Stop!")])
    btn = Button(scr,(50,50,200,50), "Stop!", toggle.change, (200,20,20), 1.0, event_manager=evt)
    btn2 = Button(scr,(0,0,40,40), "X", lambda btn: sys.exit(), (200,20,20), event_manager=evt)
    btn3 = Button(scr,(50,300,110,50), "Clear", lambda btn: [tb.clear(), mtb.clear()], (200,20,20), event_manager=evt)
    tb = TextBox(scr,(50,200,700,50), "Name", event_manager=evt)
    
    tb.onSubmit = lambda tb: pygame.display.set_caption(tb.value)
    # mtb = MultilineTextBox(scr,(50,500,700,50), "Name", event_manager=evt, lines=4)
    lbox = ListBox(scr,(50,500,700,50), "Name\nEmail\nDate\nTime", event_manager=evt, lines=4)
    gameloop = True
    while gameloop == True:
        #btn2.move(btn2.rect[0]+1,0)
        #btn2.resize(50,btn2.rect[3]+1)
        scr.fill((235,235,235))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(lbox.value)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                evt.button_check()
            elif event.type == pygame.KEYDOWN:
                evt.send(event.key)
        evt.draw()
        pygame.display.flip()
"""
        
