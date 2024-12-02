from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import tkinter.filedialog as dialog

def close_form():
    if msg.askyesno('exit','do you want to exit?'):
        win.destroy()
def open_click():
    print(dialog.askopenfilename())
    print(dialog.askdirectory())
    print(dialog.asksaveasfilename())
win= Tk()
win.title('User')
win.geometry('500x500')
win.protocol('WM_DELETE_WINDOW', close_form)
win.resizable(width=True, height=False)
Button(win, text='open file', command=open_click).place(x=20,y=20)
Button(win, text='save file', command=open_click).place(x=20,y=80)
Button(win, text='color', command=open_click).place(x=20, y=1400)








win.mainloop()
