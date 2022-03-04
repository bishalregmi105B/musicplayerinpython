import os
from tkinter import*
from tkinter import filedialog
import tkinter as tk
from musicplayerwindow import*

root = tk.Tk()
root.title("Music Player")
folder_path = tk.StringVar()
myframe = LabelFrame(root, text='Musics List here', bd=1, font=(
    'Arial', 14), relief=GROOVE, width=400, height=700, bg='white')
myframe.pack(side=LEFT)
playingfm = LabelFrame(root, text='Musics Playing here', bd=1, font=(
    'Arial', 14),width=800, height=700, relief=GROOVE, bg='white')
playingfm.pack(side=RIGHT)
canvas = Canvas(myframe)
f1 = Frame(canvas)
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

text = tkinter.Text(playingfm)
text.pack()
def selectfolder():

    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    print(os.listdir(folder_path.get()))
    f1.children.clear()
    musicplrwin(root, f1, folder_path, btn1, playingfm,text)





btn1 = Button(f1, text="Select Music Folder", command=selectfolder)
btn1.pack()


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=400, height=700)


#############################End Menu Bar###################
myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=f1, anchor='nw')
f1.bind("<Configure>", myfunction)

root.mainloop()
