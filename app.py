from PyGMod import PyGModCore as gcore

def finish(app):
    print(app.getById("tb1").value)

app = gcore.Application("PyGraphics", 800, 800, (235,235,235))
toggle = gcore.Toggle(lambda button: [button.set_color((20,200,20)), button.set_text("Go!")], lambda button: [button.set_color((200,20,20)), button.set_text("Stop!")])
app.addElement("button", id="btn1", text="Stop!", onClick=toggle.change, bg=(200,20,20), rounded=1.0)
app.getById("btn1").resize(700,80)
app.addElement("button", id="btn2", text="Blue", bg=(20,20,200), rounded=1.0)
app.deleteElement("btn2")
app.addElement("textarea", id="tb1", text="Name\nEmail\nDate")
app.onFinish = finish
app.loop()
