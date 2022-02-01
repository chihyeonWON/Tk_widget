from tkinter import *  # tkinter에서 모든 함수를 들고 옵니다.
win = Tk()
win.geometry("400x200")
win.title("place")
win.option_add("*Font", "궁서 20")

btn = Button(win)
btn.config(text="(0,0)")
btn.place(x=0, y=0)

win.mainloop()
