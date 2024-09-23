def int_input(prompt):
    while True:
        try:
            input_ = int(input(prompt))
            if input_ < 0:
                print('Please enter a number greater than zero')
                continue
            return input_
        except ValueError:
            print('Enter a valid number')

def calculate_points(books_purchased):
    if books_purchased == 0:
        return 0
    elif books_purchased == 2:
        return 5
    elif books_purchased == 4:
        return 15
    elif books_purchased == 6:
        return 30
    elif books_purchased >= 8:
        return 60
    else:
        return 0

def main():
    books_purchased = int_input("Enter the number of books purchased this month: ")
    
    points = calculate_points(books_purchased)
    
    print(f"Number of points awarded: {points}")

main()
