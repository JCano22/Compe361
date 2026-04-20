#3. Write a Python GUI application with a main window that includes two buttons and a text field (TextCtrl). When the user clicks the first button, the application should store the number entered in the text field and then clear the text field. If the user clicks the second button, the application should display the stored number in the text field.

import wx


def on_store(evt):
    global stored_num
    stored_num = t.GetValue()
    t.SetValue("")

def on_display(evt):
    t.SetValue(stored_num)


app = wx.App()
f = wx.Frame(None, title="Midterm 2 Q3", size=(300, 200))

b1 = wx.Button(f, label="Store Number", pos=(50, 100))
b1.SetSize((100, 30))
b1.Bind(wx.EVT_BUTTON, on_store)

b2 = wx.Button(f, label="Display Number", pos=(150, 100))
b2.SetSize((100, 30))
b2.Bind(wx.EVT_BUTTON, on_display)

t = wx.TextCtrl(f, pos=(50, 50), size=(200, 30), value=(""))

f.Show()
app.MainLoop()
