class Item:
    made_in = 'Chine'  # static variable shared by all object
    tariffs = "%100"  # static variable shared by all object

    def __init__(self, item_name, item_price):
        self.item_name = item_name  # instance variable
        self.item_price = item_price  # instance variable

    def __str__(self):  # instance method
        return f'Item Name: {self.item_name}, Item Price{self.item_price}'

    def __str__(self):  # instance method
        return f'{type(self).__name__}.{self.__dict__}'

    @staticmethod
    def static_method():  # they can not access static members
        print("f' This is static method {}'")

    @classmethod  # like static method in java
    def class_method(cls):  # this can access static members
        print(f"{cls.made_in}")


item1 = Item("Pen", 2)
item2 = Item("Book", 30)

print(item1)
print(item2)
print(Item.made_in)
print(Item.tariffs)

Item.class_method()
Item.static_method()

"""
Create Employee class:
    instance variables: employee_name, job_title, salary
    static_variables: pay_tax

    instance methods: 
        __init()__: declares and initalizes all the isnace variables
        __str()__: creates string version of the object
        work(): displaye  ${employee_name} is working

    class method:
        display_employee_tax_rate()


"""
