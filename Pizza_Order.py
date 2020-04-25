from tkinter import *
from tkinter.font import *
from Pizza import *
import User_Menu
import Pizza_Checkout


class Pizza:
    
    frame=0
    print_added=0
    pizza = 0
    pizza_type = 0

    def __init__(self, login, pizza_type):
        self.pizza_type = pizza_type
        self.login = login
        self.options()
    
    def options(self):
        self.frame = Tk()
        self.frame.geometry("420x760+70+0")
        self.frame.title("Pizza")
        self.frame.resizable(0,0)
        self.frame.configure(background="#f2aca5")
        self.bbq = PhotoImage(file = 'Photos/bbq_resized_gif.gif')
        self.cheese = PhotoImage(file = 'Photos/cheese_resized_gif.gif')
        self.ketchup = PhotoImage(file = 'Photos/ketchup_resized_gif.gif')
        self.beef = PhotoImage(file = 'Photos/beef_resized_gif.gif')
        self.label1 = Label(self.frame, text='Pizza', font='Times 32 bold', 
                            bg = '#f2aca5', fg = '#10c200')
        self.label1.grid(row=1, column=0, columnspan = 3, sticky =N)
        self.pizza = PizzaBuilder(str(self.pizza_type))
        
        #-------------------additional food----------------------
        self.label2  = Label(self.frame, text = 'Any additions to your pizza?', 
                            font='Times 24 bold', bg = '#f2aca5', fg = 'black')
        self.label2.grid(row=3, column = 0, columnspan=3, sticky = N)
        self.cheese_label = Label(self.frame, image = self.cheese, bg = '#f2aca5')
        self.cheese_label.grid(row = 4, column = 0, rowspan = 3, sticky = N)
        self.beef_label = Label(self.frame, image = self.beef, bg = '#f2aca5')
        self.beef_label.grid(row=4, column=1, rowspan = 3, sticky = E) 
        self.button_cheese = Button(self.frame, text = 'Add Cheese', bg = '#f2aca5', 
                                    fg = 'black', font = 'Times 18 bold',
                                    activebackground = 'red',
                                    command = self.Cheese)
        self.button_cheese.grid(row=7, column=0, sticky=S)
        self.button_beef = Button(self.frame, text = 'Add Beef', bg = '#f2aca5', 
                                    fg = 'black', font = 'Times 18 bold',
                                    activebackground = 'red',
                                    command = self.Beef)
        self.button_beef.grid(row=7, column=1, sticky=S)
        self.print_added = Label(self.frame, bg='#f2aca5', text = '\t\t',
                                fg  = 'black', font = 'Times 24 bold')
        self.print_added.grid(row=9, column = 0, columnspan=3, sticky = S)
        #------------------additional sauces----------------------
        self.space = Label(self.frame, text = '\n', bg='#f2aca5')
        self.space.grid(row = 10, column = 0, columnspan = 3)
        self.bbq_label = Label(self.frame, image=self.bbq, bg = '#f2aca5')
        self.bbq_label.grid(row=14, column=0, rowspan = 3, sticky = S)
        self.ketchup_label = Label(self.frame, image=self.ketchup, bg = '#f2aca5')
        self.ketchup_label.grid(row=14, column=1, rowspan = 3, sticky =S)
        self.space.grid(row = 17, column = 0, columnspan = 3)
        self.button_bbq = Button(self.frame, text = 'Add BBQ Sauce', bg = '#f2aca5', 
                                    fg = 'black', font = 'Times 18 bold',
                                    activebackground = 'red',
                                    command = self.add_BBQ)
        self.button_bbq.grid(row=18, column=0, sticky=S)
        self.button_ketchup = Button(self.frame, text = 'Add Ketchup', bg = '#f2aca5', 
                                    fg = 'black', font = 'Times 18 bold',
                                    activebackground = 'red',
                                    command = self.add_Ketchup)
        self.button_ketchup.grid(row=18, column=1, sticky=S)
        self.add_sauce = Label(self.frame, bg='#f2aca5', text = '\t\t',
                                fg  = 'black', font = 'Times 24 bold')
        self.add_sauce.grid(row=19, column = 0, columnspan=3, sticky = S)

        #-----------------Proceed----------------

        self.proceed_button = Button(self.frame, text = 'Proceed to checkout', bg = '#f2aca5',
                                    activebackground = 'red',
                                    fg = 'black', font = 'Times 24 bold', command = self.checkout)
        self.proceed_button.grid(row=21, column = 0, columnspan =3, sticky = S)

        self.frame.mainloop()

    def Cheese(self):
        self.pizza.add_extention('ExtraCheese')
        self.button1 = Button(self.frame, 
                            command = self.print_added.configure(text='Added Cheese'))
        self.button1.after(10, self.button1.invoke)
        #print(self.pizza.get_price(),'$')
        #print(self.pizza.get_status())
        self.button2 = Button(self.frame,
                            command = lambda: self.print_added.configure(text='\t\t'))
        self.button2.after(400, self.button2.invoke)

    def Beef(self):
        self.pizza.add_extention('Beef')
        self.button1 = Button(self.frame, 
                            command = self.print_added.configure(text='Added Beef'))
        self.button1.after(10, self.button1.invoke)
        #print(self.pizza.get_price(),'$')
        #print(self.pizza.get_status())
        self.button2 = Button(self.frame,
                            command = lambda: self.print_added.configure(text='\t\t'))
        self.button2.after(400, self.button2.invoke)

    def add_BBQ(self):
        self.pizza.add_extention('ExtraBBQSauce')
        self.button1 = Button(self.frame, 
                            command = self.add_sauce.configure(text='Added BBQ Sauce'))
        self.button1.after(10, self.button1.invoke)
        #print(self.pizza.get_price(),'$')
        #print(self.pizza.get_status())
        self.button2 = Button(self.frame,
                            command = lambda: self.add_sauce.configure(text='\t\t'))
        self.button2.after(400, self.button2.invoke)
    
    def add_Ketchup(self):
        self.pizza.add_extention('ExtraKetchup')
        self.button1 = Button(self.frame, 
                            command = self.add_sauce.configure(text='Added Ketchup'))
        self.button1.after(10, self.button1.invoke)
        #print(self.pizza.get_price(),'$')
        #print(self.pizza.get_status())
        self.button2 = Button(self.frame,
                            command = lambda: self.add_sauce.configure(text='\t\t'))
        self.button2.after(400, self.button2.invoke)

    def checkout(self):
        check = Pizza_Checkout.Checkout(self.pizza, self.login, self.pizza_type)
        #print("Works until here")
        self.frame.destroy()