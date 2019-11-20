# def get_word_count(word, filename):
#     try:
#         with open(filename) as file_object:
#             contents = file_object.readlines():
#             contents.count(word)






filenames = 'dogs.txt',

for files in filenames:
    try:
        word_count = 0
        with open(files) as file_object:
            for line in file_object.readlines():
                word_count += line.count('dog')
            print(word_count)
    except FileNotFoundError:
        pass
        #print(f"{files} is not found in given location.")

