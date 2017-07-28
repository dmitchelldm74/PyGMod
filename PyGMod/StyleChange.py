from threading import Thread
import time

def _function(target, delay, kwargs):
    time.sleep(delay)
    for k in kwargs:
        getattr(target, k)(*kwargs[k])
    

class StyleChange():
    def __init__(self, target=None):
        self.target = target
        
    def wait(self, delay, **kwargs):
        thread = Thread(target=_function, args=(self.target, delay, kwargs))
        thread.daemon = True
        thread.start()
