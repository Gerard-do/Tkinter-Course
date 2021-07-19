import tkinter

#Define Window
root = tkinter.Tk()
root.title('Window Basics!')
#User root.iconbtat to change the icon
root.geometry('400x250')
root.resizable(0,0)
root.config(bg='white')

#Second Window

top = tkinter.Toplevel()
top.title('Second Window')
top.config(bg='Black')
top.geometry('200x200+500+50')
#Run root window's mainloop
root.mainloop()
