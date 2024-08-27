from pywinauto import Desktop, Application

def ReplaceText(app, str1, str2):
    app.UntitledNotepad.menu_select("Edit->Replace")
    Replace_win = app.UntitledNotepad.child_window(title="Replace", class_name="#32770")
    Replace_win.FindwhatEdit.type_keys('^a^c{DELETE}')
    Replace_win.ReplaceWithEdit.type_keys('^a^c{DELETE}')
    Replace_win.FindwhatEdit.type_keys(str1)
    Replace_win.ReplaceWithEdit.type_keys(str2)
    if Replace_win.WrapAround == 1:
        Replace_win.WrapAround.click()
    Replace_win.ReplaceAll.click()

app = Application(backend="uia").start("notepad.exe")
app = Application(backend="uia").connect("notepad.exe")
app.UntitledNotepad.type_keys("This is my first sentence.", with_spaces=True)
ReplaceText(app, "sentence", "write")
