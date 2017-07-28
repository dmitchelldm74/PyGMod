def add_rect(rect, other):
    rect[0] += other[0]
    rect[1] += other[1]
    rect[2] += other[2]
    rect[3] += other[3]
    return rect

class Blob():
    def __init__(self):
        self.value = ""
        self.text = ""
        self.Submit = lambda: None
        self.editable = True

class Toggle():
    def __init__(self, function1=lambda: None, function2=lambda: None):
        self.current = 0
        self.function1 = function1
        self.function2 = function2
        
    def change(self, *args):
        if self.current == 0:
            self.function1(*args)
            self.current = 1
        elif self.current == 1:
            self.function2(*args)
            self.current = 0
