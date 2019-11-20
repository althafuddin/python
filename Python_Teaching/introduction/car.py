""" A Class that can be used to represent a car. """

class Car:
    """This is a Car Class"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year  = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descruptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it. ")
    
    def update_odometer(self, milage):
        """
        Set's the odometer reading to the given value. 
        Reject the change if it attemsts to rill the odometer back.  
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading. """
        self.odometer_reading += miles
    

class Battery():
    """ A simple attempt to model a battery for an electric car"""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """ This will check the battey size for an upgrade"""
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def get_software_update(self):
        """ This will let you know if the car needs a software update depends on the milage"""

        if self.odometer_reading >= 10_000:
            print(f"\nThis {self.get_descriptive_name()} require a software update!. It has {self.odometer_reading} miles on it. ")
        else:
            diff_miles = 10000 - self.odometer_reading
            print(f"\nThis {self.get_descriptive_name()} does not require a software update yet! \nIt has {self.odometer_reading} miles on the reading. Still {diff_miles} to go...")

