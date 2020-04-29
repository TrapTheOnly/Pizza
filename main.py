from tkinter import *
from tkinter.font import Font
import time
from Pizzas import User_Menu
from Pizzas import Admin_Menu
import sqlite3

class main_menu:
    root = 0
    def __init__(self, frame, db):
        self.db = db
        self.c = self.db.cursor()
        self.root = frame
        self.font1 = Font(family="Times", size="32", weight="bold")
        self.font2 = Font(family="Times", size="24", weight="bold")
        self.username = ''
        self.password = ''
        Label(self.root, text = 'Pizza Login\n', 
            bg ="#f2aca5", fg = "#10c200", 
            font = self.font1).pack()
        Label(self.root, text = "Username:", 
            bg = "#f2aca5", fg = 'Black', font = self.font2).pack()
        self.login_username = Entry(self.root, width = 20, exportselection = 0,
                            font = self.font2, bg = '#dcaca5')
        self.login_username.pack()
        self.login_password = Entry(self.root, width = 20, exportselection = 0, 
                            font = self.font2, show = '*', bg = '#dcaca5')
        Label(self.root, text = "Password:", 
            bg = "#f2aca5", fg = 'Black', font = self.font2).pack()
        self.login_password.pack()
        Label(self.root, text = "\n", 
            bg = "#f2aca5", fg = 'Black', font = self.font2).pack()
        self.entry = False
        self.submit = Button(self.root, text = 'Login', bg = "#f2aca5", font = self.font2, command = self.check_entry)
        self.submit.pack()

    def check_entry(self):
        self.name_user = ''
        self.name_user += str(self.login_username.get())
        if self.login_username.get()!='admin':
            self.c.execute("SELECT rowid FROM users WHERE login = ?", (str(self.login_username.get()),))
            user =  User(self.login_username.get(), self.login_password.get(), self.db)
            if len(self.c.fetchall()) == 0:
                self.label1 = Label(self.root, text = 'No such user. Register new!', 
                        bg = '#f2aca5', fg = 'black', 
                        font = 'Times 14 bold')
                self.button1 = Button(self.root, command = self.register_user)
                self.label1.pack()
                button3 = Button(self.root, command = self.label1.destroy)
                self.button1.after(1200, self.button1.invoke)
                button3.after(2000, button3.invoke)
                self.login_password.delete(0, len(self.login_password.get()))
                self.login_username.delete(0, len(self.login_username.get()))
                def run_new_screen(self):
                    self.root.destroy()
                    User_Menu.game(self.name_user)
            else:
                self.c.execute("SELECT password FROM users WHERE login = ?", (str(self.login_username.get()), ))
                self.password = str(list(self.c.fetchone())[0])
                if self.password != self.login_password.get():
                    self.label2 = Label(self.root, text = 'Wrong Password!', 
                        bg = '#f2aca5', fg = 'black', 
                        font = self.font2)
                    self.label2.pack()
                    button1 = Button(self.root, command = self.label2.destroy)
                    button1.after(2000, button1.invoke)
                else:
                    self.root.destroy()
                    User_Menu.game(self.name_user)
        else:
            if self.login_password.get() == 'admin':
                self.root.destroy()
                Admin_Menu.game()
            else:
                self.label2 = Label(self.root, text = 'Wrong Password!', 
                    bg = '#f2aca5', fg = 'black', 
                    font = self.font2)
                self.label2.pack()
                button1 = Button(self.root, command = self.label2.destroy)
                button1.after(2000, button1.invoke)

    def register_user(self):
        self.new_user = Tk()
        self.new_user.geometry("400x300+480+42")
        self.new_user.title("Pizza App Register")
        self.new_user.resizable(0,0)
        self.new_user.configure(background="#f2aca5")
        Label(self.new_user, text = "Enter user's login: ", font = self.font2, 
            bg = '#f2aca5').pack()
        self.entry1 = Entry(self.new_user, bg = '#dcaca5', fg = 'black', font = 'Times 22 bold')
        self.entry1.pack()
        Label(self.new_user, text = "Enter user's password: ", font = self.font2, 
            bg = '#f2aca5').pack()
        self.entry2 = Entry(self.new_user, bg = '#dcaca5', fg = 'black', font = 'Times 22 bold', show = '*')
        self.entry2.pack()
        Label(self.new_user, text = "\n", 
            bg = "#f2aca5", fg = 'Black', font = self.font2).pack()
        button1 = Button(self.new_user, text = 'Sign Up', font = self.font2, 
                bg = '#f2aca5', command = self.make_register_true)
        button1.pack()
        self.new_user.mainloop()
        
    def make_register_true(self):
        user1 =  User(self.entry1.get(), self.entry2.get(), self.db)
        user1.create_new()
        Label(self.new_user, text = "Registered!", font = 'Times 18 italic', 
            bg = '#f2aca5').pack()
        button2 = Button(self.new_user, command = self.new_user.destroy)
        button2.after(2000, button2.invoke)


class User:
    def __init__(self, login, password, db):
        self.login = login
        self.db = db
        self.password = password
        self.c = self.db.cursor()
        self.true = False
        
        

    def create_new(self):
        self.c.execute("INSERT INTO users VALUES (?, ?, ?)", (str(self.login), str(self.password), 'None',))
        self.db.commit()
        self.true = True


    @property
    def name(self):
        return str(self.login)
    
    @property
    def orders(self):
        self.c.execute("SELECT orders FROM users WHERE login = ?", (str(login), ))
        self.orders_list = str(list(self.c.fetchone())[0])
        return str(self.orders_list)

def main():
    file = open("Pizzas/pizza_ings.txt", "w")
    file.write('0')
    file.close()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE users (
                login text,
                password text,
                orders text
        )""")
    except:
        pass
    conn.commit()
    conn1 = sqlite3.connect('pizza.db')
    c1 = conn1.cursor()
    try:
        c1.execute("""CREATE TABLE pizzas (
        		pizza_type text,
        		pizza_price integer,
        		ingredients text,
                id integer
            )""")
    except:
        pass
    conn1.commit()
    c1.execute("SELECT rowid FROM pizzas WHERE pizza_type = 'BlankPizza'")
    if len(c1.fetchall())==0:
        c1.execute("INSERT INTO pizzas VALUES (?, ?, ?, ?)", (str('BlankPizza'), int(5), str("Tomato"), int(1)))
        conn1.commit()
    c1.execute("SELECT rowid FROM pizzas WHERE pizza_type = 'Barbeque'")
    if len(c1.fetchall())==0:
        c1.execute("INSERT INTO pizzas VALUES (?, ?, ?, ?)", (str('Barbeque'), int(12), str("Chicken, Mozarella Cheese, Mushrooms, BBQ Sauce"), int(2)))
        conn1.commit()
    c1.execute("SELECT rowid FROM pizzas WHERE pizza_type = 'Pepperoni'")
    if len(c1.fetchall())==0:
        c1.execute("INSERT INTO pizzas VALUES (?, ?, ?, ?)", (str('Pepperoni'), int(10), str("Ultra Pepperoni, Mozarella Cheese"), int(3)))
        conn1.commit()
    conn1.commit()
    root = Tk()
    root.geometry("400x500+70+42")
    root.title("Pizza App Login")
    root.resizable(0,0)
    root.configure(background="#f2aca5")
    main=main_menu(root, conn)
    root.mainloop()
    

if __name__ == '__main__':
    main()

