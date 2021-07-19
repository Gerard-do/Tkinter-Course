#Labels and Pack
import tkinter
from tkinter import font

#define window
root = tkinter.Tk()
root.title('Label Basics!')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg = 'blue')

#Create Widgets
name_label_1 = tkinter.Label(root, text = 'Hello my name is Bryan.')
name_label_1.pack()

name_label_2 = tkinter.Label(root, text= 'My name is Gerardo.', font =('Arial', 12, 'bold'))
name_label_2.pack(padx = 10, pady = 10)

name_label_3 = tkinter.Label(root, text = 'Hello motherfucker', font= ('Arial', 15))
name_label_3.config(bg='red')
name_label_3.pack(pady=(0,10), ipadx=10, ipady=10, anchor='w')

name_label_4 = tkinter.Label(root, text = 'Hello my names is Path.', bg = '#FFFFFF', fg='#123456')
name_label_4.pack(fill='both', expand=True, padx=10, pady=10) #Also you can use only X or Y 

#Run the roor windiwow's mainloop
root.mainloop()