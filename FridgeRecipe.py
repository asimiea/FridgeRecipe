import tkinter as tk
from tkinter import ttk

class FridgeRecipe(ttk.Frame):
    pass
    
    def main():
    root = tk.Tk()
    #app = App(root)
    root.mainloop()    #app.mainloop() or root.mainloop()?

from tkinter import *
from tkinter import ttk
r = Tk()
r.title('FridgeRecipe')
r.minsize(500,150)
#first page
frame1 = ttk.Frame(r, padding=1)
frame1.grid()
ttk.Label(frame1, text="Welcome! \nCheck one below").grid(column=0, row=0)

var1 = IntVar()
Checkbutton(frame1, text='Vegetarian', variable=var1).grid(row=4, sticky=W)#remove sticky
var2 = IntVar()
Checkbutton(frame1, text='Non-Vegetarian', variable=var2).grid(row=5, sticky=W)

#second page
frame2 = ttk.Frame(r, padding = 1)
frame2.grid
ttk.Label(frame2, text="Welcome! \nCheck one below").grid(column=0, row=0)

ttk.Button(frame1, text="Next", command=frame2).grid(column=1, row=6)

#button = Button(r, text='Search', width=25, command=r.destroy)#replace command w search internet
#button.pack()
r.mainloop()

	