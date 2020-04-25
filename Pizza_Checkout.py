from tkinter import *
from tkinter.font import *
import User_Menu
import Pizza
import sqlite3
from datetime import datetime

class Checkout:

    pizza = 0
    frame = 0
    price = 0
    
    def __init__(self, pizza, login, pizza_type):
        self.pizza = Pizza.PizzaBuilder(str(pizza_type))
        self.pizza_type = pizza_type
        self.login = login
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.create_frame(pizza)
    
    def create_frame(self, pizza_ex):
        self.pizza = pizza_ex
        self.frame = Tk()
        self.frame.geometry("420x600+70+0")
        self.frame.title("Pizza Checkout")
        self.frame.resizable(0,0)
        self.frame.configure(background="#f2aca5")
        self.checkout_func()
    
    def checkout_func(self):
        self.status = []
        self.print_status = []
        del self.status[:]
        del self.print_status[:]
        self.status = self.pizza.extentions_list
        self.check=False
        self.label_checkout = Label(self.frame, text = 'Checkout', bg = '#f2aca5',
                                    fg = '#10c200', font = 'Times 32 bold')
        self.rows_count=1
        if(len(self.status)==0):
            self.print_ingredients = Text(self.frame, width = 29, height =4,
                                    bg = '#f2aca5', fg = 'black', font = 'Times 20 bold')
            self.print_ingredients.insert(1.0, 'Additions: You added nothing!')
            self.label_checkout = Label(self.frame, text = ' Checkout', bg = '#f2aca5',
                                    fg = '#10c200', font = 'Times 32 bold')
        elif(len(self.status)>0):
            self.print_status+='Additions: '
        if(len(self.status)>0):
            for i in range (0, 4*int(len(self.status)/4)):
                self.print_status += self.status[i]
                if(i!=4*int(len(self.status)/4)-1 and self.check == False):
                    self.print_status += ', '
                if(i==4*int(len(self.status)/4)-1 and len(self.status)>4 and self.check == False):
                    self.print_status += ', '
                if(i%4==1 and len(self.status)!=1): 
                    self.print_status += '\n'
                    self.rows_count+=1
        self.rows_count+=1
        self.print_status+='\n'
        if(len(self.status)%4!=0 and len(self.status)>0):
            a=(len(self.status)%4)
            for i in range (len(self.status)-a, len(self.status)):
                    self.print_status += self.status[i]
                    if(i!=len(self.status)-1 and self.check == False):
                        self.print_status += ', '
                    if(i%4==1):
                        self.rows_count+=1
                        self.print_status+='\n'
        self.label_checkout.place(height = 40, width = 200, x = 110, y = 20)
        self.space = Label(self.frame, text = '\n\n\n', bg='#f2aca5')
        self.space.grid(row = 2, column = 0, columnspan = 3)
        if(len(self.status)>0):
            self.print_ingredients = Text(self.frame,
                                    bg = '#f2aca5', fg = 'black', 
                                    font = 'Times 20 bold',
                                    width = 29, height = 4)
            self.print_ingredients.insert(1.0, self.listToString(self.print_status))
        self.print_ingredients.place(x = 7, y = 100)

        #---------------Remove extention------------------
        self.label_error = Label(self.frame, text = 'No such addition for your Pizza',
                                bg = '#f2aca5', fg = 'black', font = 'Times 18 bold')
        self.big_space = Label(self.frame, text = '\n\n\n', bg='#f2aca5')
        self.big_space.grid(row = 6+self.rows_count, column = 0, columnspan = 3)
        self.cheese_button = Button(self.frame, text='Remove Cheese', 
                                    bg = '#f2aca5', fg = 'black', 
                                    width = 20, height = 3,
                                    font = 'Times 12 bold',
                                    activebackground = 'red', command = self.remove_cheese)
        self.cheese_button.place(x=10, y=250, width = 180)
        self.beef_button = Button(self.frame, text='Remove Beef', 
                                    bg = '#f2aca5', fg = 'black', 
                                    width = 20, height = 3,
                                    font = 'Times 12 bold',
                                    activebackground = 'red', command = self.remove_beef)
        self.beef_button.place(x=230, y = 250, width = 180)
        self.space = Label(self.frame, text = '\n\n', bg='#f2aca5')
        self.space.grid(row = 10+self.rows_count, column = 0, columnspan = 3)
        self.bbq_button = Button(self.frame, text='Remove BBQ Sauce', 
                                    bg = '#f2aca5', fg = 'black', 
                                    width = 20, height = 3,
                                    font = 'Times 12 bold',
                                    activebackground = 'red', command = self.remove_BBQ)
        self.bbq_button.place(x=10, y=350, width = 180)
        self.ketchup_button = Button(self.frame, text='Remove Ketchup', 
                                    bg = '#f2aca5', fg = 'black', 
                                    width = 20, height = 3,
                                    font = 'Times 12 bold',
                                    activebackground = 'red', command = self.remove_Ketchup)
        self.ketchup_button.place(x = 230, y = 350, width = 180)

        #-------------------------Get Price---------------------
        self.price_button = Button(self.frame, text = 'Get Price', 
                                    bg = '#f2aca5', fg = 'black', 
                                    width = 20, height = 3,
                                    font = 'Times 12 bold',
                                    activebackground = 'red', command = self.get_price)
        self.price_button.place(x = 135, y = 450, width = 150)

    def add_order(self, pizza_type, login, price):
        self.c.execute("SELECT orders FROM users WHERE login = ?", (str(login), ))
        self.orders_list = str(list(self.c.fetchone())[0])
        if self.orders_list == 'None':
            self.orders_list = ""
        self.orders_list += str(pizza_type)
        for i in range(len(self.pizza.extentions_list)):
            self.orders_list += '+'
            self.orders_list += str(self.pizza.extentions_list[i])
        self.orders_list += ' - '
        self.orders_list += str(price) + '$ - '
        self.orders_list += str(datetime.now())
        self.orders_list += '\n'
        self.c.execute("UPDATE users SET orders = ? WHERE login = ?", (self.orders_list, str(login),))
        self.conn.commit()

    def remove_cheese(self):
        if 'ExtraCheese' in self.pizza.extentions_list:
            self.pizza.remove_extention('ExtraCheese')
            for widget in self.all_children(self.frame):
                widget.destroy()
            self.checkout_func()
        else:
            self.label_error = Label(self.frame, text = 'No such addition for your Pizza',
                                bg = '#f2aca5', fg = 'black', font = 'Times 18 bold')
            self.label_error.place(x=50, y = 550)
            self.button1 = Button(self.frame, command = self.label_error.destroy)
            self.button1.after(400, self.button1.invoke)
        
    def remove_beef(self):
        if 'Beef' in self.pizza.extentions_list:
            self.pizza.remove_extention('Beef')
            for widget in self.all_children(self.frame):
                widget.destroy()
            self.checkout_func()
        else:
            self.label_error = Label(self.frame, text = 'No such addition for your Pizza',
                                bg = '#f2aca5', fg = 'black', font = 'Times 18 bold')
            self.label_error.place(x=50, y = 550)
            self.button1 = Button(self.frame, command = self.label_error.destroy)
            self.button1.after(400, self.button1.invoke)
    
    def remove_BBQ(self):
        if 'ExtraBBQSauce' in self.pizza.extentions_list:
            self.pizza.remove_extention('ExtraBBQSauce')
            for widget in self.all_children(self.frame):
                widget.destroy()
            self.checkout_func()
        else:
            self.label_error = Label(self.frame, text = 'No such addition for your Pizza',
                                bg = '#f2aca5', fg = 'black', font = 'Times 18 bold')
            self.label_error.place(x=50, y = 550)
            self.button1 = Button(self.frame, command = self.label_error.destroy)
            self.button1.after(400, self.button1.invoke)

    def remove_Ketchup(self):
        if 'ExtraKetchup' in self.pizza.extentions_list:
            self.pizza.remove_extention('ExtraKetchup')
            for widget in self.all_children(self.frame):
                widget.destroy()
            self.checkout_func()
        else:
            self.label_error = Label(self.frame, text = 'No such addition for your Pizza',
                                bg = '#f2aca5', fg = 'black', font = 'Times 18 bold')
            self.label_error.place(x=50, y = 550)
            self.button1 = Button(self.frame, command = self.label_error.destroy)
            self.button1.after(400, self.button1.invoke)

    def get_price(self):
        self.price = self.pizza.get_price()
        self.label_price = Label(self.frame, text = 'Price: '+ str(self.price)+'$', bg = '#f2aca5',
                                fg = 'black', font = 'Times 32 bold')
        button1 = Button(self.frame, command = self.bbq_button.destroy)
        button2 = Button(self.frame, command = self.ketchup_button.destroy)
        button3 = Button(self.frame, command = self.beef_button.destroy)
        button4 = Button(self.frame, command = self.cheese_button.destroy)
        button5 = Button(self.frame, command = self.price_button.destroy)
        button1.after(100, button1.invoke)
        button2.after(100, button2.invoke)
        button3.after(100, button3.invoke)
        button4.after(100, button4.invoke)
        button5.after(100, button5.invoke)
        self.label_price.place(x = 120, y = 300)
        self.add_order(str(self.pizza_type), str(self.login), str(self.price))
        button6 = Button(self.frame, command = lambda: User_Menu.game(str(self.login)))
        button6.after(4000, button6.invoke)
        button7 = Button(self.frame, command = self.frame.destroy)
        button7.after(4000, button7.invoke)

    def listToString(self, s):
        str1 = ""  
        for ele in s:  
            str1 += ele 
        return str1

    def all_children (self, wid):
        _list = wid.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list