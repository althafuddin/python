filename = 'guest.txt'
prompt = "Please enter your name:"
like_prompt = "Please enter your reason to like programming:"
print(f"Enter 'quit' to close the program.")

while True:
    guest_name = input(prompt)
    
    if guest_name == 'quit':
        break
    else:
        reason = input(like_prompt)
        with open(filename, 'a') as file_object:
            file_object.write(f"{guest_name.title()}: {reason}\n")
            