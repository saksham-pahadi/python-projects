from tkinter import *


root=Tk()
# gui logic here

# width x height
root.geometry("500x400")
root.title("My GUI With harry")
# width , height
root.minsize(400,200)


f2=Frame(root,bg="gray")
f2.pack(side=TOP,fill=X)
# important label attribute
# text= adds the text ,font=("comicsansns",9,"bold")
# bd= background
# fg= foreground
# fonts = sets the fonts
# padx= padding on X axis
# pady= padding on y axis
# relief= border style - SUNKEN,RAISED,GROOVE,RIDGE
title_label=Label(f2,text=''' Windows PowerShell Help System SHORT DESCRIPTION Displays help about Windows PowerShell cmdlets and concepts.\n LONG DESCRIPTIONWindows PowerShell Help describes Windows PowerShell cmdlets,functions, scripts, and modules, and explains concepts, \nincludingthe elements of the Windows PowerShell language.''', bg="red",fg="aqua",padx=13,pady=4,font="comicsansns 9 bold",borderwidth=3,relief=GROOVE
                  )




# IMPORTANT PACK ATTRIBUTE
title_label.pack(side=LEFT,anchor="nw",fill=X)
f1=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f1.pack(side=TOP,fill=X)

l1=Label(f1,text="project Tkinter")
l1.pack(pady=42,padx=34)
l1=Label(f2,text="calculator",borderwidth=8,relief=SUNKEN)
l1.pack(padx=34)
f3=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f3.pack(side=LEFT,anchor="nw")
def hello():
    b2=Button(f3,fg="red",text="print now",borderwidth=6,relief=GROOVE)
    b2.pack(side=LEFT,pady=5)
    print("hello")
b1=Button(f3,fg="red",text="ADD",borderwidth=6,relief=GROOVE,command=hello)
b1.pack(side=LEFT,pady=11)







root.mainloop()