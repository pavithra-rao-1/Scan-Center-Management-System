from tkinter import*
from tkinter import ttk
from PIL import ImageTk
import homepage
import time
import os
from tkinter import messagebox

def abt_us():
    def hp():
        abt.destroy()
        homepage.homepage(abt)
        
    abt=Tk()
    abt.title("ABOUT US")
    abt.geometry("1350x700+0+0")
    #abt.resizable(False,False)
    
    a=Label(abt,text="""   
Cybernaut Scans and Labs is a private limited company,was founded by Ms. Keerthana in the
year 2000 and is currently managed by a Team of Radiologists, all from one family –
Dr.Pavithra Rao, Dr.Namitha, Dr.Gayathri Srinivasan and Dr.Mohanapriya.We are the largest
and most affordable diagnostic provider in India. Cybernaut Scans and Labs offers its
services to more than 4500patients a day across India.We have 30 full fledged diagnostic
centres with CT, MRI,Ultrasound scan,Xray, Mammogram, OPG and Lab facilities.We have more
than 75 collection centres providing lab services.Our motto is to provide high quality
diagnostics to everyone at transparentaffordable costs.We are India’s most affordable
diagnostics service (We do MRI scans for Rs 2500 and CT scansfor Rs 1000).We are
accreditedby both NABL and NABH at testing our quality.Our own family group of Radiologists
ensure good scan reports.We have a fully automated centralprocessing lab in Chennai to give
accurate and quick results.Cybernaut Scans and Labs is dedicated to remain at the forefront
of the medical imaging and diagnostics field by maintaining state-of-the-art equipments and
offering the latest in scientific advances at an affordable cost.""",font=("Georgia",17,"bold"),justify=LEFT,fg="black",bg="white").place(x=0,y=5,height=700,width=1300)
    
        
    Button(abt,text="HOME",font=("Goudy old style",15,"bold"),command=hp,cursor="hand2",fg="#3787d7",bd=1,bg="light gray").place(x=10,y=10,height=40,width=110)
    Label(abt,text="ABOUT US",font=("Goudy old style",30,"bold"),bg="white",fg="black").place(x=500,y=20)



