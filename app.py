from PyGMod import alert, StyleChange, PyGModCore as gcore

def finish(app):
    alert(app.getById("tb1").value)

def btn1_onclick(btn):
    global app
    btn.set_color((100,100,200))
    app.getById("tb1").clear()
    stylechange = StyleChange(btn)
    stylechange.wait(1.0, set_color=((200,20,20), ))
    
def tb1_onSubmit(tb):
    global app
    app.set_title(tb.value)

app = gcore.Application("title", 300, 300)
app.addElement("textbox", id="tb1", text="Name", onSubmit=tb1_onSubmit)
app.addElement("button", id="btn1", text="Clear", onClick=btn1_onclick, bg=(200,20,20), rounded=1.0)
app.onFinish = finish
app.loop()
