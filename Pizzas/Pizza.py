import abc
from abc import ABCMeta
import sqlite3


class Pizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_price(self):
        pass
    @abc.abstractmethod
    def get_status(self):
        pass

class Pizza_None(Pizza):
    pizza_price=0
    def __init__(self, ingredients, price):
        self.pizza_price = price
        self.ingredients = ingredients
    def get_price(self):
        return self.pizza_price
    def get_status(self):
        return self.ingredients

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza=pizza
    
    def get_price(self):
        return self.pizza.get_price()
    
    def get_status(self):
        return self.pizza.get_status()


class UltraPepperoni(PizzaDecorator):
    def __init__(self, pizza):
        super(UltraPepperoni, self).__init__(pizza)
        self.__upepperoni_price = 2

    @property
    def price(self):
        return self.__upepperoni_price

    def get_price(self):
        return super(UltraPepperoni, self).get_price() + self.__upepperoni_price

    def get_status(self):
        return super(UltraPepperoni, self).get_status() + ", Ultra Pepperoni" 

class ExtraCheese(PizzaDecorator):
	def __init__(self, pizza):
		super(ExtraCheese, self).__init__(pizza)
		self.__cheese_price = 2

	@property
	def price(self):
		return self.__cheese_price

	def get_price(self):
		return super(ExtraCheese, self).get_price() + self.__cheese_price

	def get_status(self):
		return super(ExtraCheese, self).get_status() + ", Cheese" 

class Beef(PizzaDecorator):
	def __init__(self, pizza):
		super(Beef, self).__init__(pizza)
		self.__beef_price = 4

	@property
	def price(self):
		return self.__beef_price

	def get_price(self):
		return super(Beef, self).get_price() + self.__beef_price

	def get_status(self):
		return super(Beef, self).get_status() + ", Beef"


class ExtraBBQSauce(PizzaDecorator):
	def __init__(self, pizza):
		super(ExtraBBQSauce, self).__init__(pizza)
		self.__bbq_sauce_price = 3

	@property
	def price(self):
		return self.__bbq_sauce_price

	def get_price(self):
		return super(ExtraBBQSauce, self).get_price() + self.__bbq_sauce_price

	def get_status(self):
		return super(ExtraBBQSauce, self).get_status() + ", Extra BBQ Sauce"

class Chicken(PizzaDecorator):
	def __init__(self, pizza):
		super(Chicken, self).__init__(pizza)
		self.__chicken_price = 3

	@property
	def price(self):
		return self.__chicken_price

	def get_price(self):
		return super(Chicken, self).get_price() + self.__chicken_price

	def get_status(self):
		return super(Chicken, self).get_status() + ", Chicken"
    
class Tomato(PizzaDecorator):
	def __init__(self, pizza):
		super(Tomato, self).__init__(pizza)
		self.__tomato_price = 2

	@property
	def price(self):
		return self.__tomato_price

	def get_price(self):
		return super(Tomato, self).get_price() + self.__tomato_price 

	def get_status(self): 
		return super(Tomato, self).get_status() + ", Tomato"


class ExtraKetchup(PizzaDecorator):
	def __init__(self, pizza):
		super(ExtraKetchup, self).__init__(pizza)
		self.__ketchup_price = 1

	@property
	def price(self):
		return self.__ketchup_price

	def get_price(self):
		return super(ExtraKetchup, self).get_price() + self.__ketchup_price

	def get_status(self):
		return super(ExtraKetchup, self).get_status() + ", Extra Ketchup"

class PizzaBuilder:

    def __init__(self, pizza_type):
        self.conn = sqlite3.connect('pizza.db')
        self.c = self.conn.cursor()
        self.pizza = 0
        self.extentions_list = []
        try:
        	self.c.execute("""CREATE TABLE pizzas (
        			pizza_type text,
        			pizza_price integer,
        			ingredients text
        	)""")
        except:
        	pass
        self.conn.commit()
        self.c.execute("SELECT rowid FROM pizzas WHERE pizza_type = ?", (str(pizza_type),))
        if len(self.c.fetchall())!=0:
            self.c.execute("SELECT pizza_price FROM pizzas WHERE pizza_type = ?", (str(pizza_type),))
            self.pizza_price = int(list(self.c.fetchone())[0])
            self.c.execute("SELECT ingredients FROM pizzas WHERE pizza_type = ?", (str(pizza_type),))
            self.ingredients = str(list(self.c.fetchone())[0])
            self.pizza_type=pizza_type
            self.pizza = Pizza_None(self.ingredients, self.pizza_price)
    
    def add_extention(self, extention):
        self.pizza=eval(extention)(self.pizza)
        self.extentions_list.append(extention)
    
    def remove_extention(self, extention):

        if(extention in self.extentions_list):
            self.extentions_list.remove(extention)

        self.pizza = PizzaBuilder(self.pizza_type)
        for ex in self.extentions_list :
            self.pizza.add_extention(ex)

    def get_price(self):
        return self.pizza.get_price()
    
    def get_status(self):
        return self.pizza.get_status()