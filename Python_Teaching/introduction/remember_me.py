import json

filename = "username.json"

def get_stored_username():
    """Get stored username if available. """
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def validate_user(username):
    """Validate the given user."""
    print(f"Please Enter 'Yes' or 'No'")
    validation = input(f"Is '{username}' your username? ")
    return validation

def greet_user():
    """Greet the user by name. """
    username = get_stored_username()
    if username:
        if validate_user(username) == 'Yes':
            print(f"Welcome back, {username}")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}")          

greet_user()