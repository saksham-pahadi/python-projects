from tkinter import *
import tkinter.messagebox as tmsg

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
    
def help():
    print("i will help you")
    tmsg.showinfo("help","harry will help you with gui")
def rate():
    value=tmsg.askquestion("rate us","Was your experince good?")
    print(value)
    if value=="yes":
        tmsg.showinfo("rate us","Great,please rate us on app store")
    else:
        msg="tell us what went wrong,i will call you"
        tmsg.showinfo("experience",msg)
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

submenu2=Menu(mainmenu,tearoff=0)

submenu2.add_command(label="HELP",command=help)
submenu2.add_separator()
submenu2.add_command(label="Rate us",command=rate)
submenu2.add_separator()
submenu2.add_command(label="Copy",command=myfunc)
submenu2.add_command(label="Paste",command=myfunc)
submenu2.add_separator()
submenu2.add_command(label="Find",command=myfunc)

mainmenu.add_cascade(label="Help",menu=submenu2)
root.config(menu=mainmenu)

root.mainloop()