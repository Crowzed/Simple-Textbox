#create a simple gui
#calculator using tkinter
from tkinter import *
#creating a window
window = Tk()
window.title("Simple Textbox")
window.geometry("400x400")
window.configure(background = "light green")
#creating a label
lbl = Label(window, text = "Type some word", font = ("Arial Bold", 20))
lbl.grid(column = 0, row = 0)
#creating a text box
txt = Entry(window, width = 10)
txt.grid(column = 0, row = 1)
#creating a function
def clicked():
    res = txt.get()
    lbl.configure(text = res)
#creating a button
btn = Button(window, text = "Click Me", bg = "orange", fg = "red", command = clicked)
btn.grid(column = 0, row = 2)
window.mainloop()