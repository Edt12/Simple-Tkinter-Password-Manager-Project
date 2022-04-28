from tkinter import *
#creating main password screen window
root=Tk()
root.title("Password Manager")
root.geometry("1366x768")
screen_width=root.winfo_screenwidth()#gets screen width
screen_height=root.winfo_screenheight()#gets screen height

bg=PhotoImage(file="Background.png")
Back=Label(Canvas,image=bg)
Back.pack()
#setting background
canvas=Canvas(root,width=screen_width, height=screen_height)
canvas.config(bg="white")
canvas.pack()
#creating lines
canvas.create_line(300,0,300,screen_width,fill="black",width=25)
canvas.create_line(0,100,screen_width,100,fill="black",width=25)#x,y,x1,y1 warning grid system is weird lower y is higher
#creating Labels
passwordLabel=Label(root,bg="white", text="Passwords",font=("freesans",20))#set window then text then font then size
passwordLabel.place(x=50,y=50)
root.mainloop()