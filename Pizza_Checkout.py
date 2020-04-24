from tkinter import *
from tkinter.font import *
import User_Menu
import Pizza
import sqlite3

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
        self.frame.geometry("420x793+70+0")
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
            self.print_ingredients = Label(self.frame,text='Additions: You added nothing!',
                                    bg = '#f2aca5', fg = 'black', font = 'Times 20 bold')
            self.label_checkout = Label(self.frame, text = ' Checkout', bg = '#f2aca5',
                                    fg = '#10c200', font = 'Times 32 bold')
        
        elif(len(self.status)==1):
            self.check=True
            if(self.status[0]=='ExtraBBQSauce'):
                self.extention = 'Additions: '
                self.extention += self.listToString(self.status)
                self.print_ingredients = Label(self.frame,text=self.extention,
                                    bg = '#f2aca5', fg = 'black', font = 'Times 20 bold')
                #self.label_checkout = Label(self.frame, text = '   Checkout', bg = '#f2aca5',
                #                    fg = '#10c200', font = 'Times 32 bold')
            elif(self.status[0]=='ExtraKetchup'):
                #self.label_checkout = Label(self.frame, text = '      Checkout', bg = '#f2aca5',
                #                    fg = '#10c200', font = 'Times 32 bold')
                self.extention = 'Additions: '
                self.extention += self.listToString(self.status)
                self.print_ingredients = Label(self.frame,text=self.extention,
                                    bg = '#f2aca5', fg = 'black', font = 'Times 20 bold')
            elif(self.status[0]=='Beef'):
                #self.label_checkout = Label(self.frame, text = '           Checkout', bg = '#f2aca5',
                #                    fg = '#10c200', font = 'Times 32 bold')
                self.extention = 'Additions: '
                self.extention += self.listToString(self.status)
                self.print_ingredients = Label(self.frame,text=self.extention,
                                    bg = '#f2aca5', fg = 'black', font = 'Times 20 bold')
            elif(self.status[0]=='ExtraCheese'):
                #self.label_checkout = Label(self.frame, text = '      Checkout', bg = '#f2aca5',
                #                    fg = '#10c200', font = 'Times 32 bold')
                self.extention = 'Additions: '
                self.extention += self.listToString(self.status)
                self.print_ingredients = Label(self.frame,text=self.extention,
                                    bg = '#f2aca5', fg = 'black', font = 'Times 20 bold')
        elif(len(self.status)>1):
            self.print_status+='Additions:\n'
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
        #print (self.listToString(self.print_status))
        self.label_checkout.place(height = 40, width = 200, x = 110, y = 20)
        self.space = Label(self.frame, text = '\n\n\n', bg='#f2aca5')
        self.space.grid(row = 2, column = 0, columnspan = 3)
        if(len(self.status)>1):
            self.print_ingredients = Label(self.frame,text=self.listToString(self.print_status),
                                    bg = '#f2aca5', fg = 'black', font = 'Times 20 bold')
        self.print_ingredients.place(x = 20, y = 100)
        #print(self.pizza.extentions_list)

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
        self.bbq_button.place(x=10, y=370, width = 180)
        self.ketchup_button = Button(self.frame, text='Remove Ketchup', 
                                    bg = '#f2aca5', fg = 'black', 
                                    width = 20, height = 3,
                                    font = 'Times 12 bold',
                                    activebackground = 'red', command = self.remove_Ketchup)
        self.ketchup_button.place(x = 230, y = 370, width = 180)

        #-------------------------Get Price---------------------
        self.price_button = Button(self.frame, text = 'Get Price', 
                                    bg = '#f2aca5', fg = 'black', 
                                    width = 20, height = 3,
                                    font = 'Times 12 bold',
                                    activebackground = 'red', command = self.get_price)
        #self.big_space.grid(row = 14+self.rows_count, column = 0, columnspan = 3)
        self.price_button.place(x = 135, y = 490, width = 150)
        #self.space.grid(row = 18+self.rows_count, column = 0, columnspan = 3)

    def add_order(self, pizza_type, login, price):
        self.c.execute("SELECT orders FROM users WHERE login = ?", (str(login), ))
        self.orders_list = str(list(self.c.fetchone())[0])
        #print(self.orders_list)
        if self.orders_list == 'None':
            self.orders_list = ""
        self.orders_list += str(pizza_type)
        for i in range(len(self.pizza.extentions_list)):
            self.orders_list += '+'
            self.orders_list += str(self.pizza.extentions_list[i])
        self.orders_list += ' - '
        self.orders_list += str(price) + '$'
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
            self.label_error.place(x=50, y = 600)
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
            self.label_error.place(x=50, y = 600)
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
            self.label_error.place(x=50, y = 600)
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
            self.label_error.place(x=50, y = 600)
            self.button1 = Button(self.frame, command = self.label_error.destroy)
            self.button1.after(400, self.button1.invoke)

    def get_price(self):
        self.price = self.pizza.get_price()
        self.label_price = Label(self.frame, text = 'Price: '+ str(self.price), bg = '#f2aca5',
                                fg = 'black', font = 'Times 32 bold')
        self.label_price.place(x = 120, y = 650)
        self.add_order(str(self.pizza_type), str(self.login), str(self.price))

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