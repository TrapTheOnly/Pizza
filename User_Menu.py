from tkinter import *
from tkinter.font import Font
import Pizza
import Pizza_Order
import time
import sqlite3


class user_menu:
    frame1=0
    def __init__(self, frame, name, row_count):
        self.row_count = row_count
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.conn1 = sqlite3.connect('pizza.db')
        self.c1 = self.conn1.cursor()
        self.username = name
        self.frame1 = frame
        self.font1 = Font(family="Times", size="32", weight="bold")
        self.font2 = Font(family="Times", size="22", weight="bold")
        self.tab = Label(frame, text = '  ', bg = '#f2aca5', font = self.font2)
        self.space = Label(frame, text = '\n', bg='#f2aca5', font = self.font1)
        Label(frame, text = 'Hi '+str(self.username), font = 'Times 26 bold', 
                bg = "#f2aca5", fg = 'black').grid(row = 0, column = 0,
                columnspan = 1, sticky = W)
        self.tab.grid(row = 0, column = 1)
        self.get_orders = Button(frame, text="Get Orders History", bg='#f2aca5',
                                font = self.font2, fg='black',
                                activebackground = '#f2aca5', command = lambda:  self.orders(frame))
        self.get_orders.grid(row = 0, column = 2) 
        self.label1 = Label(frame, text = 'Pizza Constructor\n', bg='#f2aca5',
                             fg='#10c200', font=self.font1)
        self.label1.grid(row=1, column=0, columnspan=3, sticky=N)
        Label(frame, text="\n\n\n\n\n\n")
        self.pizza_vars = {}
        self.row = 6
        self.pizza_checks = {}
        self.pizza_checks[0]=100
        self.pizza_vars[0]=100
        for i in range(1, self.row_count+1):
            self.pizza_vars[i]=IntVar()
            self.c1.execute("SELECT pizza_type FROM pizzas WHERE id = ?", (i, ))
            a = str(list(self.c1.fetchone())[0])
            self.pizza_checks[i] = Checkbutton(frame, 
                        text = a, bg = '#f2aca5',
                        font = self.font2, fg = 'black', 
                        activebackground = '#f2aca5', 
                        variable = self.pizza_vars[i], 
                        onvalue = 1, offvalue = 0)
            self.pizza_checks[i].grid(row = self.row, column = 0, columnspan = 3)
            self.row+=1
        file = open("notifications.txt")
        line = file.readline()
        Label(frame, text = line, font = 'Times 18 italic', bg = '#f2aca5', 
                fg = 'gray').grid(row = 8+self.row_count, column = 0, columnspan = 3)
        file.close()
        self.space.grid(row = 9+self.row_count, column = 0, columnspan = 3)
        self.choice_button = Button(frame, text="Submit choice", bg='#f2aca5',
                                    font = self.font2, fg='black',
                                    activebackground = '#f2aca5', command = self.choice)  
        self.choice_button.grid(row=9+self.row_count, column = 0, columnspan = 3)
    def choice(self):
        self.pizza_list = []
        self.pizza_list.append(100)
        for i in range(1, self.row_count+1):
            self.pizza_list.append(self.pizza_vars[i].get())
        if(self.pizza_list.count(1) == 1):
            self.pizza_func(self.pizza_list.index(1))
        elif(self.pizza_list.count(1) > 1):
            self.label2 = Label(self.frame1,
                                text = "Choose only one type of Pizza!",
                                 bg='#f2aca5', font = self.font2, fg='black')
            self.label2.grid(row=10+self.row_count, column=0, columnspan = 3)
            button1 = Button(self.frame1, text = 'Kill label', command = self.label2.destroy)
            button1.after(2000, button1.invoke)
        elif(self.pizza_list.count(1)==0):
            self.label2 = Label(self.frame1,
                                text = "Choose something before clicking!",
                                 bg='#f2aca5', font = self.font2, fg='black')
            self.label2.grid(row=10+self.row_count, column=0, columnspan = 3)
            button1 = Button(self.frame1, text = 'Kill label', command = self.label2.destroy)
            button1.after(2000, button1.invoke)

    def orders(self, frame):
        self.size = "427x"
        self.height = 506+(self.row_count-3)*20
        self.size+=str(self.height)
        self.size+= "+70+42"
        self.print_orders = Text(frame, font = 'Times 16 bold',
                                bg = "#f2aca5",
                                height = 5, width = 38)
        self.print_orders.place(x = 2, y = self.height)
        self.c.execute("SELECT * FROM users WHERE login = ?", (str(self.username),))
        self.list = list(self.c.fetchone())
        self.data = ""
        for i in range(1):
            self.data += str(self.list[2])
            self.data += '\n'
        self.print_orders.insert(INSERT, self.data)
        self.button3 = Button(frame, command = lambda: self.print_orders.destroy())
        #self.button3.after(5000, self.button3.invoke)

    def pizza_func(self, id):
        #print("BBQ")
        self.c1.execute("SELECT pizza_type FROM pizzas WHERE id = ?", (int(id),))
        self.pizza_type = str(list(self.c1.fetchone())[0])
        self.frame1.destroy()
        pizza_obj=Pizza_Order.Pizza(self.username,self.pizza_type)


def game(login):
    conn = sqlite3.connect('pizza.db')
    c = conn.cursor()
    c.execute("select count(*) from pizzas")
    row_count = c.fetchone()
    size = "427x"
    height = 636+(row_count[0]-3)*20
    size+=str(height)
    size+= "+70+42"
    root = Tk()
    print(size)
    root.geometry(str(size))
    root.title("Pizza constructor app")
    #root.resizable(0,0)
    root.configure(background="#f2aca5")
    menu=user_menu(root, login, row_count[0])
    root.mainloop()
