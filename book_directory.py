import tkinter
from tkinter import *
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import sqlite3

def exit():
    result=messagebox.askyesno("Alert","do you want to exit")
    if result==True:
        sys.exit()
    else:
        pass

root=Tk()
root.title("Boook Directory")
root.geometry("504x295+200+300")
root.resizable(True,True)
root.config(bg="light pink")

label1=Label(root,text="Title")
label1.grid(row=0,column=0)
entry1=Entry(width=35)
entry1.grid(row=0,column=1)

label2=Label(root,text="Author")
label2.grid(row=0,column=2)
entry2=Entry(root,width=35)
entry2.grid(row=0,column=3)

label3=Label(root,text="Year")
label3.grid(row=1,column=0)
entry3=Entry(root,width=35)
entry3.grid(row=1,column=1)

label4=Label(root,text="ISBN    ")
label4.grid(row=1,column=2)
entry4=Entry(root,width=35)
entry4.grid(row=1,column=3)

b1=Button(root,text="View All",width=20,height=2)
b1.place(x=320,y=42)
b2=Button(root,text="Search Entry",width=20,height=2)
b2.place(x=320,y=84)
b3=Button(root,text="Add Entry",width=20,height=2)
b3.place(x=320,y=126)
b4=Button(root,text="Update Selected",width=20,height=2)
b4.place(x=320,y=168)
b5=Button(root,text="Delete Selected",width=20,height=2)
b5.place(x=320,y=210)
b6=Button(root,text="Exit",width=20,height=2,command=exit)
b6.place(x=320,y=252)

f=Frame(root)
f.place(x=0,y=84)
s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set,width=40,height=10)
l.pack(side=LEFT,fill=BOTH)

root.mainloop()