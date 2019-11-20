class Resturants:
    """A simple attempt to create Resturants class"""

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.numbers_serverd = 0

    def describe_resturant(self):
        """Describe the resturant"""
        print(f"\nThe Resturant {self.resturant_name} does offer {self.cuisine_type} cuisine.")

    def open_resturant(self):
        """Mention the resturant is open"""
        print(f"The Resturant {self.resturant_name} is now open.")
    
    def get_numbers_served(self):
        """Print the number of customers served."""
        print(f"\n{self.resturant_name} served {self.numbers_serverd} people")

    def set_number_served(self, num_of_customers):
        """Set the number of customers to numbers_served. """
        self.numbers_serverd = num_of_customers
    
    def increment_number_served(self, customers):
        """Increment the number of customers by the customers number."""
        self.numbers_serverd += customers

class IcecreamStand(Resturants):
    """A simple model to create an Icecream Stand resturant"""

    def __init__(self, resturant_name, cuisine_type):
        """Initialize the attributes from the parent(Super) Class."""
        super().__init__(resturant_name, cuisine_type)
        self.icecream_flavors = ""

    def get_icecream_flavors(self):
        """Print out the list of icecream flavors. """
        print(f"These are the Ice-Cream Flavors Available:\n {self.icecream_flavors}")


icecream_stand = IcecreamStand('stoneclod', 'Icecream')

icecream_stand.describe_resturant()
icecream_stand.get_icecream_flavors()

icecream_stand.icecream_flavors='mango', 'strawberry', 'vanilla', 'pinapple'
icecream_stand.get_icecream_flavors()
