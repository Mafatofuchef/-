from cProfile import label
from cgitb import text
from ctypes.wintypes import SIZE
from curses import newwin
import tkinter as tk
from turtle import width

def window():
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text="test2233",width=40, height=20)
    
    labelExample.pack()


def window2():
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text="test2213",width=40, height=20)

    labelExample.pack()

root =tk.Tk()



#메인에 대한 값들

root.title("파티 편집기 v.1")
root.geometry("800x800")
root.resizable(False, False)
Label_vs=tk.Label(root, text="test")
Label_vs.place(x=400,y=400)


#입력 버튼

btn1=tk.Button(root, text="입력", command=window)
btn1.pack()

#편성버튼

btn2=tk.Button(root, text="편성", command=window2)
btn2.pack()

root.mainloop()


