from tkinter import *

window = Tk()
window.geometry("443x527")
window.title("Integral Calculator")
window.configure(bg = "#FFFFFF")

f1 = Frame(window)
f2 = Frame(window)

f1.grid(row=0, column=0)
f2.grid(row=0, column=2)

l1 = Label(f1, text="Hello im from page 1", pady=2, font=("Inter", 16))
l1.grid(row=0, column=2)
l1.pack(side='top', anchor='center', pady=100)

l2 = Label(f2, text="Hello im from page 2", pady=2, font=("Inter", 16))
l2.grid(row=0, column=2)
l2.pack(side='top', anchor='center', pady=100)

b1 = Button(f1, text="Page 2", font=("Inter", 16), pady=2, command=lambda: f2.tkraise())
b1.pack()

b2 = Button(f2, text="Page 2", font=("Inter", 16), pady=2, command=lambda: f1.tkraise())
b2.pack()

f1.tkraise()
window.resizable(False, False)
window.mainloop()