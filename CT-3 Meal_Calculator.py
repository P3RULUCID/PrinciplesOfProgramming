import array
def int_input(prompt):
    while True:
        try:
            input_ = int(input(prompt))
            if input_ < 0:
                print('Please enter a non-negative number')
                continue
            return input_
        except ValueError:
            print('Enter a valid number')
def float_input(prompt):
    while True:
        try:
            input_ = float(input(prompt))
            if input_ < 0:
                print('Please enter a non-negative cost amount')
                continue
            return input_
        except ValueError:
            print('Enter a valid cost amount')
def receipt_print(name, cost):
    print(f'{name:<{30- len(name)}}${cost:.2f}')
            
tip_percentage = 0.18
sales_tax = 0.07
sub_total = 0.0
dish_names = []
dish_costs = array.array('f')
print('Welcome to the Meal Cost Calculator\n')

item_count = int_input('How many dishes were ordered for the meal\n')
for i in range(item_count):
    name = input('Enter name of dish:\n')
    cost = float_input('Enter cost of dish:\n')
    dish_names.append(name)
    dish_costs.append(cost)
    sub_total = sub_total + cost

tip_cost = tip_percentage * sub_total
tax_cost = sales_tax * sub_total
total_cost = tip_cost + tax_cost + sub_total
print('\nThank you and here is your reciept breakdown\n')

for i in range(item_count):
    receipt_print(dish_names[i], dish_costs[i])    
receipt_print('Subtotal:', sub_total)
receipt_print('Tip:', tip_cost)
receipt_print('Sales Tax:', tax_cost)
receipt_print('Total Cost:', total_cost)
