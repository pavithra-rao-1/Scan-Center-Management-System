from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import re
import os
import puduhome
import mysql.connector as sql

def patient_appo():
    appo_window=Tk()
    appo_window.title("Appointment")
    appo_window.geometry("1350x700+0+0")
    appo_window.resizable(False,False)
    
    def home_page():
        appo_window.destroy()
        puduhome.homepage(appo_window)
        
    frame=Frame(appo_window,bg="light gray")
    frame.place(x=1,y=1,height=700,width=1350)

    Button(frame,text="HOME",font=("Goudy old style",15,"bold"),command=home_page,cursor="hand2",fg="#3787d7",bd=1,bg="light gray").place(x=10,y=10,height=40,width=110)
    Label(appo_window,text="APPOINTMENT",font=("Goudy old style",30,"bold"),bg="light gray",fg="black").place(x=500,y=20)

    Label(frame,text="Name",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=90,height=40,width=300)
    t1=Entry(frame,font=("times new roman",15),bg="white")
    t1.place(x=250,y=90,height=40,width=300)

    Label(frame,text="DOB",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=170,height=40,width=300)
    t2=Entry(frame,font=("times new roman",15),bg="white")
    t2.place(x=250,y=170,height=40,width=300)

    Label(frame,text="Gender",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=250,height=40,width=300)
    var = IntVar()
    sel=StringVar()
    Radiobutton(appo_window, text="Male", variable=var, value=1,command=sel,font=("Goudy old style",15,"bold")).place(x=250,y=250,height=40,width=110)
    Radiobutton(appo_window, text="Female", variable=var, value=2,command=sel,font=("Goudy old style",15,"bold")).place(x=400,y=250,height=40,width=110)

    Label(frame,text="Address",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=330,height=40,width=300)
    t3=Entry(frame,font=("times new roman",15),bg="white")
    t3.place(x=250,y=330,height=40,width=300)

    Label(frame,text="Phone No.",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=410,height=40,width=300)
    t4=Entry(frame,font=("times new roman",15),bg="white")
    t4.place(x=250,y=410,height=40,width=300)

    Label(frame,text="Registration no.",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=2,y=490,height=40,width=300)
    t5=Entry(frame,font=("times new roman",15),bg="white")
    t5.place(x=250,y=490,height=40,width=300)

    Label(frame,text="Registration Date",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=90,height=40,width=300)
    t6=Entry(frame,font=("times new roman",15),bg="white")
    t6.place(x=870,y=90,height=40,width=300)

    Label(frame,text="Hospital ref. by",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=170,height=40,width=300)
    t7=Entry(frame,font=("times new roman",15),bg="white")
    t7.place(x=870,y=170,height=40,width=300)

    Label(frame,text="Test date",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=250,height=40,width=300)
    t8=Entry(frame,font=("times new roman",15),bg="white")
    t8.place(x=870,y=250,height=40,width=300)
            
    Label(frame,text="Test Type",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=330,height=40,width=300)
    listy=["XRay","ECG","CT Scan","MRI Scan","Cardian CT"]
    sel=StringVar()
    #sel.set("check")
    menu=ttk.Combobox(appo_window,textvariable=sel,values=listy)
    menu.place(x=870,y=330,height=40,width=300)

    Label(frame,text="Doctor",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=410,height=40,width=300)
    t9=Entry(frame,font=("times new roman",15),bg="white")
    t9.place(x=870,y=410,height=40,width=300)

    Label(frame,text="Fees",font=("Goudy old style",20,"bold"),fg="black",bg="light gray").place(x=570,y=490,height=40,width=300)
    t10=Entry(frame,font=("times new roman",15),bg="white")
    t10.place(x=870,y=490,height=40,width=300)
    radio=''
    def add_to_sql():
        global radio
        hospital1=0
        hospital2=0
        hosp3=0
        T1=t1.get()
        T2=t2.get()
        T3=t3.get()
        T4=t4.get()
        if not T4.isdigit() or len(str(T4))!=10:
            messagebox.showerror('Error','Enter your phone number properly')
        else:
            hospital1=1
        T5=t5.get()
        if not T5.isdigit():
            messagebox.showerror('Error','Enter your registration ID properly')

        else:
            hospital2=2
        T6=t6.get()
        T7=t7.get()
        T8=t8.get()
        T9=t9.get()        
        T11=var.get() #male/female
        if T11==1:
            radio='Male'
        if T11==2:
            radio='Female'
        T12=menu.get() #optionbox
        ch='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.'
        for i in T1:
            if i not in ch:
                messagebox.showerror('Error','Enter your name properly')
                hosp3=0
                break
            else:
                hosp3=3
                continue
        T10=t10.get()
        if hospital1==1 and hospital2==2 and hosp3==3:
            
            if T1=="" or T2=="" or T3=="" or T4=="" or T5=="" or T6=="" or T7=="" or T8=="" or T9=="" or T10=="" or radio=="" or T12=="":
                messagebox.showerror('Error','All fields are required')
            else:
                try:
                    con=sql.connect(host="localhost",user="root",password="keerthi",database="MDBA")
                    cr=con.cursor()
                    cr.execute("insert into appo values('"+T1+"','"+T2+"','"+radio+"','"+T3+"',"+T4+","+T5+",'"+T6+"','"+T7+"','"+T8+"','"+T12+"','"+T9+"',"+T10+")")
                    cr.execute("commit")
                    messagebox.showinfo('Insert Query Info','Value Added successfully..')
                    con.close()
                except:
                    messagebox.showerror("Error","Registration ID already exist")
    add=Button(frame,text="ADD",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light gray",command=add_to_sql).place(x=660,y=570,height=40,width=110)
    appo_window.mainloop()

