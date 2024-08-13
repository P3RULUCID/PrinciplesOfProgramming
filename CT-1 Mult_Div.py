def int_input(prompt):
    while True:
        try:
            input_ = int(input(prompt))
            return input_
        except ValueError:
            print('Enter a valid Integer!')

print('Welcome to the multiplication and division program!')

num1 = int_input('Please enter the first number: ')
num2 = int_input('Please enter the second number: ')

print(f'Using multiplication gives us the following: {num1} * {num2} = {num1 * num2}')

if num2 != 0:
    print(f'Using division gives us the following: {num1} / {num2} = {num1 / num2}')
else:
    print(f'Using division gives us the following: {num1} / {num2} = Undefined')
