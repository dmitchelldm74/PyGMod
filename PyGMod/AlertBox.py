from threading import Thread
import os, sys
from PyGMod import Application

def alertBox(text, title="Alert!"):
    app = Application(title, w=400, h=200)
    app.addElement("label", id="lb1", text=text, h=48)
    app.addElement("button", id="btn1", text="Ok", radius=0.3, onClick=lambda btn: app.exit())
    app.loop()
    
def startAlert(text):
    thread = Thread(target=os.system, args=('python -c "import PyGMod;PyGMod.alertBox(\'%s\')"'%(text), ))
    thread.daemon = True
    thread.start()
    
if __name__ == '__main__':
    alertBox(sys.argv[1])
