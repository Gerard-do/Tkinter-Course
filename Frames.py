#Frames

import tkinter
from tkinter import BOTH

root = tkinter.Tk()
root.title('Frame Basics!')
root.geometry('500x500')
root.resizable(0,0)

#Example of why to use frames

#name_label = tkinter.Label(root, text='Enter your name: ')
#name_label.pack()
#name_button = tkinter.Button(root, text='Submit your name.')
#name_button.grid(row=0, column=1)

#Define Frames

pack_frame = tkinter.Frame(root, bg='red')
grid_frame1 = tkinter.Frame(root, bg='blue')
grid_frame2 = tkinter.LabelFrame(root, text='Grid system rules', borderwidth=5)

#Pack frames into the root

pack_frame.pack(fill=BOTH, expand=True)
grid_frame1.pack(fill='x', expand=True)
grid_frame2.pack(fill=BOTH, expand=True, padx=10, pady=10)

#Pack frame

tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()

#Grid one layout

tkinter.Label(grid_frame1, text='text').grid(row=0, column=0)
tkinter.Label(grid_frame1, text='text').grid(row=1, column=1)
tkinter.Label(grid_frame1, text='text').grid(row=2, column=2)
#tkinter.Label(grid_frame1, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row=3, column=0)

#Grid 2 layout

tkinter.Label(grid_frame2, text='aaaaaaaaaaaaaaaaaaaaaa').grid(row=0, column=0)
#Run root window's mainloop

root.mainloop()