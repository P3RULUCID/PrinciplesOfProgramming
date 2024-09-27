room_numbers = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

def display_course_info(course_number):
    print(f"\nCourse: {course_number}")
    print(f"Room Number: {room_numbers[course_number]}")
    print(f"Instructor: {instructors[course_number]}")
    print(f"Meeting Time: {meeting_times[course_number]}")

available_courses = ', '.join(room_numbers.keys())
print("Welcome to the course query system!")

while True:
    print(f"\nAvailable courses: {available_courses}")
    course_number = input("Enter a course number from the list above (or type 'exit' to quit): ").upper()

    if course_number == 'EXIT':
        print("Exiting the course query system. Goodbye!")
        break

    if course_number in room_numbers:
        display_course_info(course_number)
    else:
        print(f"Error: Course {course_number} not found. Please try again.")
