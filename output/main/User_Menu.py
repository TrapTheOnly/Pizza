from tkinter import *
from tkinter.font import Font
import Pizza
import Barbeque_Pizza
import Pepperoni_Pizza
import time
import sqlite3


class user_menu:
    frame1=0
    frame2=0
    def __init__(self, frame, name):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.username = name
        self.frame1 = frame
        self.frame2 = frame
        self.font1 = Font(family="Times", size="32", weight="bold")
        self.font2 = Font(family="Times", size="24", weight="bold")
        Label(frame, text = 'Hi '+str(self.username), font = 'Times 26 bold', 
                bg = "#f2aca5", fg = 'black').grid(row = 0, column = 0,
                columnspan = 1, sticky = W)
        self.bbq_list = ['Chicken, Mozarella Cheese,', 'Mushrooms, BBQ Sauce']
        self.peppe_list = ['Pepperoni', 'Mozarella Cheese']
        self.label1 = Label(frame, text = 'Pizza Constructor\n', bg='#f2aca5',
                             fg='#10c200', font=self.font1)
        self.label1.grid(row=1, column=0, columnspan=3, sticky=N)
        Label(frame, text="\n\n\n\n\n\n")
        self.bbq_photo = PhotoImage(file="Photos/bbq_edited_gif.gif")
        self.peppe_photo = PhotoImage(file="Photos/pepperoni_edited_gif.gif")
        self.print_bbq = Label(frame, image=self.bbq_photo,
                                bg='#f2aca5', height=220, width = 320)
        self.print_bbq.grid(row=3, column=0, rowspan=3, sticky=W)
        self.bbq = IntVar()
        self.button1 = Checkbutton(frame, text="Barbeque",
                                    bg='#f2aca5', font = self.font2, fg='black',
                                    activebackground = '#f2aca5', variable=self.bbq)
        self.button1.grid(row=6, column=0)
        self.print_peppe = Label(frame, image=self.peppe_photo,
                                bg='#f2aca5', height=220, width = 320)
        self.print_peppe.grid(row=3, column=2, rowspan=3, sticky=E)
        self.peppe = IntVar()
        self.button2 = Checkbutton(frame, text="Pepperoni", bg='#f2aca5',
                                    font = self.font2, fg='black',
                                    activebackground = '#f2aca5', variable=self.peppe)
        self.button2.grid(row=6, column=2)
        self.bbq_ingredients = Label(frame, text = self.bbq_list[0]+'\n'+self.bbq_list[1],
                                     font = 'Times 12 bold', fg = 'gray', bg = '#f2aca5')
        self.bbq_ingredients.grid(row=7, column = 0, sticky = S, rowspan = 2)
        self.peppe_ingredients = Label(frame, text = self.peppe_list[0]+'\n'+
                                        self.peppe_list[1], font = 'Times 12 bold',
                                        fg = 'gray', bg = '#f2aca5')
        self.peppe_ingredients.grid(row=7, column = 2, sticky = S, rowspan = 2)
        self.space = Label(frame, text = '\n\n\n', bg='#f2aca5')
        self.space.grid(row = 9, column = 0, columnspan = 3)
        self.choice_button = Button(frame, text="Submit choice", bg='#f2aca5',
                                    font = self.font2, fg='black',
                                    activebackground = '#f2aca5', command = self.choice)
        self.choice_button.grid(row=9, column = 1, columnspan = 2)
        self.get_orders = Button(frame, text="Get Orders History", bg='#f2aca5',
                                font = self.font2, fg='black',
                                activebackground = '#f2aca5', command = self.orders)
        self.get_orders.grid(row = 9, column = 0)
    def choice(self):
        #print (self.bbq.get())
        #print (self.peppe.get())
        if(self.bbq.get()==1 and self.peppe.get()==0):
            #print("BBQ")
            self.bbq_func()
        elif(self.bbq.get()==0 and self.peppe.get()==1):
            #print("PEPPE")
            self.peppe_func()
        elif(self.bbq.get()==1 and self.peppe.get()==1):
            #print("BOTH")
            self.label2 = Label(self.frame1,
                                text = "Choose only one type of Pizza!",
                                 bg='#f2aca5', font = self.font2, fg='black')
            self.label2.grid(row=12, column=0, columnspan = 3)
            button1 = Button(self.frame1, text = 'Kill label', command = self.label2.destroy)
            button1.after(2000, button1.invoke)
        elif(self.bbq.get()==0 and self.peppe.get()==0):
            #print("NONE")
            self.label2 = Label(self.frame1,
                                text = "Choose something before clicking!",
                                 bg='#f2aca5', font = self.font2, fg='black')
            self.label2.grid(row=12, column=0, columnspan = 3)
            button1 = Button(self.frame1, text = 'Kill label', command = self.label2.destroy)
            button1.after(2000, button1.invoke)

    def orders(self):
        self.frame1.geometry("650x745+70+10")
        Label(self.frame1, text = '\n', bg = '#f2aca5', 
            font = 'Times 3 bold').grid(row = 11, column = 0, columnspan = 3)
        self.print_orders = Text(self.frame1, font = self.font2,
                                height = 5, width = 38)
        self.print_orders.grid(row = 12, column = 0, columnspan = 3, sticky = S)
        self.c.execute("SELECT * FROM users WHERE login = ?", (str(self.username),))
        self.list = list(self.c.fetchone())
        self.data = ""
        for i in range(1):
            self.data += str(self.list[2])
            self.data += '\n'
        self.print_orders.insert(INSERT, self.data)
        self.button3 = Button(self.frame1, command = lambda: {self.print_orders.destroy(), self.frame1.geometry("650x720+70+42")})
        self.button3.after(3000, self.button3.invoke)

    def bbq_func(self):
        #print("BBQ")
        self.frame1.destroy()
        bbq_obj=Barbeque_Pizza.BBQ(self.username)

    def peppe_func(self):
        #print("Peppe")
        self.frame1.destroy()
        peppe_obj=Pepperoni_Pizza.Peppe(self.username)


def game(login):
    root = Tk()
    root.geometry("650x720+70+42")
    root.title("Pizza constructor app")
    root.resizable(0,0)
    root.configure(background="#f2aca5")
    menu=user_menu(root, login)
    root.mainloop()