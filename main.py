from cProfile import label
from cgitb import text
from ctypes.wintypes import SIZE
from curses import newwin
import tkinter as tk
import tkinter as insert
import tkinter as party
from tkinter.ttk import Button
from turtle import width

#입력창 설정

def window():
    newWindow = tk.Toplevel(root)
    newWindow.title("입력창")
    labelExample = tk.Label(newWindow, text="",width=40, height=20)
    button_ins=tk.Button(newWindow, text="GO")
    
    labelExample.pack()
    button_ins.place(x=200, y=100)



#편성창 설정

def window2():
    newWindow = tk.Toplevel(root)
    newWindow.title("편성창")
    labelExample = tk.Label(newWindow, text="",width=40, height=20)
    button_par=tk.Button(newWindow, text="GO")

    labelExample.pack()
    button_par.place(x=200, y=100)


#메인에 대한 값들
root =tk.Tk()

root.title("파티 편집기 v.1")
root.geometry("800x800")
root.resizable(False, False)
Label_vs=tk.Label(root, text="test")
Label_vs.place(x=400,y=400)


#입력 버튼

btn1=tk.Button(root, text="입력", command=window)
btn1.place(x=200,y=400)

#편성버튼

btn2=tk.Button(root, text="편성", command=window2)
btn2.place(x=600, y=400)

root.mainloop()


