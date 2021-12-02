from tkinter import*
from PIL import ImageTk
import appointment
import spatient
import pinfo
import dpat
import aboutus
import newdoctor
import dinfo
import sdoctor
import vpat
import vdoc
import ddoc

def delete_doc():
    global root
    root.destroy()
    ddoc.d_doc()

def view_d():
    global root
    root.destroy()
    vdoc.v_doc()

def view_p():
    global root
    root.destroy()
    vpat.v_pat()

def s_doc():
    global root
    root.destroy()
    sdoctor.search_d()

def doc_change():
    global root
    root.destroy()
    dinfo.d_info()

def nw_doc():
    global root
    root.destroy()
    newdoctor.doc_app()    

def at_us():
    global root
    root.destroy()
    aboutus.abt_us()

def appo_fun():
    global root
    root.destroy()
    appointment.patient_appo()

def s_pat():
    global root
    root.destroy()
    spatient.search_p()

def c_info():
    global root
    root.destroy()
    pinfo.p_info()

def d_info():
    global root
    root.destroy()
    dpat.d_info()

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
    title=Label(root,text="PATIENT",font=("Courier",30,"bold"),bg="#108cb5",fg="white").place(x=600,y=110)

    #Frame_hp=Frame(root,bg="#108cb5").place(x=890,y=110,height=50,width=190)
    title=Label(root,text=" DOCTOR ",font=("Courier",30,"bold"),bg="#108cb5",fg="white").place(x=890,y=110)

    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Appointment",command=appo_fun).place(x=600,y=200,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Search",command=s_pat).place(x=600,y=255,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Change Info",command=c_info).place(x=600,y=310,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="Delete",command=d_info).place(x=600,y=365,height=50,width=190)
    Button(root,font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",text="View Data",command=view_p).place(x=600,y=420,height=50,width=190)

    Button(root,text="Application",font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",command=nw_doc).place(x=890,y=200,height=50,width=190)
    Button(root,text="Search",font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",command=s_doc).place(x=890,y=255,height=50,width=190)
    Button(root,text="Change Info",font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",command=doc_change).place(x=890,y=310,height=50,width=190)
    Button(root,text="Remove",font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",command=delete_doc).place(x=890,y=365,height=50,width=190)
    Button(root,text="View Doctors",font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",command=view_d).place(x=890,y=420,height=50,width=190)

    Button(root,text="ABOUT US",font=("Goudy old style",20,"bold"),cursor="hand2",fg="#3787d7",bd=2,bg="white",command=at_us).place(x=745,y=510,height=50,width=190)   

    root.mainloop()

