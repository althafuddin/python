def calc_addition(int_a,int_b):
    """ Add the given two numbers """
    try:
        print (int(int_a) + int(int_b))
    except ValueError:
        print('You have to enter integers only!')


while True:
    number_1 = input("Enter your first number: ")
    number_2 = input("Enter your second number: ")
    if (number_1 == 'quit') or (number_2 == 'quit'):
        break
    else:
        calc_addition(number_1,number_2)