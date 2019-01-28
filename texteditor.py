# Tcl/Tk text documentation
from tkinter import *
import tkinter.filedialog
import os
import tkinter.messagebox

def cut():
    content_text.event_generate('<<Cut>>')

def paste():
    content_text.event_generate('<<Paste>>')

def copy():
    content_text.event_generate('<<Copy>>')

def undo():
    content_text.event_generate('<<Undo>>')

def redo(event=None):
    content_text.event_generate('<<Redo>>')
    return 'break'
def select_all (event=None):
    content_text.tag_add('sel','1.0','end')
    return 'break'
def find_text(event=None):
    search_toplevel = Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text="Find All:").grid(row=0, column=0,
    sticky='e')
    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2,
    sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='Ignore Case',variable=ignore_case_value).grid(
    row=1, column=1, sticky='e', padx=2, pady=2)
    Button(search_toplevel, text="Find All", underline=0,
    command=lambda: search_output( search_entry_widget.get(),
    ignore_case_value.get(), content_text, search_toplevel,
    search_entry_widget)).grid(row=0, column=2, sticky='e' +
    'w', padx=2, pady=2)
    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
        search_toplevel.protocol('WM_DELETE_WINDOW',
        close_search_window)
    return "break"
def search_output(needle, if_ignore_case, content_text,search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
    while True:
        start_pos = content_text.search(needle, start_pos,
        nocase=if_ignore_case, stopindex=END)
        if not start_pos:
            break
        end_pos = '{}+{}c'.format(start_pos, len(needle))
        content_text.tag_add('match', start_pos, end_pos)
        matches_found += 1
        start_pos = end_pos
    content_text.tag_config('match', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))
def save():
    file_object = tkinter.filedialog.asksaveasfile(mode='w')

def open_file():
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension='txt',
    filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0,_file.read())
def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"
def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[
            ("All Files","*.*"),
            ("Text Documents", "*.txt")
        ]
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name). PROGRAM_NAME))
        return "break"
def write_to_file(file_name):
    try:
        content = content_text.get(1.0,'end')
        with open(file_name,'w') as the_file:
            the_file.write(content)
    except IOError:
        pass
        #pass for now but we sho warning 
def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0,END)
def display_about_messagebox(event=None):
    tkinter.messagebox.showinfo(
    "About", "{}{}".format(PROGRAM_NAME, "\nTkinter GUI\
    Application\n Development Blueprints"))
def display_help_messagebox(event=None):
    tkinter.messagebox.showinfo(
    "Help", "Help Book: \nTkinter GUI Application\n Development\
    Blueprints", icon='question')
def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
        root.destroy()
PROGRAM_NAME ="Footprint Editor"
file_name = None
root = Tk()
root.title(PROGRAM_NAME)
menu_bar = Menu(root)

# file menu 

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', accelerator='Ctrl+N',underline=0, command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O',underline=0, command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S',underline=0,command=save)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S',underline=0,command=save_as )
file_menu.add_command(label='Exit', accelerator='Alt+F4',command= exit_editor)
# edit menn and items
edit_menu = Menu(menu_bar,tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', underline=0, command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', underline=0,command=redo)
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', underline=0,command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', underline=0, command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', underline=0, command=paste)
edit_menu.add_command(label='Find', accelerator='Ctrl+F', underline=0, command=find_text)
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', underline=0,command=select_all)

# about menu and items
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', underline=0, command=display_about_messagebox)
about_menu.add_command(label='Help', underline=0 ,accelerator="F1",command=display_help_messagebox)
menu_bar.add_cascade(label='File',menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='View')
menu_bar.add_cascade(label='About', menu=about_menu)

# shortcut bar
shortcut_bar = Frame(root, height=25, background='light sea green')
shortcut_bar.pack(expand='no', fill='x')

line_number_bar = Text(root, width=4, padx=3,takefocus=0,border=0,
background='cyan', state='disabled',wrap='none')
line_number_bar.pack(side='left',fill='y')

# Text content
content_text = Text(root, wrap='word',undo=1)
content_text.pack(expand='yes',fill='both')

# key binding
content_text.bind('<Control-y>', redo) # redo binding to small case y
content_text.bind('<Control-Y>', redo) # redo binding to capital case Y
content_text.bind('<Control-a>',select_all)  # select all binding small case a
content_text.bind('<Control-A>',select_all) # select all binding small case A
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-F4>', exit_editor)
content_text.bind('<KeyPress-F1>', display_help_messagebox)
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right',fill='y')
root.config(menu=menu_bar)
root.protocol('WM_DELETE_WINDOW', exit_editor)
root.mainloop()