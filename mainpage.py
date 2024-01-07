from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
root.title("Smart Library")
ttk.Label(frm, text="Welcome to the Smart Library!").grid(column=0, row=0)
ttk.Button(frm, text="Enter", command=root.destroy).grid(column=1, row=0)
root.mainloop()
text = "What is the title? "
title = input(text)
text = "How many pages does the book have?"
qtpage = input(text)
text = "Who is the author? "
author = input(text)
text = "What is the ISBN? "
isbn = input(text)
text = "Where is going to be? "
location = input(text)
text = "How many copies?"
qty = input(text)