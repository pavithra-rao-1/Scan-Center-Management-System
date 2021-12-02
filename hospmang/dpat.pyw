from tkinter import*
from tkinter import messagebox
import mysql.connector as sql
import homepage

def d_info():
    global e1,listy
    dpat=Tk()
    dpat.title('Delete Register Number')
    dpat.geometry("800x400+60+10")
    dpat.resizable(False,False)
    listy=[]
    def search_back():
        dpat.destroy()
        homepage.homepage(dpat)

    def d_pat():
        global e1,listy
        E1=e1.get()
        con1 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
        cr1 = con1.cursor()
        cr1.execute("select reg_num from appo")
        #cr1.execute("commit")
        rows=cr1.fetchall()
        con1.close()
        for i in rows:
            listy += [str(i)[-len(str(i))+1:-2]]
        var=0
        if E1 in listy:
            listy.remove(E1)
            listy=[]
            con = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
            cr = con.cursor()
            cr.execute("delete from appo where reg_num='"+E1+"'")
            cr.execute("commit")
            con.close()
            messagebox.showinfo('Deleted','Record deleted successfully')
        else:
            messagebox.showerror('Error','Register number not found')

    frame = Frame(dpat,bg='aquamarine2',width=1200,height=650).place(x=1,y=1)
    Label(dpat,text='Registration ID',font=("times bold",15),bg="aquamarine2").place(x=120,y=100,height=40,width=300)
    e1 = Entry(dpat,font=("times new roman",15))
    e1.place(x=420,y=100,height=40,width=300)

    Button(dpat,text='DELETE',command=d_pat).place(x=360,y=200,height=40,width=100)
    Button(dpat,text="BACK",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light grey",command=search_back).place(x=10,y=10,height=40,width=110)

