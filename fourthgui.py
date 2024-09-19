from tkinter import *


root=Tk()
# gui logic here

# width x height
canvas_width = 960
canvas_height = 543
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("My GUI With harry")
# width , height
root.minsize(400,200)

# HEADING
Label(root,text="welcome to harry travels",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
# TEXT FOR OUR FORM
name=Label(root,text="Name").grid(row=1,column=2)
phone=Label(root,text="Phone").grid(row=2,column=2)
gender=Label(root,text="Gender").grid(row=3,column=2)
emergency=Label(root,text="Emergency number").grid(row=4,column=2)
paymentmode=Label(root,text="Payment Mode").grid(row=5,column=2)
# VARIABLE FOR FORM
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()
# ENTRIES FOR A FORM
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)
# PACKING THE ENTRIES
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)
# CHECKBOX and packing it
foodservice=Checkbutton(text="Want to prebook your meals",variable=foodservicevalue).grid(row=6,column=3)
# BUTTON AND PACKING IT AND ASSIGN A COMMAND
def getvals():
    print("Submitting form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")
    
Button(text="Summit to harry Travels",command=getvals).grid(row=7,column=3)



root.mainloop()