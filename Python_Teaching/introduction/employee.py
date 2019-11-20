class Employee():
    """A simple class to store Employee data and Raise amount"""

    def __init__(self, first_name, last_name, salary):
        """Intialize the attributes for an Employee class"""
        self.first_name = first_name
        self.last_name  = last_name
        self.salary     = salary
    
    def give_raise(self, raise_amount=5000):
        """Add the raise amount to the annual salary"""
        self.salary += raise_amount
