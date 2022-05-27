
from tkinter import *
#login window
login=Tk()
login.title("Password Manager")
login.geometry("1366x768")
screen_width=login.winfo_screenwidth()#gets screen width
screen_height=login.winfo_screenheight()#gets screen height

loginBox=Entry(login,width=100)
loginBox.pack()


def loginClick():


    if loginBox.get()=="steve":

        #main window
        login.destroy()
        # creating main password screen window
        main = Toplevel()
        main.title("Password Manager")
        main.geometry("1366x768")
        screen_width = main.winfo_screenwidth()  # gets screen width
        screen_height = main.winfo_screenheight()  # gets screen height

        # setting background
        canvas = Canvas(main, width=screen_width, height=screen_height)
        canvas.config(bg="white")
        canvas.pack()
        # creating lines
        canvas.create_line(200, 0, 200, screen_height, fill="blue", width=25)
        canvas.create_line(0, 100, screen_width, 100, fill="blue",
                           width=25)  # x,y,x1,y1 warning grid system is weird lower y is higher
        # creating labels
        passwordLabel = Label(main, bg="white", text="Passwords",
                              font=("freesans", 20))  # set window then text then font then size
        passwordLabel.place(x=50, y=50)
        NewPasswordImg = PhotoImage(file="Create Password Button.png")

        def generateButton():  # generates buttons to access passwords

                b=open("Database.txt","r")
                passwordNamedata=b.readline()
                usernameData=b.readline()
                passwordData=b.readline()
                print(passwordNamedata)
                print(usernameData)
                print(passwordData)
        generateButton()
        # commands for buttons
        def newPasswordclick():
            # creating Labels for search bars and title
            newPasswordlabel = Label(main, text="Create Password Screen", bg="white", font=("freesans", 20))
            newPasswordlabel.place(x=215, y=50)

            def nameEntry():
                passwordName = NameofPassword.get()
                username = Name.get()
                password = Password.get()  # gets input from the input box
                NameofPassword.delete(0, END)  # deletes text within the range of 0 to end
                Name.delete(0, END)
                Password.delete(0, END)
                D = open("Database.txt", "a")  # opens text filein append mode
                if passwordName != "" and username != "" and password != "":  # checks that the user has typed in all the input boxes
                    D.write(passwordName + "\n" + username + "\n" + password + "\n")
                    NameofPassword.destroy()  # destroy destroys labels and other widgets
                    Name.destroy()
                    Password.destroy()
                    UserNameLabel.destroy()
                    nameEnter.destroy()
                    newPasswordlabel.destroy()
                    NameofPasswordlabel.destroy()
                    PasswordLabel.destroy()

            # labels for buttons
            NameofPasswordlabel = Label(main, text="Enter the name of your password", bg="white", font=("freesans", 10))
            NameofPasswordlabel.place(x=215, y=125)

            UserNameLabel = Label(main, text="Enter your username or email address", bg="white", font=("freesans", 10))
            UserNameLabel.place(x=215, y=175)

            PasswordLabel = Label(main, text="Enter your password", bg="white", font=("freesans", 10))
            PasswordLabel.place(x=215, y=225)
            # creating search bars
            NameofPassword = Entry(main, width=100, highlightthickness=2, highlightbackground="black",
                                   highlightcolor="black")
            NameofPassword.place(x=215, y=150)

            Name = Entry(main, width=100, highlightthickness=2, highlightbackground="black",
                         highlightcolor="black")  # highlight attributes create border
            Name.place(x=215, y=200)

            Password = Entry(main, width=100, highlightthickness=2, highlightbackground="black", highlightcolor="black")
            Password.place(x=215, y=250)
            # buttons
            nameEnter = Button(main, text="Enter", command=nameEntry)
            nameEnter.place(x=850, y=250)

        # creating buttons
        newPassword = Button(main, image=NewPasswordImg, compound="center", text="Create new password",
                             command=newPasswordclick)  # to combine text with image need to set compound to center,left or right which determines where text is put
        newPassword.config(height=50, width=150)
        newPassword.place(x=20, y=125)

        main.mainloop()

loginButton=Button(login,text="Login",font=("freesans",20),command=loginClick,width=5,height=10)
loginButton.pack()
login.mainloop()