
from tkinter import *
import tkinter.messagebox
board=Tk()
board.title("Tic Toc Game")
board.geometry("700x500+0+0")
p1_score=StringVar()
p2_score=StringVar()
p3_score=StringVar()
p4_score=StringVar()
p5_score=StringVar()
player1=StringVar()
player2=StringVar()
flag=True
ptr1=0
ptr2=0
pte3=0
ptr4=0
ptr5=0
ctr=1





def play(btn):
    global flag,ctr 
    if btn["text"]==" " and flag==True:
        flag=False
        btn["text"]="X"
        ctr+=1
        check()
    elif btn["text"]==" " and flag==False:
        flag=True 
        btn["text"]="O"
        ctr+=1
        check()
    else:
        tkinter.messagebox.showinfo("Learn TechTotech","Not allowed")  


fr=Frame(board,bg="crimson")
fr.place(x=350,y=105,width=340,height=390)



#*****************************************************CONDTON CHEC X***************************************
fr1=Frame(board,bg="crimson")
fr1.place(x=6,y=390,width=339,height=105)
def check():
    global ptrl,ptr2,p1_score,p2_score,ctr
    if(A1["text"]=="X" and B2["text"]=="X" and C3["text"]=="X"):
        ib1=Label(fr,text="1 2 3",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(D4["text"]=="X" and E5["text"]=="X" and F6["text"]=="X"):
        ib1=Label(fr,text="4 5 6",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")
        clearButton()

    if(G7["text"]=="X" and H8["text"]=="X" and I9["text"]=="X"):
        ib1=Label(fr,text="7 8 9",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(A1["text"]=="X" and E5["text"]=="X" and I9["text"]=="X"):
        ib1=Label(fr,text="1 5 9",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(A1["text"]=="X" and E5["text"]=="X" and H8["text"]=="X"):
        ib1=Label(fr,text="1 5 8",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(C3["text"]=="X" and F6["text"]=="X" and I9["text"]=="X"):
        ib1=Label(fr,text="3 6 9",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")
    if(C3["text"]=="X" and E5["text"]=="X" and G7["text"]=="X"):
        ib1=Label(fr,text="3 5 7",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(A1["text"]=="X" and D4["text"]=="X" and G7["text"]=="X"):
        ib1=Label(fr,text="1 4 7",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(B2["text"]=="X" and E5["text"]=="X" and H8["text"]=="X"):
        ib1=Label(fr,text="2 5 8",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(G7["text"]=="X" and F6["text"]=="X" and I9["text"]=="X"):
        ib1=Label(fr,text="7 6 9",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 1 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")
#*****************************************************CONDTON CHEC Y ***************************************
    elif(A1["text"]=="O" and B2["text"]=="O" and C3["text"]=="O"):
        ib1=Label(fr,text="1 2 3",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 2 win")
 
    if(D4["text"]=="O" and E5["text"]=="O" and F6["text"]=="O"): 
        ib1=Label(fr,text="4 5 6",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 2 win")

    if(G7["text"]=="O" and H8["text"]=="O" and I9["text"]=="O"):
        ib1=Label(fr,text="7 8 9",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 2 win")

    if(A1["text"]=="O" and E5["text"]=="O" and I9["text"]=="O"):
        ib1=Label(fr,text="1 5 9",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 1 win")

    if(C3["text"]=="O" and E5["text"]=="O" and G7["text"]=="O"):
        ib1=Label(fr,text="3 5 7",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 2 win")

    if(A1["text"]=="O" and D4["text"]=="O" and G7["text"]=="O"):
        ib1=Label(fr,text="1 4 7",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13) 
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 2 win")

    if(B2["text"]=="O" and E5["text"]=="O" and H8["text"]=="O"):
        ib1=Label(fr,text="2 5 8",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 2 win")

    if(G7["text"]=="O" and F6["text"]=="O" and I9["text"]=="O"):
        ib1=Label(fr,text="7 6 9",fg="yellow",bg="black",font=("17",15,"normal"))
        ib1.place(x=45,y=13)
        ib2=Label(fr1,text="Player 2 win  ",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)
        clearButton()
        tkinter.messagebox.showinfo("Tic tac toe","Player 2 win")
    elif(ctr==9):             
        tkinter.messagebox.showinfo("Tic tac toe","It d a tie")
        ib2=Label(fr1,text="Drawn Match",bg="crimson",fg="yellow",font=("7",30,"normal"))
        ib2.place(x=60,y=20)

        clearButton()

def clearButton():
    A1["text"]=" "
    B2["text"]=" "
    C3["text"]=" "
    D4["text"]=" "
    E5["text"]=" "
    F6["text"]=" "
    G7["text"]=" "
    H8["text"]=" "
    I9["text"]=" "
      
    
lbl=Label(board,text="Tic Tac Game",bd=20,relief=SUNKEN,font=("7",50,"normal"),bg="black",fg="yellow")
lbl.place(x=1,y=1,width=700,height=100)



A1=Button(board,text=" ",bg="RED",font=("times 15 normal"),width=9,height=3,command=lambda:play(A1))
A1.place(x=7,y=105)

B2=Button(board,text=" ",bg="RED",font=("times 15 normal"),width=9,height=3,command=lambda:play(B2))
B2.place(x=120,y=105)

C3=Button(board,text=" ",bg="RED",font=("times 15 normal"),width=9,height=3,command=lambda:play(C3))
C3.place(x=233,y=105)

D4=Button(board,text=" ",bg="yellow",font=("times,15,normal"),width=11,height=4,command=lambda:play(D4))
D4.place(x=7,y=200)

E5=Button(board,text=" ",bg="yellow",font=("times,15,normal"),width=11,height=4,command=lambda:play(E5))
E5.place(x=120,y=200)

F6=Button(board,text=" ",bg="yellow",font=("times,15,normal"),width=11,height=4,command=lambda:play(F6))
F6.place(x=233,y=200)



G7=Button(board,text=" ",bg="blue",font=("times,15,normal"),width=11,height=4,command=lambda:play(G7))
G7.place(x=7,y=300)

H8=Button(board,text=" ",bg="blue",font=("times,15,normal"),width=11,height=4,command=lambda:play(H8))
H8.place(x=120,y=300)

I9=Button(board,text=" ",bg="blue",font=("times,15,normal"),width=11,height=4,command=lambda:play(I9))
I9.place(x=233,y=300)



fr=Frame(board,bg="crimson")
fr.place(x=350,y=105,width=340,height=390)

lbll=Label(fr,text=" ",bd=20,relief=SUNKEN,font=("7",50,"normal"),bg="black",fg="yellow")
lbll.place(x=1,y=2,width=150,height=50)


labB=Label(fr,text="Win",font=("Times",15,"normal"),relief=SUNKEN,bg="blue")
labB.place(x=170,y=9,width=70,height=30)

labc=Label(fr,text="Won",font=("Times",15,"normal"),relief=SUNKEN,bg="blue")
labc.place(x=260,y=9,width=70,height=30)


lab=Label(fr,text="Player 1",font=("Times",15,"normal"),relief=SUNKEN,bg="blue")
lab.place(x=1,y=50,width=150,height=30)

en=Entry(fr,textvariable=p1_score,font=("7",15,"normal"),bg="crimson")
en.place(x=170,y=50,width=70,height=30)

en1=Entry(fr,textvariable=p4_score,font=("7",15,"normal"),bg="crimson")
en1.place(x=260,y=50,width=70,height=30)



labb=Label(fr,text="Player 2",font=("Times",15,"normal"),relief=SUNKEN,bg="blue")
labb.place(x=1,y=90,width=150,height=30)

enn=Entry(fr,textvariable=p2_score,font=("7",15,"normal"),bg="crimson",fg="black")
enn.place(x=170,y=90,width=70,height=30)

enn2=Entry(fr,textvariable=p5_score,font=("7",15,"normal"),bg="crimson",fg="black")
enn2.place(x=260,y=90,width=70,height=30)

labbb=Label(fr,text="Drawn Match",font=("Times",15,"normal"),relief=SUNKEN,bg="blue")
labbb.place(x=1,y=140,width=150,height=30)
ennn=Entry(fr,textvariable=p3_score,font=("7",15,"normal"),bg="crimson",fg="black")
ennn.place(x=170,y=140,width=70,height=30)

ennnV=Entry(fr,font=("7",15,"normal"),bg="crimson",fg="black")
ennnV.place(x=260,y=140,width=70,height=30)





botton=Button(fr,text="clrscr",bg="blue",fg="yellow")
botton.place(x=250,y=240,width=80,height=30)

labbbB=Label(fr,text="Player 1 Symbol X",font=("Times",15,"normal"),relief=SUNKEN,bg="blue")
labbbB.place(x=1,y=180,width=160,height=30)

labbbBb=Label(fr,text="Player 2 Symbol O",font=("Times",15,"normal"),relief=SUNKEN,bg="blue")
labbbBb.place(x=170,y=180,width=160,height=30)





board.mainloop()