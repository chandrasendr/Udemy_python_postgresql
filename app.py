student_list = []


def create_student():
    # Ask user for students name
    # Create the dictionary in the format {'name': '<student_name>', 'marks': []}
    # Return that dictionary
    name = input('Enter the student name: ')
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data


def add_mark(student, mark):
    # Append a mark to the student dictionary
    student['marks'].append(mark)
    return None


def calculate_avg_marks(student):
    # Add together all the students marks
    # Divide them by total number of marks
    number = len(student['marks'])
    # What happens if the students have no marks yet?
    if number == 0:
        return 0
    total = sum(student['marks'])
    return total / number


def print_student_details(student):
    # Print out a string that tells user important informationabout this student
    print('{}, average mark: {}'. format(student['name'],
                                         calculate_avg_marks(student)))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}". format(i))
        print_student_details(student)


def menu():
    # Adding a student (to student_list)
    # Add a mark to student
    # Print a list of students
    # Exit the application
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add new student, "
                      "'a' to add mark to student, or "
                      "'q' to quit")
    if selection == 'p':
        print_student_list(student_list)
    elif selection == 's':
        student_list.append(create_student())
    elif selection == 'a':
        student_id = int(input("Enter a student ID to add a mark to: "))
        student = student_list[student_id]
        new_mark = int(input("Enter the new mark to be added: "))
        add_mark(student, new_mark)

menu()


