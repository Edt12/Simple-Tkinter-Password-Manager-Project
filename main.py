from tkinter import *
#Main Window
#creating main password screen window
main=Tk()
main.title("Password Manager")
main.geometry("1366x768")
screen_width=main.winfo_screenwidth()#gets screen width
screen_height=main.winfo_screenheight()#gets screen height

bac=PhotoImage(file="Background.png")
Back=Label(main,image=bac)#Remember to add background image later


#setting background
canvas=Canvas(main,width=screen_width, height=screen_height)
canvas.config(bg="white")
canvas.pack()
#creating lines
canvas.create_line(200,0,200,screen_height,fill="blue",width=25)
canvas.create_line(0,100,screen_width,100,fill="blue",width=25)#x,y,x1,y1 warning grid system is weird lower y is higher
#creating labels
passwordLabel=Label(main,bg="white", text="Passwords",font=("freesans",20))#set window then text then font then size
passwordLabel.place(x=50,y=50)
NewPasswordImg=PhotoImage(file="Create Password Button.png")
#commands for buttons
def newPasswordclick():
    pass

#creating buttons
newPassword=Button(main,image=NewPasswordImg,compound="center",text="Create new password",command=newPasswordclick)#to combine text with image need to set compound to center,left or right which determines where text is put
newPassword.config(height=50,width=150)
newPassword.place(x=20,y=125)


main.mainloop()
