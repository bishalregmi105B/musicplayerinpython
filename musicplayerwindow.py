from ast import arg
import os
from tkinter import*
from functools import partial
import tkinter
from django.forms import Textarea

from playsound import*
import threading

def plymusic(pa):
    playsound(pa,block = False)
   

def plyso(filename,playingfm,root,text):
    ab=path.get()
    
    pa=(f"{ab}/{filename}")
    t1=threading.Thread(target=plymusic, args=(pa,))

    

    text.insert(0.0,
    f"{filename} is being Played By /n Ashlya Tech Music Player.\n Plz Like,Subscribe and share My Video ./n    Music Location : {ab}")

    
    
  
    if t1.is_alive ==True:
        t1.setDaemon(False)
    else:
        t1.start()
   
        


def musicplrwin(root,f1,folder_path,btn1,playingfm,text):
    global path
    btn1.destroy()
    root.geometry("1024x480")
    root.title("Music Player")
    path=folder_path
    fils=os.listdir(folder_path.get())
    for i in fils:
        btn=Button(f1,text=i,command=partial(plyso,i,playingfm,root,text),border=0)
        btn.pack()


