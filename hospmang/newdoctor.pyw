from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import homepage
import mysql.connector as sql

def doc_app():
    global radio,t2,t3,t4,t5,t6,t7,t8,t9,t1
    doc_win=Tk()
    doc_win.title("New Doctor Application")
    doc_win.geometry("1350x700+0+0")
    doc_win.resizable(False,False)
    
    def home_page():
        doc_win.destroy()
        homepage.homepage(doc_win)
        
    frame=Frame(doc_win,bg="light gray")
    frame.place(x=1,y=1,height=700,width=1350)

    Button(frame,text="HOME",font=("Goudy old style",15,"bold"),command=home_page,cursor="hand2",fg="#3787d7",bd=1,bg="light gray").place(x=10,y=10,height=40,width=110)
    Label(doc_win,text="NEW DOCTOR APPLICATION",font=("Goudy old style",30,"bold"),bg="light gray",fg="black").place(x=500,y=20)

    Label(frame,text="Name",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=90,height=40,width=300)
    t1=Entry(frame,font=("times new roman",15),bg="white")
    t1.place(x=250,y=90,height=40,width=300)

    Label(frame,text="DOB",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=170,height=40,width=300)
    t2=Entry(frame,font=("times new roman",15),bg="white")
    t2.place(x=250,y=170,height=40,width=300)

    Label(frame,text="Gender",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=250,height=40,width=300)
    var = IntVar()
    sel=StringVar()
    Radiobutton(doc_win, text="Male", variable=var, value=1,command=sel,font=("Goudy old style",15,"bold")).place(x=250,y=250,height=40,width=110)
    Radiobutton(doc_win, text="Female", variable=var, value=2,command=sel,font=("Goudy old style",15,"bold")).place(x=400,y=250,height=40,width=110)

    Label(frame,text="Address",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=330,height=40,width=300)
    t3=Entry(frame,font=("times new roman",15),bg="white")
    t3.place(x=250,y=330,height=40,width=300)

    Label(frame,text="Phone No.",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=410,height=40,width=300)
    t4=Entry(frame,font=("times new roman",15),bg="white")
    t4.place(x=250,y=410,height=40,width=300)

    Label(frame,text="Teresa Scan ID",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=490,height=40,width=300)
    t5=Entry(frame,font=("times new roman",15),bg="white")
    t5.place(x=250,y=490,height=40,width=300)

    Label(frame,text="Qualification",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=170,height=40,width=300)
    t6=Entry(frame,font=("times new roman",15),bg="white")
    t6.place(x=870,y=170,height=40,width=300)

    Label(frame,text="Specialist",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=250,height=40,width=300)
    t7=Entry(frame,font=("times new roman",15),bg="white")
    t7.place(x=870,y=250,height=40,width=300)
            
    Label(frame,text="Email ID",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=330,height=40,width=300)
    t8=Entry(frame,font=("times new roman",15),bg="white")
    t8.place(x=870,y=330,height=40,width=300)

    Label(frame,text="Medical License ID",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=410,height=40,width=300)
    t9=Entry(frame,font=("times new roman",15),bg="white")
    t9.place(x=870,y=410,height=40,width=300)

    radio=''
    def add_to_sql():
        global radio,t2,t3,t4,t5,t6,t7,t8,t9,t1
        hospital1=0
        hospital2=0
        hospital3=0
        hospital4=0
        hosp5=0
        T1=t1.get()
        T2=t2.get()
        T3=t3.get()
        T4=t4.get()
        T5=t5.get()
        T6=t6.get()     
        T10=var.get() #male/female
        if T10==1:
            radio='Male'
        if T10==2:
            radio='Female'
        T8=t8.get()
        ch='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.'
        for i in T1:
            if i not in ch:
                messagebox.showerror('Error','Enter your name properly')
                hosp5=0
                break
            else:
                hosp5=5
                continue
        T9=t9.get()
        if (not T4.isdigit()) or len(T4)!=10:
            messagebox.showerror('Error','Enter your phone number properly')
        else:
            hospital1=1
            
        if not T5.isdigit():
            messagebox.showerror('Error','Enter your Teresa Scan ID properly')            
        else:
            hospital2=2
            
        if not T9.isdigit():
            messagebox.showerror('Error','Enter your Medical License ID properly')            
        else:
            hospital3=3
            
        if T8[-10:]!='@gmail.com':
            messagebox.showerror("Error","Enter Email ID properly!!")            
        else:
            hospital4=4
            
        T7=t7.get()
        if hospital1==1 and hospital2==2 and hospital3==3 and hospital4==4 and hosp5==5:    
            if T1=="" or T2=="" or T3=="" or T4=="" or T5=="" or T6=="" or T7=="" or T8=="" or T9=="" or radio=="":
                messagebox.showerror('Error','All fields are required')
            else:
                try:
                    con=sql.connect(host="localhost",user="root",password="keerthi",database="MDBA")
                    cr=con.cursor()
                    cr.execute("insert into doct values('"+T1+"','"+T2+"','"+radio+"','"+T3+"',"+str(T4)+","+str(T5)+",'"+T6+"','"+T7+"','"+T8+"','"+T9+"')")
                    cr.execute("commit")
                    messagebox.showinfo('Insert Query Info','Value Added successfully..')
                    con.close()
                except:
                    messagebox.showerror("Error","Medical License Number already exist")

        
    add=Button(frame,text="ADD",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light gray",command=add_to_sql).place(x=660,y=570,height=40,width=110)
    doc_win.mainloop()

        
