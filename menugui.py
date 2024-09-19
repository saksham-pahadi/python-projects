from tkinter import *


root=Tk()
# gui logic here

# width x height
canvas_width = 733
canvas_height = 566
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("My GUI With harry")
# width , height
root.minsize(400,200)
def myfunc():
    print("file opened")
    
# USE THESE TO CREAT A NON DROPDOWN MENU
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)



mainmenu=Menu(root)
submenu=Menu(mainmenu,tearoff=0)

submenu.add_command(label="New project",command=myfunc)
submenu.add_separator()
submenu.add_command(label="Save",command=myfunc)
submenu.add_command(label="Save as",command=myfunc)
submenu.add_separator()
submenu.add_command(label="print",command=myfunc)

mainmenu.add_cascade(label="File",menu=submenu)
root.config(menu=mainmenu)

submenu1=Menu(mainmenu,tearoff=0)

submenu1.add_command(label="Cut",command=myfunc)
submenu1.add_separator()
submenu1.add_command(label="Copy",command=myfunc)
submenu1.add_command(label="Paste",command=myfunc)
submenu1.add_separator()
submenu1.add_command(label="Find",command=myfunc)

mainmenu.add_cascade(label="Edit",menu=submenu1)
root.config(menu=mainmenu)

root.mainloop()