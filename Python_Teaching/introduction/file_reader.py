with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip().replace('Python', 'C'))

