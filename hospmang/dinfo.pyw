from tkinter import*
from tkinter import messagebox
import mysql.connector as sql
import homepage

def d_info():
    global e1
    spat=Tk()
    spat.title('Change Information')
    spat.geometry("1200x650+60+10")
    spat.resizable(False,False)

    frame = Frame(spat,bg='aquamarine2',width=1200,height=650).place(x=1,y=1)
    Label(spat,text='Medical License ID',font=("times new roman",15),bg="aquamarine2").place(x=120,y=20,height=40,width=300)
    e1 = Entry(spat,font=("times new roman",15))
    e1.place(x=420,y=20,height=40,width=300)

    def search_back():
        spat.destroy()
        homepage.homepage(spat)
    def change_info():
        global e1,entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,rows
        E1=e1.get()
        if E1=='':
            messagebox.showerror('Error',"Enter Medical License No. to change")
        elif not E1.isdigit():
            messagebox.showerror('Error',"Enter only digits")
        else:
            con=sql.connect(host="localhost",user="root",password="keerthi",database="MDBA")
            cr=con.cursor()
            cr.execute("select * from doct where med_license="+str(E1))
            #cr.execute("commit")
            rows=cr.fetchall()
            con.close()
            if rows!=[]:

                #Label(spat,text="PATIENT'S DETAILS",font=("times bold",25),bg="aquamarine2").place(x=500,y=20)
                Button(spat,text="BACK",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light grey",command=search_back).place(x=10,y=10,height=40,width=110)

                Label(spat,text="Name",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=120,height=40,width=300)
                a=StringVar()
                entry1=Entry(spat,textvariable=a,font=("times new roman",15),bg="white")
                entry1.place(x=250,y=120,height=40,width=300)
                entry1.insert(0, rows[0][0])

                Label(spat,text="DOB",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=200,height=40,width=300)
                b=StringVar()
                entry2=Entry(spat,textvariable=b,font=("times new roman",15),bg="white")
                entry2.place(x=250,y=200,height=40,width=300)
                entry2.insert(0, rows[0][1])

                Label(spat,text="Gender",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=280,height=40,width=300)
                c=StringVar()
                entry3=Entry(spat,textvariable=c,font=("times new roman",15),bg="white")
                entry3.place(x=250,y=280,height=40,width=300)
                entry3.insert(0, rows[0][2])

                Label(spat,text="Address",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=360,height=40,width=300)
                d=StringVar()
                entry4=Entry(spat,textvariable=d,font=("times new roman",15),bg="white")
                entry4.place(x=250,y=360,height=40,width=300)
                entry4.insert(0, rows[0][3])

                Label(spat,text="Phone No.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=440,height=40,width=300)
                e=StringVar()
                entry5=Entry(spat,textvariable=e,font=("times new roman",15),bg="white")
                entry5.place(x=250,y=440,height=40,width=300)
                entry5.insert(0, rows[0][4])

                Label(spat,text="Teresa Scan ID",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=520,height=40,width=300)
                f=StringVar()
                entry6=Entry(spat,textvariable=f,font=("times new roman",15),bg="white")
                entry6.place(x=250,y=520,height=40,width=300)
                entry6.insert(0, rows[0][5])

                Label(spat,text="Qualification",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=120,height=40,width=300)
                g=StringVar()
                entry7=Entry(spat,textvariable=g,font=("times new roman",15),bg="white")
                entry7.place(x=870,y=120,height=40,width=300)
                entry7.insert(0, rows[0][6])

                Label(spat,text="Specialist",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=200,height=40,width=300)
                h=StringVar()
                entry8=Entry(spat,textvariable=h,font=("times new roman",15),bg="white")
                entry8.place(x=870,y=200,height=40,width=300)
                entry8.insert(0, rows[0][7])

                Label(spat,text="Email ID",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=280,height=40,width=300)
                i=StringVar()
                entry9=Entry(spat,textvariable=i,font=("times new roman",15),bg="white")
                entry9.place(x=870,y=280,height=40,width=300)
                entry9.insert(0, rows[0][8])
                        
                Label(spat,text="Medical License ID",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=360,height=40,width=300)
                j=StringVar()
                entry10=Entry(spat,textvariable=j,font=("times new roman",15),bg="white")
                entry10.place(x=870,y=360,height=40,width=300)
                entry10.insert(0, rows[0][9])
            else:
                messagebox.showerror("Error","No Records are found")

    Button(spat,text='EDIT',command=change_info).place(x=820,y=20,height=40,width=100)

    def change_info1():
        global entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,rows
        hosp1=0
        E1=entry1.get()        
        E2=entry2.get()
        E3=entry3.get()
        E4=entry4.get()
        E5=entry5.get()
        E6=entry6.get()
        E7=entry7.get()
        E8=entry8.get()
        E9=entry9.get()
            
        ch='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.'
        for i in E1:
            if i not in ch:
                messagebox.showerror('Error','Enter your name properly')
                hosp1=0
                break
            else:
                hosp1=1
                continue
        E10=entry10.get()
        if hosp1==1:
            if (not E5.isdigit()) or len(E5)!=10:
                messagebox.showerror('Error','Enter your phone number properly')
            
            elif int(E10)!=int(rows[0][9]):
                f=StringVar()
                messagebox.showerror('Error','Medical License ID cannot be changed')
                entr10=Entry(spat,textvariable=f,font=("times new roman",15),bg="white")
                entr10.place(x=250,y=520,height=40,width=300)
                entr10.insert(0, rows[0][9])
        
            else:
                
                con1 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr1 = con1.cursor()
                cr1.execute("update doct set name='"+E1+"' where med_license='"+E10+"'")
                cr1.execute("commit")
                con1.close()

                con2 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr2 = con2.cursor()
                cr2.execute("update doct set dob='"+E2+"' where med_license='"+E10+"'")
                cr2.execute("commit")
                con2.close()

                con3 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr3 = con3.cursor()
                cr3.execute("update doct set gender='"+E3+"' where med_license='"+E10+"'")
                cr3.execute("commit")
                con3.close()

                con4 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr4 = con4.cursor()
                cr4.execute("update doct set address='"+E4+"' where med_license='"+E10+"'")
                cr4.execute("commit")
                con4.close()

                con5 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr5 = con5.cursor()
                cr5.execute("update doct set ph_num='"+E5+"' where med_license='"+E10+"'")
                cr5.execute("commit")
                con5.close()

                con6 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr6 = con6.cursor()
                cr6.execute("update doct set teresa_id='"+E6+"' where med_license='"+E10+"'")
                cr6.execute("commit")
                con6.close()

                con7 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr7 = con7.cursor()
                cr7.execute("update doct set qualification='"+E7+"' where med_license='"+E10+"'")
                cr7.execute("commit")
                con7.close()

                con8 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr8= con8.cursor()
                cr8.execute("update doct set specialist='"+E8+"' where med_license='"+E10+"'")
                cr8.execute("commit")
                con8.close()

                con9 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
                cr9 = con9.cursor()
                cr9.execute("update doct set email='"+E9+"' where med_license='"+E10+"'")
                cr9.execute("commit")
                con9.close()

                messagebox.showinfo('Changed','Your details have been changed')
        
    Button(spat,text='CHANGE',command=change_info1).place(x=500,y=600,height=40,width=100)
  












