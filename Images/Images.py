#Images

import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title('Images basics!')
root.geometry('700x700')

#Basics... works for png

my_image = tkinter.PhotoImage(file='Shield-2-icon.png')
my_lable = tkinter.Label(root, image=my_image)
my_lable.pack()

my_button = tkinter.Button(root, image=my_image)
my_button.pack()

#Not for jpeg

#cat_image = tkinter.PhotoImage(file='descarga.jpg')
#cat_label = tkinter.Label(root, image=cat_image)
#cat_label.pack()

#Using PIL for jpg


#Run root window's mainloop

root.mainloop()

