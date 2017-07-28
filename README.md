# PyGMod
Graphics Module for Python 2.7

### (Python 3.5 release coming soon!)

## Install
`python setup.py install`

**Creating an application is simple with PyGMod!**
1.  Create a directory for your application
2.  Create a file called `app.py`
3.  Copy PyGMod's helloworld app:
```
from PyGMod import PyGModCore as gcore

def btn1_onclick(btn):
    global app
    btn.set_color((100,100,200))
    app.getById("tb1").clear()
    
def tb1_onSubmit(tb):
    global app
    app.set_title(tb.value)

app = gcore.Application("title", 300, 300)

app.addElement("textbox", id="tb1", text="Name", onSubmit=tb1_onSubmit)
app.addElement("button", id="btn1", text="Clear", onClick=btn1_onclick, bg=(200,20,20), rounded=1.0)
app.loop()
```
