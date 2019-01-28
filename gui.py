from tkinter import *

root = Tk()
root.title('Cal')

def add_to_display():
    print(self)
mainframe =   Frame(root)
Label(text='0', height=2, bg= 'white', justify=LEFT, width=10).grid(row=0,columnspan=5, sticky='ew')

Button(mainframe,text='ON',font=24, width=5,bg='#000',fg='#fff').grid(row=1,column=0)
Button(mainframe,text='CE',font=24, width=5).grid(row=1,column=1)
Button(mainframe,text='C',font=24, width=5).grid(row=1,column=2)
Button(mainframe,text='*',font=24, width=5).grid(row=1,column=3)
Button(mainframe,text='7',font=24, width=5, command=add_to_display).grid(row=2,column=0)
Button(mainframe,text='8',font=24, width=5).grid(row=2,column=1)
Button(mainframe,text='9',font=24, width=5).grid(row=2,column=2)
Button(mainframe,text='4',font=2, width=5).grid(row=3,column=0)
Button(mainframe,text='5',font=24, width=5).grid(row=3,column=1)
Button(mainframe,text='6',font=24, width=5).grid(row=3,column=2)
Button(mainframe,text='1',font=24, width=5).grid(row=4,column=0)
Button(mainframe,text='2',font=24, width=5).grid(row=4,column=1)
Button(mainframe,text='3',font=24, width=5).grid(row=4,column=2)
Button(mainframe,text='-',font=24, width=5).grid(row=4,column=3)
Button(mainframe,text='0',font=24, width=5).grid(row=5,column=1)
Button(mainframe,text='.',font=24, width=5).grid(row=5,column=0)
Button(mainframe,text='00',font=24, width=5).grid(row=5,column=2)
Button(mainframe,text='/',font=24, width=5).grid(row=5,column=3)
Button(mainframe,text='+',font=24,width=5).grid(row=2,column=3, rowspan=2, sticky=NS)

mainframe.grid()
mainframe.config(pady=5,padx=5)
root.option_readfile('option.txt')
root.config(bg='pink')
root.mainloop()
