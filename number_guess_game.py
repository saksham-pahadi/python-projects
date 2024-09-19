from random import *
from tkinter import *
def play():
    if(guess.get()==number.get()):
        Label(f2,text=f"YEEH! YOU WON BY GUESSING THE CORRECT NUMBER",borderwidth=2,relief=GROOVE).pack(pady=10)
        print(guess,number)
    else:
        print(guess,number)
        Label(f2,text=f"Opps! YOU FAILED BY GUESSING INCORRECT NUMBER\nThe correct number is {guess.get()}",borderwidth=2,relief=GROOVE).pack(pady=10)
root=Tk()
root.geometry("400x600")
root.minsize(200,300)
number=IntVar()
guess=IntVar()
guess.set(randint(1,10))
f1=Frame(root,height=10,bg="aqua",border=4,relief=GROOVE,pady=5)
f1.pack(fill=X)
f2=Frame(root,height=500,bg="lightgreen",border=4,relief=GROOVE,pady=5)
f2.pack(fill=X)
heading=Label(f1,text="NUMBER GUESS GAME",borderwidth=5,relief=GROOVE).pack()
Label(f2,text="GUESS A NUMBER BETWEEN 1-10",pady=10,padx=10,borderwidth=2,relief=GROOVE).pack()
Entry(f2,textvariable=number).pack(pady=10)
Button(f2,text="SUBMIT",pady=5,padx=10,borderwidth=2,relief=GROOVE,command=play).pack()
root.mainloop()