from tkinter import *


root=Tk()
# gui logic here

# width x height
root.geometry("500x400")
root.title("My GUI With harry")
# width , height
root.minsize(400,200)



sakshamtext=Label(text="saksham is a good boy",font=(10))
sakshamtext.pack()
photo=PhotoImage(file="Picsart_24-02-16_15-03-52-331.png")
sakshamimg=Label(image=photo,height=500,width=500,padx=10,pady=10)
sakshamimg.pack()

root.mainloop()