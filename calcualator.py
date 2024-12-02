import math
from tkinter import *
from tkinter import StringVar


def btn_enter(event):
    event.widget.config(background='green', foreground='white')
def btn_leave(event):
    event.widget.config(background='red', foreground='white')
def btn_click(event):
    clicked_btn=event.widget
    char=clicked_btn['text']
    if len(result.get()+char)<8:
        if char!='.' and char!='=':
            result.set(result.get()+char)
        result.set(result.get()+char)
    if char=='.' and '.' not in result.get():
        result.set(result.get()+char)
    if char=='=':
        result.set(eval(result.get()+char))
    if char=='SQ':
        result.set(math.sqrt(result.get()+char))
win=Tk()
win.title('calcualator')
win.geometry("500x500")


result=StringVar()
Entry(win,textvariable=result,font=('Arial',16),width=12).place(x=20,y=20)
labels=[['7','8','9','/'],
        ['4','5','6','*'],
        ['1','2','3','-'],
        ['0','.','=']
        ]
distance=40
x=20
y=100
width=4

for row in range(4):
    for col in range(5):
        print(labels[row][col])
        text=labels[row][col]
        btn=Button (win,text=text,width=width,bg='red')
        btn.place(x=x+col*distance,y=y+row*distance)
        btn.bind('<Enter>',btn_enter)
        btn.bind('<Leave>', btn_enter)
        btn.bind('<Buttonrelease>', btn_enter)
win.mainloop()
