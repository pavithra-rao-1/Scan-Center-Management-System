from tkinter import*
from tkinter import messagebox
import mysql.connector as sql
import homepage

def search_p():
    global t1,t2,t3
    pat=Tk()
    pat.title("Search Patient")
    pat.geometry("1200x650+60+10")
    pat.resizable(False,False)

    def homep():
        pat.destroy()
        homepage.homepage(pat)

    def reg_check():
        global t1
        ta1=t1.get()
        if ta1=='':
            messagebox.showerror("Error","Enter patient's register number")
        elif not ta1.isdigit():        
            messagebox.showerror("Error","Enter only digits")

        else:
            T1=int(ta1)
            con=sql.connect(host="localhost",user="root",password="keerthi",database="MDBA")
            cr=con.cursor()
            cr.execute("select * from appo where reg_num="+str(T1))
            #cr.execute("commit")
            rows=cr.fetchall()
            con.close()

            if rows==[]:
                messagebox.showerror("ERROR","Records not found")
            else:
                pat.withdraw()
                spat=Tk()
                spat.title('search reg no')
                spat.geometry("1200x650+60+10")
                spat.resizable(False,False)         
                
                def search_back():
                    pat.deiconify()
                    spat.destroy()

                frame = Frame(spat,bg='aquamarine2',width=1200,height=650).place(x=1,y=1)
                Label(spat,text="PATIENT'S DETAILS",font=("times bold",25),bg="aquamarine2").place(x=500,y=20)
                Button(spat,text="BACK",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light grey",command=search_back).place(x=10,y=10,height=40,width=110)

                           
                Label(spat,text="Name",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=120,height=40,width=300)
                Label(spat,text=rows[0][0],font=("times new roman",15),bg="white").place(x=250,y=120,height=40,width=300)

                Label(spat,text="DOB",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=200,height=40,width=300)
                Label(spat,text=rows[0][1],font=("times new roman",15),bg="white").place(x=250,y=200,height=40,width=300)

                Label(spat,text="Gender",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=280,height=40,width=300)
                Label(spat,text=rows[0][2],font=("times new roman",15),bg="white").place(x=250,y=280,height=40,width=300)

                Label(spat,text="Address",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=360,height=40,width=300)
                Label(spat,text=rows[0][3],font=("times new roman",15),bg="white").place(x=250,y=360,height=40,width=300)

                Label(spat,text="Phone No.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=440,height=40,width=300)
                Label(spat,text=rows[0][4],font=("times new roman",15),bg="white").place(x=250,y=440,height=40,width=300)

                Label(spat,text="Registration no.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=520,height=40,width=300)
                Label(spat,text=rows[0][5],font=("times new roman",15),bg="white").place(x=250,y=520,height=40,width=300)

                Label(spat,text="Registration Date",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=120,height=40,width=300)
                Label(spat,text=rows[0][6],font=("times new roman",15),bg="white").place(x=870,y=120,height=40,width=300)

                Label(spat,text="Hospital ref. by",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=200,height=40,width=300)
                Label(spat,text=rows[0][7],font=("times new roman",15),bg="white").place(x=870,y=200,height=40,width=300)

                Label(spat,text="Test date",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=280,height=40,width=300)
                Label(spat,text=rows[0][8],font=("times new roman",15),bg="white").place(x=870,y=280,height=40,width=300)
                        
                Label(spat,text="Test Type",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=360,height=40,width=300)
                Label(spat,text=rows[0][9],font=("times new roman",15),bg="white").place(x=870,y=360,height=40,width=300)
                
                Label(spat,text="Doctor",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=440,height=40,width=300)
                Label(spat,text=rows[0][10],font=("times new roman",15),bg="white").place(x=870,y=440,height=40,width=300)

                Label(spat,text="Fees",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=520,height=40,width=300)
                Label(spat,text=rows[0][11],font=("times new roman",15),bg="white").place(x=870,y=520,height=40,width=300)
            
    def name_check():
        global t2
        ta2=t2.get()
        if ta2=='':
            messagebox.showerror("Error","Enter patient's name")
        elif not t2.get().isalpha():
            messagebox.showerror("Error","Enter only alphabets")
        else:            
            con=sql.connect(host="localhost",user="root",password="keerthi",database="MDBA")
            cr=con.cursor()
            cr.execute("select * from appo where name='"+ta2+"'")
            #cr.execute("commit")
            rows=cr.fetchall()
            con.close()

            if rows==[]:
                messagebox.showerror("ERROR","Records not found")
            else:
                pat.withdraw()
                spat=Tk()
                spat.title('search reg no')
                spat.geometry("1200x650+60+10")
                spat.resizable(False,False)

                def search_back():
                    pat.deiconify()
                    spat.destroy()

                frame = Frame(spat,bg='aquamarine2',width=1200,height=650).place(x=1,y=1)
                Label(spat,text="PATIENT'S DETAILS",font=("times bold",25),bg="aquamarine2").place(x=500,y=20)
                Button(spat,text="BACK",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light grey",command=search_back).place(x=10,y=10,height=40,width=110)

                
                Label(spat,text="Name",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=120,height=40,width=300)
                Label(spat,text=rows[0][0],font=("times new roman",15),bg="white").place(x=250,y=120,height=40,width=300)

                Label(spat,text="DOB",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=200,height=40,width=300)
                Label(spat,text=rows[0][1],font=("times new roman",15),bg="white").place(x=250,y=200,height=40,width=300)

                Label(spat,text="Gender",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=280,height=40,width=300)
                Label(spat,text=rows[0][2],font=("times new roman",15),bg="white").place(x=250,y=280,height=40,width=300)

                Label(spat,text="Address",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=360,height=40,width=300)
                Label(spat,text=rows[0][3],font=("times new roman",15),bg="white").place(x=250,y=360,height=40,width=300)

                Label(spat,text="Phone No.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=440,height=40,width=300)
                Label(spat,text=rows[0][4],font=("times new roman",15),bg="white").place(x=250,y=440,height=40,width=300)

                Label(spat,text="Registration no.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=520,height=40,width=300)
                Label(spat,text=rows[0][5],font=("times new roman",15),bg="white").place(x=250,y=520,height=40,width=300)

                Label(spat,text="Registration Date",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=120,height=40,width=300)
                Label(spat,text=rows[0][6],font=("times new roman",15),bg="white").place(x=870,y=120,height=40,width=300)

                Label(spat,text="Hospital ref. by",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=200,height=40,width=300)
                Label(spat,text=rows[0][7],font=("times new roman",15),bg="white").place(x=870,y=200,height=40,width=300)

                Label(spat,text="Test date",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=280,height=40,width=300)
                Label(spat,text=rows[0][8],font=("times new roman",15),bg="white").place(x=870,y=280,height=40,width=300)
                        
                Label(spat,text="Test Type",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=360,height=40,width=300)
                Label(spat,text=rows[0][9],font=("times new roman",15),bg="white").place(x=870,y=360,height=40,width=300)
                
                Label(spat,text="Doctor",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=440,height=40,width=300)
                Label(spat,text=rows[0][10],font=("times new roman",15),bg="white").place(x=870,y=440,height=40,width=300)

                Label(spat,text="Fees",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=520,height=40,width=300)
                Label(spat,text=rows[0][11],font=("times new roman",15),bg="white").place(x=870,y=520,height=40,width=300)
            
    def cont_check():
        global t3
        ta3=t3.get()
        if ta3=='':
            messagebox.showerror("Error","Enter patient's contact number")
        elif not ta3.isdigit():
            messagebox.showerror("Error","Enter only digits")
        elif len(ta3)!=10:
            messagebox.showerror("Error","Phone number must contain 10 digits")
        else:
            T3=int(ta3)
            
            con=sql.connect(host="localhost",user="root",password="keerthi",database="MDBA")
            cr=con.cursor()
            cr.execute("select * from appo where ph_num="+str(T3))
            #cr.execute("commit")
            rows=cr.fetchall()
            con.close()

            if rows==[]:
                messagebox.showerror("ERROR","Records not found")
            else:
                pat.withdraw()
                spat=Tk()
                spat.title('search reg no')
                spat.geometry("1200x650+60+10")
                spat.resizable(False,False)

                def search_back():
                    pat.deiconify()
                    spat.destroy()

                frame = Frame(spat,bg='aquamarine2',width=1200,height=650).place(x=1,y=1)
                Label(spat,text="PATIENT'S DETAILS",font=("times bold",25),bg="aquamarine2").place(x=500,y=20)
                Button(spat,text="BACK",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light grey",command=search_back).place(x=10,y=10,height=40,width=110)
                
                Label(spat,text="Name",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=120,height=40,width=300)
                Label(spat,text=rows[0][0],font=("times new roman",15),bg="white").place(x=250,y=120,height=40,width=300)

                Label(spat,text="DOB",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=200,height=40,width=300)
                Label(spat,text=rows[0][1],font=("times new roman",15),bg="white").place(x=250,y=200,height=40,width=300)

                Label(spat,text="Gender",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=280,height=40,width=300)
                Label(spat,text=rows[0][2],font=("times new roman",15),bg="white").place(x=250,y=280,height=40,width=300)

                Label(spat,text="Address",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=360,height=40,width=300)
                Label(spat,text=rows[0][3],font=("times new roman",15),bg="white").place(x=250,y=360,height=40,width=300)

                Label(spat,text="Phone No.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=440,height=40,width=300)
                Label(spat,text=rows[0][4],font=("times new roman",15),bg="white").place(x=250,y=440,height=40,width=300)

                Label(spat,text="Registration no.",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=2,y=520,height=40,width=300)
                Label(spat,text=rows[0][5],font=("times new roman",15),bg="white").place(x=250,y=520,height=40,width=300)

                Label(spat,text="Registration Date",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=120,height=40,width=300)
                Label(spat,text=rows[0][6],font=("times new roman",15),bg="white").place(x=870,y=120,height=40,width=300)

                Label(spat,text="Hospital ref. by",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=200,height=40,width=300)
                Label(spat,text=rows[0][7],font=("times new roman",15),bg="white").place(x=870,y=200,height=40,width=300)

                Label(spat,text="Test date",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=280,height=40,width=300)
                Label(spat,text=rows[0][8],font=("times new roman",15),bg="white").place(x=870,y=280,height=40,width=300)
                        
                Label(spat,text="Test Type",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=360,height=40,width=300)
                Label(spat,text=rows[0][9],font=("times new roman",15),bg="white").place(x=870,y=360,height=40,width=300)
                
                Label(spat,text="Doctor",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=440,height=40,width=300)
                Label(spat,text=rows[0][10],font=("times new roman",15),bg="white").place(x=870,y=440,height=40,width=300)

                Label(spat,text="Fees",font=("Goudy old style",20,"bold"),fg="black",bg="aquamarine2").place(x=570,y=520,height=40,width=300)
                Label(spat,text=rows[0][11],font=("times new roman",15),bg="white").place(x=870,y=520,height=40,width=300)
        

    frame=Frame(pat,bg="sky blue")
    frame.place(x=1,y=1,height=700,width=1350)

    Button(frame,text="HOME",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light grey",command=homep).place(x=10,y=10,height=40,width=110)
    Label(pat,text="SEARCH PATIENT BASED ON",font=("Goudy old style",30,"bold"),bg="sky blue",fg="black").place(x=400,y=20)

    Label(pat,text="Reg Number",font=("Goudy old style",30,"bold"),bg="sky blue",fg="black").place(x=200,y=100)
    t1=Entry(frame,font=("times new roman",25),bg="white")
    t1.place(x=450,y=110,height=40,width=300)
    Button(frame,text="SEARCH",font=("Goudy old style",20,"bold"),cursor="hand2",command=reg_check,fg="#3787d7",bd=1,bg="light grey").place(x=800,y=110,height=40,width=200)


    Label(pat,text="Name",font=("Goudy old style",30,"bold"),bg="sky blue",fg="black").place(x=200,y=160)
    t2=Entry(frame,font=("times new roman",25),bg="white")
    t2.place(x=450,y=170,height=40,width=300)
    Button(frame,text="SEARCH",font=("Goudy old style",20,"bold"),cursor="hand2",command=name_check,fg="#3787d7",bd=1,bg="light grey").place(x=800,y=170,height=40,width=200)


    Label(pat,text="Contact num",font=("Goudy old style",30,"bold"),bg="sky blue",fg="black").place(x=200,y=220)
    t3=Entry(frame,font=("times new roman",25),bg="white")
    t3.place(x=450,y=230,height=40,width=300)
    Button(frame,text="SEARCH",font=("Goudy old style",20,"bold"),cursor="hand2",command=cont_check,fg="#3787d7",bd=1,bg="light grey").place(x=800,y=230,height=40,width=200)

    pat.mainloop()













    
   
