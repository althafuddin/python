class Users:
    """ A simple model to create class for storing Users"""

    def __init__(self, first_name, last_name, age, title, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age    = age
        self.title = title
        self.department = department
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\nUser {self.first_name} {self.last_name} with {self.title} as a title and working under {self.department} department. User {self.last_name} is {self.age} years old.")
    
    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}!!! \nWelcome to the User Profile.")

    def increment_login_attempts(self):
        """Increment the login_attempts value by 1 each time. """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the login_attempts value to zero. """
        self.login_attempts = 0

    def get_login_attempts(self):
        """Provide the attempts of logins"""
        print(f"User {self.last_name} tried login attempt(s) on {self.login_attempts} occasions")


class Privileges():
    """Instantiate the class to model the privilages. """

    def __init__(self, privileges=""):
        self.privileges = privileges

    def show_privileges(self):
        """Print the privileges of a user."""
        print(f"List of privileges for user:")
        for privilege in self.privileges:
            print(privilege.title())


class Administrator(Users):
    """Instantiate the class for Administrator user."""

    def __init__(self, first_name, last_name, age, title, department):
        """Initialize the attributes from the parent class."""
        super().__init__(first_name, last_name, age, title, department)
        self.privilages = Privileges()


admin = Administrator("Althafuddin", "Shaik", 29, "DevOps Engineer", "MDC")

admin.describe_user()
admin.privilages.show_privileges()

admin.privilages.privileges = 'can add post', 'can delete post', "can ban user"
admin.privilages.show_privileges()


