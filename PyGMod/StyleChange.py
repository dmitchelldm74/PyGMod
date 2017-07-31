from threading import Thread
import time

def _function(target, delay, kwargs, onFinish):
    time.sleep(delay)
    for k in kwargs:
        getattr(target, k)(*kwargs[k])
    onFinish(target)
    

class StyleChange():
    def __init__(self, target=None):
        self.target = target
        self.onFinish = lambda btn: None
        
    def wait(self, delay, **kwargs):
        thread = Thread(target=_function, args=(self.target, delay, kwargs, self.onFinish))
        thread.daemon = True
        thread.start()
