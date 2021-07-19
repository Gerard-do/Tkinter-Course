#Radio Buttons

import tkinter
from tkinter import IntVar, Label, StringVar

root = tkinter.Tk()
root.title('Radio Buttons Basics!')
root.geometry('500x500')
root.resizable(0,0)

#Define my functions

def make_label():
    '''Print to teh screen'''
    if number.get() == 1:
        num_label = tkinter.Label(output_frame, text="1 one 1")
    elif number.get() == 2:
        num_label = tkinter.Label(output_frame, text='2 two 2')

    num_label.pack()
#Define frames
input_frame = tkinter.LabelFrame(root, text='This is fun', width=350, height=50)
output_frame = tkinter.LabelFrame(root, width=350, height=300)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0,10))
output_frame.pack_propagate(0)

#Define widgets
#Define radio button
number = IntVar()
number.set(1)
radio_1 = tkinter.Radiobutton(input_frame, text='Print the number one!', variable = number, value=1)
radio_2 = tkinter.Radiobutton(input_frame, text='Print the number two!',variable = number, value=2)
print_button = tkinter.Button(input_frame, text='Print the number!', command=make_label)


radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


#Run the root window's mainloop
root.mainloop()