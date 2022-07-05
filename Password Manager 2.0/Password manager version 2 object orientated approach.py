#Password manager version 2 object orientated
"python.suggest.autoImports: false"#disables autoImports for python in vscode file

import tkinter as tk
import sqlite3
 

conn=sqlite3.connect("Passwords.db")
cursor=conn.cursor()
#creating database
conn.execute("""create table IF NOT EXISTS Passwords
(passwordName text PRIMARY KEY
,UserName text
,password text
)""")#inside are columns/categorys


class LoginWindow(tk.Tk):#tk is module name TK is class inside module which you are instanciating
    def __init__(self,*args,):#args lets you add a variable number of arguments to any 
        tk.Tk.__init__(self,*args)#initalises tkinter with same arguments as class
        self.geometry("1366x768")
        screenHieght=LoginWindow.winfo_screenheight(self)
        screenWidth=LoginWindow.winfo_screenwidth(self)
        self.username=tk.Entry(self,width=20)#takes entry class from tkinter module
        self.username.pack()
        self.password=tk.Entry(self,width=20)
        self.password.pack()
        #enter login details button
        def enterButtonClick(self):
            passwordLogin=self.password.get()
            usernameLogin=self.username.get()
            passwordLogin
            usernameLogin
            if usernameLogin=="steve" and usernameLogin=="123":
                self.destro(LoginWindow)

        self.Enter=tk.Button(self,text="Login",command=enterButtonClick)
        self.Enter.pack()

class PasswordsWindow(tk.Tk):#tk is module name TK is class inside module which you are instanciating
    def __init__(self,*args,):#args lets you add a variable number of arguments to any 
        tk.Tk.__init__(self,*args)#initalises tkinter with same arguments as class
        self.geometry("1366x768")

login_window=LoginWindow()
login_window.mainloop()