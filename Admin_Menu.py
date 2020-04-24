import sqlite3
from tkinter import *
from tkinter.font import Font

class admin_menu:
    def __init__(self, root, par):
        self.root = root
        self.conn = par
        self.font1 = Font(family="Times", size="32", weight="bold")
        self.font2 = Font(family="Times", size="24", weight="bold")
        self.c = self.conn.cursor()
        Label(self.root, text = "ADMIN SCREEN", 
            bg = "#f2aca5", fg = '#10c200', font = self.font1).pack()
        Label(self.root, text = "Enter Username:", 
            bg = "#f2aca5", fg = 'black', font = self.font2).pack()
        self.error_message = Label(self.root, text = "No such user", bg = '#f2aca5',
                    fg = 'black', font = self.font2)
        self.username = Entry(self.root, width = 20, exportselection = 0,
                            font = self.font2)
        self.username.pack()
        Label(self.root, text = '\n', bg = '#f2aca5').pack()
        self.button = Button(self.root, text = 'Search', bg = '#f2aca5',
                fg = "black", font = self.font2, activebackground = 'red', 
                command = self.check)
        self.button.pack()
        Label(self.root, text = '\n', bg = '#f2aca5').pack()
        self.data_get = Text(self.root, width = 20, height = 8,
                            font = 'Times 18 bold')
        self.data_get.pack()

    def check(self):
        print(str(self.username.get()))
        self.c.execute("SELECT rowid FROM users WHERE login = ?", (str(self.username.get()),))
        print(len(self.c.fetchall()))
        if(len(self.c.fetchall())==1):
            self.error_message.pack()
        elif len(self.c.fetchall()) == 0:
            self.c.execute("SELECT * FROM users WHERE login = ?", (str(self.username.get()),))
            self.list = list(self.c.fetchone())
            self.data = ""
            for i in range(1):
                self.data += "Login: "
                self.data += str(self.list[0])
                self.data += '\n'
                self.data += "Password: "
                self.data += str(self.list[1])
                self.data += '\n'
                self.data += "Orders: "
                self.data += str(self.list[2])
                self.data += '\n'
            self.data_get.insert(INSERT, self.data)


def game():
    conn = sqlite3.connect('users.db')
    conn.commit()
    root = Tk()
    root.title("Admin Menu")
    root.geometry("350x500")
    root.configure(background = "#f2aca5")
    main = admin_menu(root, conn)
    root.mainloop()