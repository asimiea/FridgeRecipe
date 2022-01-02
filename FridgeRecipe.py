from tkinter import * #as tk

r = Tk()
r.title('FridgeRecipe')

var1 = IntVar()
Checkbutton(r, text='Vegetarian', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(r, text='Non-Vegetarian', variable=var2).grid(row=1, sticky=W)

#button = Button(r, text='Search', width=25, command=r.destroy)#replace command w search internet
#button.pack()
r.mainloop()

