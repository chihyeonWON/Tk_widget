from tkinter import *  # tkinter에서 모든 함수를 들고 옵니다.
win = Tk()
win.geometry("400x200")
win.title("pack")
win.option_add("*Font", "궁서 20")

btn = Button(win)
btn.config(text="버튼")
btn.pack()

btn1 = Button(win)
btn1.config(text="버튼1")
btn1.pack(pady=40)

win.mainloop()
