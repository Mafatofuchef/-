from cProfile import label
from cgitb import text
from ctypes.wintypes import SIZE
from sqlite3 import Row
import tkinter as tk
from tkinter import RAISED, Entry, Label, StringVar, ttk
from tkinter.tix import COLUMN
from tkinter.ttk import Button
from turtle import color

#입력창 설정

def window():
    newWindow = tk.Toplevel(root)
    newWindow.title("입력창")
    labelExample = tk.Label(newWindow, text="",width=40, height=20)
    button_ins=tk.Button(newWindow, text="GO")
    entry_ins = Entry(newWindow, width = 20)

    labelExample.pack()
    button_ins.place(x=200, y=100)
    entry_ins.place(x=20, y=100)


#편성창 설정

def window2():
    newWindow = tk.Toplevel(root)
    newWindow.title("편성창")
    labelExample = tk.Label(newWindow, text="",width=40, height=20)
    button_par=tk.Button(newWindow, text="GO")
    entry_par = Entry(newWindow, width=20)

    labelExample.pack()
    button_par.place(x=200, y=100)
    entry_par.place(x=20, y=100)


#메인에 대한 값들
root =tk.Tk()

root.title("파티 편집기 v.1")
root.geometry("800x800")
root.resizable(False, False)
Label_vs=tk.Label(root, text="제작자 :마파두부")
Label_vs.place(x=600,y=700)


#입력 버튼

btn1=tk.Button(root, text="입력", command=window, width=10, height=3, bg="green", fg="black")
btn1.place(x=100,y=100)

#편성버튼

btn2=tk.Button(root, text="편성", command=window2, width=10, height=3, bg="red", fg="white")
btn2.place(x=600, y=100)

#파티 편성 내용 보여주는 창


root.mainloop()


