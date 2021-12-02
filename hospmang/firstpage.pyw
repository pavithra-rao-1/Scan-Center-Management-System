from tkinter import*
from PIL import ImageTk
import login
from tkinter import messagebox

login_window=Tk()
login_window.title("WELCOME")
login_window.geometry("1350x900+0+0")
login_window.resizable(False,False)

bg=ImageTk.PhotoImage(file="photo.jpg")
bg_image=Label(login_window,image=bg)
bg_image.place(x=0,y=0,relwidth=1,relheight=1)

Frame_login=Frame(login_window,bg="white").place(x=50,y=290,height=340,width=500)

login_window()
