def int_input(prompt):
    while True:
        try:
            input_ = int(input(prompt))
            return input_
        except ValueError:
            print('Enter a valid Integer!')

print('Welcome to the addition and subtraction program!')

num1 = int_input('Please enter the first number: ')
num2 = int_input('Please enter the second number: ')

print(f'Using addition gives us the following: {num1} + {num2} = {num1 + num2}')
print(f'Using subtraction gives us the following: {num1} - {num2} = {num1 - num2}')
