from tkinter import *


root=Tk()
# gui logic here

# width x height
root.geometry("500x400")
root.title("My GUI With harry")
# width , height
root.minsize(400,200)



user=Label(root,text="username")
password=Label(root,text="password")
user.grid()
password.grid(row=1)

# variable calsses in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)


def getvals():
    
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")
    user1=Label(root,text=f"The value of username is {uservalue.get()}")
    password1=Label(root,text=f"The value of password is {passvalue.get()}\nhehe")
    user1.grid(row=3,column=1)
    password1.grid(row=4,column=1)
    
Button(text="Submit",command=getvals).grid()

root.mainloop()