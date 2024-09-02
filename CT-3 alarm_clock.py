def int_input(prompt):
    while True:
        try:
            input_ = int(input(prompt))
            return input_
        except ValueError:
            print('Enter a valid Integer!')

def calculate_alarm_time(current_time, hours_to_wait):
    future_time = (current_time + hours_to_wait) % 24
    return future_time

print("Welcome to your Alarm Clock!\n")

while True:
    current_time = int_input("Enter the current time (in hours, 0-23):\n")
    if 0 <= current_time < 24:
        break
    else:
        print("Invalid time. Please enter a time between 0 and 23.")

while True:
    hours_to_wait = int_input("Enter the number of hours to wait for the alarm:\n")
    if hours_to_wait >= 0:
        break
    else:
        print("Invalid number of hours. Please enter a non-negative integer.")

alarm_time = calculate_alarm_time(current_time, hours_to_wait)
print(f"The alarm will go off at {alarm_time:02d}:00\n")
print("Program Terminating, Good-bye!")
