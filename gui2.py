from tkinter import *
mygui = Tk()
mylabel = Label(text="Customer Name" ,fg='#dedede',background="green",font=('Broadway',24,'bold')).pack()

def hello():
    b = a.get()
    mylabel.cget(text=b)
def logout():
    b = a.get()

    mylabel.configure(text=b)

def mbox():
    # messagebox= Message()
    messagebox.showinfo(title='save',message='Are you sure to save')
def mquit():
    # messagebox= Message()
    messagebox.askyesno(title="Quit", message="Are you sure to quit")

a = StringVar()
mygui.title("Chrome")
mygui.geometry("500x500+0+0")
mybtn = Button(text="Sign Up",fg="white",bg="blue",font=25,command = hello).pack()
mybtn2 = Button(text="Register",fg="white",bg="black",font=25,command=logout).pack()
text = Entry(textvariable=a).pack()
appmenu = Menu()
# create a menu list 
listone = Menu()
listone.add_command(label='New File')
listone.add_command(label='Open File')
listone.add_command(label='Save',command=mbox)
listone.add_command(label='Quit',command=mquit)

listtwo = Menu()
listtwo.add_command(label='Undo')
listtwo.add_command(label='Redo')
listtwo.add_command(label='Cancel')
# add all menu item to menu
appmenu.add_cascade(label="File",menu=listone)
appmenu.add_cascade(label="Edit",menu = listtwo)
appmenu.add_cascade(label="View")
appmenu.add_cascade(label="Format")
appmenu.add_cascade(label="Help")
mygui.config(menu=appmenu)
mygui.mainloop()

