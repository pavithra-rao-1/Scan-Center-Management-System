from tkinter import*
from tkinter import messagebox
import mysql.connector as sql
import homepage

def d_doc():
    global e1,listy
    ddoc=Tk()
    ddoc.title('Delete doctor Information')
    ddoc.geometry("800x400+60+10")
    ddoc.resizable(False,False)
    listy=[]
    
    def search_back():
        ddoc.destroy()
        homepage.homepage(ddoc)

    def del_doc():
        global e1,listy
        some1=e1.get()
        E1=some1[2:]
        a=[]
        con1 = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
        cr1 = con1.cursor()
        cr1.execute("select med_license from doct")
        #cr1.execute("commit")
        rows=cr1.fetchall()
        con1.close()
        for i in rows:
            listy += [str(i)[-len(str(i))+1:-2]]
        var=0
        for some in range(len(listy)):
            a+=listy[some][3]
            
        if E1 in a:
            listy.remove("'00"+str(E1)+"'")
            listy=[]
            con = sql.connect(host = "localhost", user = "root", password = "keerthi", database = "mdba")
            cr = con.cursor()
            cr.execute("delete from doct where med_license="+"'00"+E1+"'")
            cr.execute("commit")
            con.close()
            messagebox.showinfo('Deleted','Record deleted successfully')
        elif E1=='':
            messagebox.showerror('Error','Please enter Medical License Number')
        else:
            messagebox.showerror('Error','Medical License Number not found')

    frame = Frame(ddoc,bg='aquamarine2',width=1200,height=650).place(x=1,y=1)
    Label(ddoc,text='Medical License Number',font=("times bold",15),bg="aquamarine2").place(x=120,y=100,height=40,width=300)
    e1 = Entry(ddoc,font=("times new roman",15))
    e1.place(x=420,y=100,height=40,width=300)

    Button(ddoc,text='DELETE',command=del_doc).place(x=360,y=200,height=40,width=100)
    Button(ddoc,text="BACK",font=("Goudy old style",15,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="light grey",command=search_back).place(x=10,y=10,height=40,width=110)


