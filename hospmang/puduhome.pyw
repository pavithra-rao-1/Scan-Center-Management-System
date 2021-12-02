from tkinter import*
from PIL import ImageTk
import n_appointment
import n_spatient
import n_pinfo
import n_dpat
import n_vpat



def view_p():
    global root
    root.destroy()
    n_vpat.v_pat()

def appo_fun():
    global root
    root.destroy()
    n_appointment.patient_appo()

def s_pat():
    global root
    root.destroy()
    n_spatient.search_p()

def c_info():
    global root
    root.destroy()
    n_pinfo.p_info()

def d_info():
    global root
    root.destroy()
    n_dpat.d_info()

def homepage(root1):
    global root   
    root=Tk()
    root.title("HOME")
    root.geometry("1280x800+0+0")
    root.resizable(False,False)
    bg=ImageTk.PhotoImage(file="photo2.jpg")
    bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

    Label(root,text="WELCOME TO CYBERNAUT SCAN CENTER",font=("Copperplate Gothic Bold",40,"bold"),bg="light gray",fg="black").place(x=2,y=20)

    #Frame_h=Frame(root,bg="#108cb5").place(x=600,y=110,height=50,width=190)
    title=Label(root,text="PATIENT",font=("Courier",30,"bold"),bg="#108cb5",fg="white").place(x=700,y=110)

    #Frame_hp=Frame(root,bg="#108cb5").place(x=890,y=110,height=50,width=190)
    

    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Appointment",command=appo_fun).place(x=700,y=200,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Search",command=s_pat).place(x=700,y=255,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Change Info",command=c_info).place(x=700,y=310,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Delete",command=d_info).place(x=700,y=365,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="View Data",command=view_p).place(x=700,y=420,height=50,width=190)

    
    root.mainloop()

