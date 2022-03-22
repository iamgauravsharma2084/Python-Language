from tkinter import *
from tkinter import ttk
import pymysql
class student:
    def __init__(self,root):
#all display
        self.root=root
        self.root.title("Student management system")
        self.root.geometry("1350x700+0+0")
#frame name
        title=Label(self.root,text="Radha Inter College Dhampur",bd=10,relief=GROOVE,font=("7",40,"normal"),bg="black",fg="pink")
        title.pack(side=TOP,fill=X)

        #***************************ALLL vaseriable****************************************
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.emal_var=StringVar()
        self.grnder_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self._var=StringVar()




#Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)
        m_title=Label(Manage_Frame,text="Manage stduent",bg="crimson",fg="yellow",font=("7",30,"bold")) #jo jo hum frame per hona chi
        m_title.grid(row=0,columnspan=2,pady=20)

#iNFOR Total
        lbl_roll=Label(Manage_Frame,text="Roll No",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

#Ek function hai Entry
        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE) #jo jo hum frame per hona chi
        txt_Roll.grid(row=1,column=1,padx=20,pady=10,sticky="w")


#iNFOR Total
        lbl_Name=Label(Manage_Frame,text="Name",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_Name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
#Ek function hai Entry user se input karne
        txt_Name=Entry(Manage_Frame,textvariable=self.name_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE) #jo jo hum frame per hona chi
        txt_Name.grid(row=2,column=1,padx=20,pady=10,sticky="w")


#iNFOR Total
        lbl_email=Label(Manage_Frame,text="Email",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
#Ek function hai Entry
        txt_email=Entry(Manage_Frame,textvariable=self.emal_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE) #jo jo hum frame per hona chi
        txt_email.grid(row=3,column=1,padx=20,pady=10,sticky="w")

#iNFOR Total
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
#Ek function hai Entry
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.grnder_var,font=("7",14,"bold"),state='readonly')
        combo_gender["values"]=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)


#iNFOR Total
        lbl_Contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
#Ek function hai Entry
        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE) #jo jo hum frame per hona chi
        txt_Contact.grid(row=5,column=1,padx=20,pady=10,sticky="w")

#iNFOR Total
        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")
#Ek function hai Entry
        txt_DOS=Entry(Manage_Frame,textvariable=self.dob_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE) #jo jo hum frame per hona chi
        txt_DOS.grid(row=6,column=1,padx=20,pady=10,sticky="w")

#iNFOR Total
        lbl_address=Label(Manage_Frame,text="Address",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
#Ek function hai Entry
        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("7",10,"bold"))
        self.txt_address.grid(row=7,column=1,padx=20,pady=10,sticky="w")

#Button frame
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=15,y=500,width=420)
        
        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=1,column=1,padx=10)
        updatabtn=Button(btn_Frame,text="update",width=10).grid(row=1,column=2,padx=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=1,column=3,padx=10)
        clerbtn=Button(btn_Frame,text="clear",width=10,command=self.clear).grid(row=1,column=4,padx=10)



#Detail Frame      
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=830,height=560)

        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="yellow",font=("7",20,"bold")) #jo jo hum frame per hona chi
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("7",14,"bold"),state='readonly')
        combo_search["values"]=("Roll no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10) 

        txt_search=Entry(Detail_Frame,font=("time new roman",14,"bold"),bd=5,relief=GROOVE) #jo jo hum frame per hona chi
        txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
        searchbtn=Button(Detail_Frame,text="Show all",width=10).grid(row=0,column=4,padx=9,pady=10)

#******************************Table Frame*****************************
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=40,y=70,width=760,height=480)  #X=10
        
#*******************Scroll bar******************************************
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL) #xscrollcommand=scroll_x.set
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)   #yscrollcommand=scroll_y.set
        student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Roll",text="Roll No.")
        student_table.heading("Name",text="Name.")
        student_table.heading("Email",text="Email.")
        student_table.heading("Gender",text="Gender.")
        student_table.heading("Contact",text="Contact.")
        student_table.heading("DOB",text="DOB.")
        student_table.heading("Address",text="Address.")
        student_table['show']='headings'

        student_table.column("Roll",width=100)
        student_table.column("Name",width=100)
        student_table.column("Email",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Contact",width=100)
        student_table.column("DOB",width=100)
        student_table.column("Address",width=150)
        student_table.pack(fill=BOTH,expand=1)
    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.name_var.get(),
                                                                         self.emal_var.get(),
                                                                         self.grnder_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_address.get('1.0',END)
                                                                         ))
        con.commit()
        self.clear()
        con.close()
    def clear(self):
            self.Roll_No_var.set("")
            self.name_var.set("")
            self.emal_var.set("")
            self.grnder_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_address.delete.set("1.0",END)




root=Tk()
ob=student(root)
root.mainloop()