#3. Write a Python GUI application with a main window that includes two buttons and a text field (TextCtrl). When the user clicks the first button, the application should store the number entered in the text field and then clear the text field. If the user clicks the second button, the application should display the stored number in the text field.

import wx

def on_store(evt):
    global num
    if txt.GetValue() != "":
        num = txt.GetValue()
        txt.SetValue("")
    else:
        on_display()

def on_display():
    txt.SetValue(num)


app = wx.App()
f = wx.Frame(None, title="midterm", size = (300, 200))

txt = wx.TextCtrl(f, pos = (50, 50), size = (50, 20), value = "")

b1 = wx.Button(f, label = "click", pos = (50, 100), size =(50,20))
b1.Bind(wx.EVT_BUTTON, on_store)


f.Show()
app.MainLoop()
