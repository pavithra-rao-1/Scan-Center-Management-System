from tkinter import*
from PIL import ImageTk
import homepage
import puduhome
from tkinter import messagebox


    
login_window=Tk()
login_window.title("LOGIN")
login_window.geometry("1350x900+0+0")
login_window.resizable(False,False)

bg=ImageTk.PhotoImage(file="photo.jpg")
bg_image=Label(login_window,image=bg)
bg_image.place(x=0,y=0,relwidth=1,relheight=1)



def login():
    global txt_pass,txt_user,username,password

    Frame_login=Frame(login_window,bg="white").place(x=50,y=290,height=340,width=500)

    Label(Frame_login,text="LOGIN",font=("Algerian",50,"bold"),fg="#3787d7",bg="white").place(x=170,y=310)
    Label(Frame_login,text="CYBERNAUT SCAN CENTER",font=("Bradley Hand ITC",50,"bold"),bg="#070c4a",fg="#373ad7").place(x=164,y=50)

    Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=80,y=380)
    txt_user=Entry(Frame_login,font=("times new roman",15),bg="light gray")
    txt_user.place(x=80,y=420,width=350,height=35)

    Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=80,y=470)
    txt_pass=Entry(Frame_login,font=("times new roman",15),show="*",bg="light gray")
    txt_pass.place(x=80,y=510,width=350,height=35)

    

    def login_user():
        global txt_pass,txt_user,username,password
        if txt_pass.get()=="" or txt_user.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif txt_pass.get()!=username or txt_user.get()!=password:
            messagebox.showerror("Error","INVALID Username or Password")
        else:
            login_window.destroy()
            if username=="admin" and password=="admin":
                homepage.homepage(login_window)
            elif username=="doctor" and password=="doctor":
                puduhome.homepage(login_window)
            
    Button(Frame_login,text="Forget Password?",font=("Goudy old style",10,"bold"),cursor="hand2",fg="#3787d7",bd=1,bg="white").place(x=80,y=560)
    Button(login_window,text="LOGIN",command=login_user,cursor="hand2",font=("Goudy old style",15,"bold"),bg="#3787d7",fg="white").place(x=200,y=612,height=40,width=180)


def admin():
    global username,password
    username="admin"
    password="admin"
    Button(login_window,text="ADMINISTRATOR",font=("Goudy old style",20,"bold"),cursor="hand2",command=admin,fg="#3787d7",bd=1,bg="white",state='disabled').place(x=210,y=170)
    Button(login_window,text="DOCTOR",font=("Goudy old style",20,"bold"),cursor="hand2",command=doctr,fg="#3787d7",bd=1,bg="white",state='disabled').place(x=780,y=170)
    login()
def doctr():
    global username,password
    username="doctor"
    password="doctor"
    Button(login_window,text="ADMINISTRATOR",font=("Goudy old style",20,"bold"),cursor="hand2",command=admin,fg="#3787d7",bd=1,bg="white",state='disabled').place(x=210,y=170)
    Button(login_window,text="DOCTOR",font=("Goudy old style",20,"bold"),cursor="hand2",command=doctr,fg="#3787d7",bd=1,bg="white",state='disabled').place(x=780,y=170)
    login()
    

Button(login_window,text="ADMINISTRATOR",font=("Goudy old style",20,"bold"),cursor="hand2",command=admin,fg="#3787d7",bd=1,bg="white").place(x=210,y=170)
Button(login_window,text="DOCTOR",font=("Goudy old style",20,"bold"),cursor="hand2",command=doctr,fg="#3787d7",bd=1,bg="white").place(x=780,y=170)

