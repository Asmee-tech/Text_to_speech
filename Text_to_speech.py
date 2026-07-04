from tkinter import*
# from tkinter.ttk import*
from gtts import gTTS
import os
# import pygame

screen=Tk()
screen.title("Text to speech")
screen.geometry("650x550+350+200")

frame1=Frame(screen,bg="lightpink",height="150")
frame1.pack(fill=X)

frame2=Frame(screen,bg="lightgreen",height="750")
frame2.pack(fill=X)

lab1=Label(frame1,text="Text to speech",font="bold,80")
lab1.place(x=250,y=100)

ent=Entry(frame2,font=14,width=45)
ent.place(x=100,y=50)
ent.insert(0,"")

def play():
    language="en"
    myobj=gTTS(text=ent.get(),lang=language,slow=False)
    myobj.save("convert.mp3")
    os.system("xdg-open convert.mp3")


sub=Button(frame2,text="SUBMIT",width=15,pady=15,command=play).place(x=250,y=130)

screen.mainloop()
