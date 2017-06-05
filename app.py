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
