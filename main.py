from tkinter import *
from tkinter.font import Font
import time
import User_Menu
import Admin_Menu
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
                            font = self.font2)
        self.login_username.pack()
        self.login_password = Entry(self.root, width = 20, exportselection = 0, 
                            font = self.font2, show = '*')
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
                #user.add_order('Barbeque', self.login_username.get(), '12')
                self.label1 = Label(self.root, text = 'No such user. Registered new!\nYou can now log in!', 
                        bg = '#f2aca5', fg = 'black', 
                        font = 'Times 14 bold')
                self.label1.pack()
                self.login_password.delete(0, len(self.login_password.get()))
                self.login_username.delete(0, len(self.login_username.get()))
                #user.add_order('Barbeque', self.login_username.get(), '12')
                #self.button2 = Button(self.root, command = self.run_new_screen())
                #self.button2.after(2000, self.button2.invoke)
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
                    #user.add_order('Barbeque', self.login_username.get(), '12')
                    button1 = Button(self.root, command = self.label2.destroy)
                    button1.after(2000, button1.invoke)
                    #self.label2.after(1000 , lambda: self.label2.destroy())
                else:
                    #user.add_order('Pepperoni', self.login_username.get(), '10')
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
                #user.add_order('Barbeque', self.login_username.get(), '12')
                button1 = Button(self.root, command = self.label2.destroy)
                button1.after(2000, button1.invoke)
                #self.label2.after(1000 , lambda: self.label2.destroy())
    #def run_new_screen(self):
    #    self.root.destroy()
    #    User_Menu.game(self.name_user)
class User:
    def __init__(self, login, password, db):
        self.login = login
        #print(login)
        self.db = db
        self.password = password
        #print(password)
        self.c = self.db.cursor()
        self.c.execute("SELECT rowid FROM users WHERE login = ?", (str(self.login),))
        if len(self.c.fetchall())==0:
            self.c.execute("INSERT INTO users VALUES (?, ?, ?)", (str(self.login), str(self.password), 'None',))
        #self.c.execute("SELECT * FROM users WHERE login = ?", (str(self.login), ))
        #print(self.c.fetchone())
        self.db.commit()

    def add_order(self, pizza_type, login, price):
        self.c.execute("SELECT orders FROM users WHERE login = ?", (str(login), ))
        self.orders_list = str(list(self.c.fetchone())[0])
        #print(self.orders_list)
        if self.orders_list == 'None':
            self.orders_list = ""
        self.orders_list += str(pizza_type)
        self.orders_list += ' - '
        self.orders_list += str(price)
        self.orders_list += ', '
        self.c.execute("UPDATE users SET orders = ? WHERE login = ?", (self.orders_list, str(login),))
        self.db.commit()
    
    @property
    def name(self):
        return str(self.login)
    
    @property
    def orders(self):
        self.c.execute("SELECT orders FROM users WHERE login = ?", (str(login), ))
        self.orders_list = str(list(self.c.fetchone())[0])
        return str(self.orders_list)

def main():
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
    #c.execute("DELETE FROM users WHERE login = 'Ismail'")
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
    #c1.execute("INSERT INTO pizzas VALUES (?, ?, ?, ?)", (str('Barbeque'), int(12), str("Chicken, Mozarella Cheese, Mushrooms, BBQ Sauce"), int(1)))
    #c1.execute("INSERT INTO pizzas VALUES (?, ?, ?, ?)", (str('Pepperoni'), int(10), str("Ultra Pepperoni, Mozarella Cheese"), int(2)))
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

