def reverse_string(word):
    return_string = ""
    return_string = [s+return_string for s in word]
    return return_string

print(reverse_string("Hello World"))