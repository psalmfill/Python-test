from tkinter import *

class Application(Frame):
   
    def __init__ (self, master=None):
        Frame.__init__ (self,master)
        self.grid 
        self.a = StringVar()
        self.master.geometry("500x500")
        self.grid(sticky=N+S+E+W)
        self.columnconfigure(0,minsize=10, weight=3)
        self.create_widgets()
    def create_widgets(self):
        top = self.winfo_toplevel()
        top.columnconfigure(1, weight=3)
        self.columnconfigure(1,weight=1)
        self.quitButton = Button( text='Quit',command=self.quit,bg='red', fg='white')
        self.quitButton.place(x=450,y=450)
        self.lname = Label(text='Username', bg='#ffffff')
        self.lname.grid(row=0,column=0)
        self.iname = Entry(textvariable=self.a)
        self.iname.grid(row=0,column=1, sticky=E+W,padx=10)
        self.lpass = Label(text='Password',bg='#ffffff')
        self.lpass.grid(row=2,column=0)
        self.ipass = Entry()
        self.ipass.grid(row=2,column=1, sticky=E+W ,pady=5 ,padx=10)
        self.lbtn = Button(text='Login', bg='gray',fg="#ffffff",command=self.clickme)
        self.lbtn.grid(row=3,column=1,ipadx=20,sticky=E+W,pady=5,padx=10)
        self.appmenu = Menu()
        self.listmenu1 = Menu
        # self.listmenu1.add_command(self,label='Quit', command=self.quit)
        self.appmenu.add_cascade(label="File",menu = self.listmenu1)
        self.appmenu.add_cascade(label="Edit")
        self.appmenu.add_cascade(label="Help")
        self.master.config(menu=self.appmenu)
    def clickme(self):
        self.lbtn.config(text=self.a.get())
app = Application()
app.master.title("Sample Application")
app.mainloop()