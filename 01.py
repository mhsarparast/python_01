from tkinter import *
calcualator=Tk()
calcualator.title('calcualator')
calcualator.geometry("500x500")
text_name=Entry(calcualator)
text_name.place(x=100,y=50)
btn1=Button(calcualator,text='7',width=8,height=4,bg='red')
btn1.place(x=100,y=100)
btn2=Button(calcualator,text='4',width=8,height=4,bg='red')
btn2.place(x=100,y=180)
btn3=Button(calcualator,text='1',width=8,height=4,bg='red')
btn3.place(x=100,y=260)
btn4=Button(calcualator,text='o',width=8,height=4,bg='red')
btn4.place(x=100,y=340)
btn5=Button(calcualator,text='.',width=8,height=4,bg='red')
btn5.place(x=180,y=340)
btn6=Button(calcualator,text='2',width=8,height=4,bg='red')
btn6.place(x=180,y=260)
btn7=Button(calcualator,text='5',width=8,height=4,bg='red')
btn7.place(x=180,y=180)
btn7=Button(calcualator,text='8',width=8,height=4,bg='red')
btn7.place(x=180,y=100)
btn8=Button(calcualator,text='9',width=8,height=4,bg='red')
btn8.place(x=260,y=100)
btn9=Button(calcualator,text='6',width=8,height=4,bg='red')
btn9.place(x=260,y=180)
btn10=Button(calcualator,text='3',width=8,height=4,bg='red')
btn10.place(x=260,y=260)
btn11=Button(calcualator,text='=',width=8,height=4,bg='red')
btn11.place(x=260,y=340)
btn12=Button(calcualator,text='/',width=8,height=4,bg='red')
btn12.place(x=340,y=100)
btn13=Button(calcualator,text='*',width=8,height=4,bg='red')
btn13.place(x=340,y=180)
btn14=Button(calcualator,text='-',width=8,height=4,bg='red')
btn14.place(x=340,y=260)
btn15=Button(calcualator,text='+',width=8,height=4,bg='red')
btn15.place(x=340,y=340)




calcualator.mainloop()