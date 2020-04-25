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
        Label(self.root, text = '\n', bg = '#f2aca5').pack()
        self.new_pizza_button = Button(self.root, text = 'Add New Pizza', bg = '#f2aca5',
                fg = "black", font = self.font2, activebackground = 'red', 
                command = self.create_new_pizza)
        self.new_pizza_button.pack()
        Label(self.root, text = '\n', bg = '#f2aca5').pack()
        Label(self.root, text = "Enter Username:", 
            bg = "#f2aca5", fg = 'black', font = self.font2).pack()
        self.error_message = Label(self.root, text = "No such user", bg = '#f2aca5',
                    fg = 'black', font = self.font2)
        
        self.username = Entry(self.root, width = 20, exportselection = 0,
                            font = self.font2)
        self.username.pack()
        Label(self.root, text = '', bg = '#f2aca5').pack()
        self.button = Button(self.root, text = 'Search', bg = '#f2aca5',
                fg = "black", font = self.font2, activebackground = 'red', 
                command = self.check)
        self.button.pack()
        Label(self.root, text = '', bg = '#f2aca5').pack()
        self.data_get = Text(self.root, width = 29, height = 8,
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
                self.data += "Orders: \n"
                self.data += str(self.list[2])
                self.data += '\n'
            self.data_get.insert(INSERT, self.data)
    
    def create_new_pizza(self):
        self.frame1 = Tk()
        self.frame1.geometry("370x620+450+42")
        self.frame1.configure(background = "#f2aca5")
        self.frame1.title("Add Pizza")
        self.frame1.resizable(0,0)
        Label(self.frame1, text = "Pizza Name:", bg = '#f2aca5',
            font = 'Times 32 bold').pack()
        self.entry_name = Entry(self.frame1, font = 'Times 22 bold')
        self.entry_name.pack()
        Label(self.frame1, text = '\n', font = 'Times 12 bold', bg = '#f2aca5').pack()
        Label(self.frame1, text = "Pizza Price:", bg = '#f2aca5',
            font = 'Times 32 bold').pack()
        self.entry_price = Entry(self.frame1, font = 'Times 22 bold')
        self.entry_price.pack()
        Label(self.frame1, text = '\n', font = 'Times 12 bold', bg = '#f2aca5').pack()
        Label(self.frame1, text = "Pizza Ingredients:", bg = '#f2aca5',
            font = 'Times 32 bold').pack()
        self.entry_ings = Text(self.frame1, font = 'Times 22 bold', height = 5, width = 20)
        self.entry_ings.pack()
        Label(self.frame1, text = '\n', font = 'Times 12 bold', bg = '#f2aca5').pack()
        Button(self.frame1, text = 'Submit', bg = '#f2aca5', 
                font = 'Times 22 bold', command = self.add_pizza).pack()

    def add_pizza(self):
        conn1 = sqlite3.connect('pizza.db')
        c = conn1.cursor()
        conn1.commit()
        c.execute("select count(*) from pizzas")
        row_count = c.fetchone()
        ingredients = str(self.entry_ings.get(1.0, END))
        c.execute("SELECT rowid FROM pizzas WHERE pizza_type = ?", (str(self.entry_name.get()),))
        if len(c.fetchall())==0:
            c.execute("INSERT INTO pizzas VALUES (?, ?, ?, ?)", 
                        (str(self.entry_name.get()), int(self.entry_price.get()), 
                        str(self.entry_ings.get(1.0, END)), int(row_count[0]+1)))
            conn1.commit()
            file = open("Pizzas/notifications.txt", 'w')
            file.write("New pizza added - {}!".format(str(self.entry_name.get())))
            file.close()
            Label(self.frame1, text = 'Added!', font = 'Times 22 bold',
                bg = '#f2aca5').pack()
            self.frame1.after(2000, self.frame1.destroy)
        else:
            label1 = Label(self.frame1, text = 'Already exists!', font = 'Times 22 bold',
                bg = '#f2aca5').pack()
            button1 = Button(self.frame1, command = label1.destroy)
            button1.after(2000, button1.invoke)

def game():
    conn = sqlite3.connect('users.db')
    conn.commit()
    root = Tk()
    root.title("Admin Menu")
    root.geometry("370x620+70+42")
    root.resizable(0,0)
    root.configure(background = "#f2aca5")
    main = admin_menu(root, conn)
    root.mainloop()
