from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(f"{scvalue.get()}{text}")
        screen.update()

root=Tk()
root.geometry("332x500")
root.minsize(322,450)
root.title("Calculator GUI")
root.wm_iconbitmap("favicon.ico")


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 30 bold",width=120)
screen.pack(ipadx=8,pady=10,padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="c",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="OFF",font="lucida 10 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,ipady=16)
b.bind("<Button-1>",exit)

b=Button(f,text="%",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="/",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=20,pady=12)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text=9,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12,)
b.bind("<Button-1>",click)

b=Button(f,text=8,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=7,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=20,pady=12)
b.bind("<Button-1>",click)


f.pack()
f=Frame(root,bg="grey")
b=Button(f,text=6,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=5,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=4,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=20,pady=12)
b.bind("<Button-1>",click)


f.pack()
f=Frame(root,bg="grey")
b=Button(f,text=3,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=2,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=1,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

f.pack()
f=Frame(root,bg="grey")
b=Button(f,text=".",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,ipadx=4,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=0,font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="00",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=15,ipadx=0,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="lucida 20 bold",borderwidth=5,relief=GROOVE)
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()