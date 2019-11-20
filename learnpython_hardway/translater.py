def translater(phrase):
    translation = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in phrase:
        if letter in vowels:
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translater("something"))

