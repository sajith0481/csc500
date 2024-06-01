def main():
    # Combined dictionary for courses
    courses = {
        'CSC101': {'room': '3004', 'instructor': 'Haynes', 'time': '8:00 a.m.'},
        'CSC102': {'room': '4501', 'instructor': 'Alvarado', 'time': '9:00 a.m.'},
        'CSC103': {'room': '6755', 'instructor': 'Rich', 'time': '10:00 a.m.'},
        'NET110': {'room': '1244', 'instructor': 'Burke', 'time': '11:00 a.m.'},
        'COM241': {'room': '1411', 'instructor': 'Lee', 'time': '1:00 p.m.'}
    }

    # Get user input for course number
    course_number = input("Enter a course number: ").upper()

    # Display the course information
    if course_number in courses:
        print(f"Room Number: {courses[course_number]['room']}")
        print(f"Instructor: {courses[course_number]['instructor']}")
        print(f"Meeting Time: {courses[course_number]['time']}")
    else:
        print("Course not found.")

if __name__ == "__main__":
    main()