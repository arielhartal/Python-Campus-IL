from tkinter import *
import tkinter




def showImage():
    root = Tk()

    #canv = Canvas(master, width=80, height=80, bg='white')
    #canv.grid(row=2, column=3)

    img = PhotoImage(file="burger.png")
    l = Label(image=img)
    l.pack()
#    canv.create_image(20, 20, anchor=NW, image=img)





master = tkinter.Tk()
label = tkinter.Label(master, text="What's my favorite food?")
label.config(pady = 50, padx = 100, font=('Arial', 23))
label.pack()
button = tkinter.Button(master, text="Click to find out", command = showImage)
button.config(pady = 20)
button.pack()





tkinter.mainloop()