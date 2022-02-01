from tkinter import *  # tkinter에서 모든 함수를 들고 옵니다.
win = Tk()
win.geometry("400x200")
win.title("grid")
win.option_add("*Font", "궁서 20")

btn1 = Button(win)
btn1.config(text="(0,0)")
btn1.grid(column=0, row=0)

btn2 = Button(win)
btn2.config(text="(1,0)")
btn2.grid(column=2, row=0)

btn3 = Button(win)
btn3.config(text="(0,3)")
btn3.grid(column=0, row=3)

btn4 = Button(win)
btn4.config(text="셀병합")
btn4.grid(column=0, row=0, columnspan=1)
win.mainloop()
