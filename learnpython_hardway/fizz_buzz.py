

def fizz_buzz(numbers):
    for i, num in enumerate(numbers):
        if num % 3 == 0 and num%5 == 0:
            numbers[i] = 'FizzBuzz'
        elif num % 5 == 0:
            numbers[i] = 'Buzz'
        elif num % 3 == 0:
            numbers[i] = 'Fizz'
    return numbers
    


values = [1,2,3,4,5,6,8,9,10,11,12,15]

try:
    print(fizz_buzz(values))
except Exception as e:
    print(e)

print('word'.__len__)