from tkinter import *
#creating Window
root=Tk()
root.title("Password Manager")
root.geometry("1366x768")
root.config(bg="white")
canvas=Canvas(root,width=1366, height=768)
canvas.config(bg="white")
canvas.pack()
#creating lines
canvas.create_line(300,0,300,1766,fill="black",width=25)
canvas.create_line(0,100,1400,100,fill="black",width=25)#x,y,x1,y1 warning grid system is weird lower y is higher
#creating Labels
passwordLabel=Label(root, text="Passwords",)
passwordLabel.place(x=50,y=50)
root.mainloop()