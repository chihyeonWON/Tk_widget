from tkinter import *  # tkinter에서 모든 함수를 들고 옵니다.
win = Tk()
win.geometry("400x200")
win.title("grid")
win.option_add("*Font", "궁서 20")

btn1 = Button(win)
btn1.config(text="(0,0)")
btn1.grid(column=0, row=0)

win.mainloop()
