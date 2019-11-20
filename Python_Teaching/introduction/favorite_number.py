import json


filename = "numbers.json"

try:
    with open(filename) as f:
        print(f"I know your favorite number! It's {json.load(f)}.")
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)

