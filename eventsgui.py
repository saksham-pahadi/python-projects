from tkinter import *

def harry(event):
    
    print=Label(root,text=f"you clicked on button at {event.x},{event.y}")
    print.pack()
    print(f"you clicked on button at {event.x},{event.y}")
    


root=Tk()
# gui logic here

# width x height
canvas_width = StringVar()
canvas_height = StringVar()
def apply():
    
    root.geometry(f"{canvas_width}x{canvas_height}")
# root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Events in GUI Python")
# width , height 
root.minsize(400,200) 
Label(text="Enter window width").pack()
Entry(root,textvariable=canvas_width).pack()
Label(text="Enter window height").pack()
Entry(root,textvariable=canvas_height).pack()
Button(root,text="Apply",command=apply).pack()
widget =Button(text="Click Here")
widget.pack()

widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)

root.mainloop()