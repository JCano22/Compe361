#3. Write a Python GUI application with a main window that includes two buttons and a text field (TextCtrl). When the user clicks the first button, the application should store the number entered in the text field and then clear the text field. If the user clicks the second button, the application should display the stored number in the text field.

import wx

def btn1Click(evt):
    global memo
    memo = txt.GetValue()
    txt.SetValue("")

def btn2Click(evt):
    txt.SetValue(memo)

theApp = wx.App()
f = wx.Frame(parent = None, title = "Midterm-2 Q3", size = (300, 200))

txt = wx.TextCtrl(parent = f, size = (100, 25))
txt.SetPosition(wx.Point(5, 10))

btn1 = wx.Button(parent = f, size = (50, 25), label = "Hide")
btn1.SetPosition(wx.Point(5, 50))
btn1.Bind(wx.EVT_BUTTON, btn1Click)

btn2 = wx.Button(parent = f, size = (50, 25), label = "Show")
btn2.SetPosition(wx.Point(55, 50))
btn2.Bind(wx.EVT_BUTTON, btn2Click)

f.Show()
theApp.MainLoop()