from tkinter import *
from tkinter import font
def btnclick(numbar):
    global val
    val=val+str(numbar)
    data.set(val)
def btnclear():
    global val
    val=""
    data.set("")
def btneqals():
    global val
    result=str(eval(val))
    data.set(result)
root=Tk()
root.title("Calculator My First GUI Application")
root.geometry("361x381+500+200")
val=""
data=StringVar()
display=Entry(root,textvariable=data,bd=29,justify="right",bg="yellow",font=("arial",20))
display.grid(row=1,columnspan=4)
#********************************button*****************************************
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(9))
btn9.grid(row=12,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(8))
btn8.grid(row=12,column=1)

btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(7))
btn7.grid(row=12,column=2)

btnadd=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("+"))
btnadd.grid(row=12,column=3)

btnsix=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(6))
btnsix.grid(row=13,column=0)

btnfive=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(5))
btnfive.grid(row=13,column=1)

btnfor=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(4))
btnfor.grid(row=13,column=2)

btnm=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("-"))
btnm.grid(row=13,column=3)



btnthree=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(3))
btnthree.grid(row=14,column=0)

btntwo=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(2))
btntwo.grid(row=14,column=1)

btnone=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(1))
btnone.grid(row=14,column=2)
btnin=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("*"))
btnin.grid(row=14,column=3)

btndiv=Button(root,text="%",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("%"))
btndiv.grid(row=15,column=0)

btnzero=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(0))
btnzero.grid(row=15,column=1)
btnc=Button(root,text="c",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnclear)
btnc.grid(row=15,column=2)
btneq=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btneqals)
btneq.grid(row=15,column=3)



root.mainloop()
