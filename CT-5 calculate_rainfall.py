def int_input(prompt):
    while True:
        try:
            input_ = int(input(prompt))
            if input_ <= 0:
                print('Please enter a number greater than zero')
                continue
            return input_
        except ValueError:
            print('Enter a valid number')
            
def float_input(prompt):
    while True:
        try:
            input_ = float(input(prompt))
            if input_ < 0:
                print('Please enter a non-negative value')
                continue
            return input_
        except ValueError:
            print('Enter a valid value')

def calculate_rainfall():
    years = int_input("Enter the number of years: ")
    
    total_rainfall = 0
    total_months = years * 12
    
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        for month in range(1, 13):
            rainfall = float_input(f"Enter the rainfall (in inches) for month {month}: ")
            total_rainfall += rainfall
    
    average_rainfall = total_rainfall / total_months
    
    print(f"\nTotal number of months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

calculate_rainfall()
