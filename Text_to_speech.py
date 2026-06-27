from tkinter import*
# from tkinter.ttk import*
from gtts import gTTS
import os

screen=Tk()
screen.title("Text to speech")
screen.geometry("650x550+350+200")

frame1=Frame(screen,bg="lightpink",height="150")
frame1.pack(fill=X)

frame2=Frame(screen,bg="lightgreen",height="750")
frame2.pack(fill=X)

lab1=Label(frame1,text="Text to speech",font="bold,80").place(x=80,y=100)

ent=Entry(frame2,font=40,width=45).place(x=80,y=150)
ent.insert(0,"")

sub=Button(frame2,text="SUBMIT",width=15).place(x=250,y=130)


screen.mainloop()