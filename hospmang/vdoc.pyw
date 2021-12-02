from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
import homepage

def v_doc():
    global vdoc
    vdoc=Tk()
    vdoc.title('VIEW DOCTORS')
    vdoc.geometry('1200x600+60+10')
    frame = Frame(vdoc,bg='aquamarine2',width=1200,height=650).place(x=1,y=1)
    
    def homep():
        global vdoc
        vdoc.destroy()
        homepage.homepage(vdoc)

    a=120
    b=200
    c=280
    d=360
    e=440
    f=520   

    con=sql.connect(host="localhost",user="root",password="keerthi",database="MDBA")
    cr=con.cursor()
    cr.execute("select * from doct")
    #cr.execute("commit")
    rows=cr.fetchall()
    con.close()

    ca=Canvas(vdoc,width=1150)
    ca.pack(side=LEFT,fill=Y)
    scroll=ttk.Scrollbar(vdoc,orient='vertical',command=ca.yview)
    scroll.pack(side=RIGHT,fill=Y)
    ca.config(yscrollcommand=scroll.set)
    ca.bind('<Configure>',lambda e: ca.config(scrollregion=ca.bbox('all')))
    s_frame=Frame(ca,bg='aquamarine2')
    ca.create_window((0,0),window=s_frame,anchor='nw')

    if rows==[]:
         Frame(s_frame,bg='aquamarine2',width=1500,height=1000).place(x=1,y=1)
         Label(s_frame,bg='aquamarine2',text="No Doctors Found",font=("times bold",45)).pack(padx=380,pady=280)

    else: 
        for i in range(len(rows)):
            Label(s_frame,text="DOCTOR'S DETAILS",font=("times bold",25),bg="white").place(x=500,y=20)

            Frame(s_frame,bg='aquamarine2',width=1500,height=600).pack(padx=10,pady=10)
            
            Label(s_frame,text="Name",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=a,height=40,width=300)
            Label(s_frame,text=rows[i][0],font=("times new roman",15),bg="white").place(x=250,y=a,height=40,width=300)

            Label(s_frame,text="DOB",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=b,height=40,width=300)
            Label(s_frame,text=rows[i][1],font=("times new roman",15),bg="white").place(x=250,y=b,height=40,width=300)

            Label(s_frame,text="Gender",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=c,height=40,width=300)
            Label(s_frame,text=rows[i][2],font=("times new roman",15),bg="white").place(x=250,y=c,height=40,width=300)

            Label(s_frame,text="Address",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=d,height=40,width=300)
            Label(s_frame,text=rows[i][3],font=("times new roman",15),bg="white").place(x=250,y=d,height=40,width=300)

            Label(s_frame,text="Phone No.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=e,height=40,width=300)
            Label(s_frame,text=rows[i][4],font=("times new roman",15),bg="white").place(x=250,y=e,height=40,width=300)

            Label(s_frame,text="Teresa Scan ID",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=f,height=40,width=300)
            Label(s_frame,text=rows[i][5],font=("times new roman",15),bg="white").place(x=250,y=f,height=40,width=300)

            Label(s_frame,text="Qualification",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=b,height=40,width=300)
            Label(s_frame,text=rows[i][6],font=("times new roman",15),bg="white").place(x=870,y=b,height=40,width=300)

            Label(s_frame,text="Specialist",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=c,height=40,width=300)
            Label(s_frame,text=rows[i][7],font=("times new roman",15),bg="white").place(x=870,y=c,height=40,width=300)

            Label(s_frame,text="Email ID",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=d,height=40,width=300)
            Label(s_frame,text=rows[i][8],font=("times new roman",15),bg="white").place(x=870,y=d,height=40,width=300)
                    
            Label(s_frame,text="Medical license",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=e,height=40,width=300)
            Label(s_frame,text=rows[i][9],font=("times new roman",15),bg="white").place(x=870,y=e,height=40,width=300)

            a+=600
            b+=600
            c+=600
            d+=600
            e+=600
            f+=600
    Button(s_frame,text="HOME",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light gray",command=homep).place(x=10,y=10,height=40,width=110)
    vdoc.mainloop()


