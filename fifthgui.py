from tkinter import *


root=Tk()
# gui logic here

# width x height
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("My GUI With harry")
# width , height
root.minsize(400,200)


can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
# the line goes from the point x1,y1 to x2,y2

can_widget.create_rectangle(0,0,800,400,fill="green")
can_widget.create_oval(100,100,700,300,fill="yellow")
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="blue")
can_widget.create_text(400,80,text="Python",font=("comicsansns",19,"bold"))


root.mainloop()