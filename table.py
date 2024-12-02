from tkinter import *
from tkinter.ttk import Treeview
def set_form():
    name.set('')
    family.set('')
    codemelli.set(0)
    codedaneshjooi.set(0)
def click():
    person=(name.get(),family.get(),codemelli.get(),codedaneshjooi.get())
    table.insert('',person)
    set_form()
win=Tk()
win.title('Table')
win.geometry('500x300')
Label(win,text='Name').place(x=900,y=50)
name=StringVar()
Entry(win,textvariable=name).place(x=940,y=50)
Label(win,text='Family').place(x=900,y=70)
family=StringVar()
Entry(win,textvariable=family).place(x=940,y=80)
Label(win,text='Codemelli').place(x=880,y=110)
codemelli=IntVar()
Entry(win,textvariable=codemelli).place(x=940,y=110)
Label(win,text='CodedaneshIooi').place(x=845,y=150)
codedaneshjooi=IntVar()
Entry(win,textvariable=codedaneshjooi).place(x=940,y=150)

table=Treeview(win,columns=[1,2,3,4],show='headings')
table.heading(1,text='name')
table.heading(2,text='family')
table.heading(3,text='codemelli')
table.heading(4,text='codedaneshjooi')
table.column(3,width=100)
table.column(4,width=100)
table.place(x=100, y=100)
Button(win,text="add",width=8,command=click and set_form).place(x=200, y=500)










win.mainloop()