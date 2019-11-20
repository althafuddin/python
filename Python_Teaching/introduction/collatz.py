def collatz(number):
    """Print the even or odd numbers and process them"""
    if number % 2 == 0:
        result = number//2
        return result
    if number % 2 == 1:
        result = 3 * number + 1
        return result




num_value = 100
print(num_value)
while num_value != 1:
    num_value = collatz(num_value)
    print(num_value)
