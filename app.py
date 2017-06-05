# This is just a trial

students = {"name": "chandra",
            "marks": [80, 90, 76, 93, 60],
            "exams": {
                "final": 80,
                "midterm": 70
            }}

marks = students["marks"]
exams = students["exams"]

# This is the script to create the app which returns the student name and their marks.

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

# add_mark(s, 90) # Passing by reference


# An example which shows how passing by value works
# z = 10
#
# def add_numbers(x, y):
#     x = x + y
#
# add_numbers(z, 10) # Passing by value


def calculate_avg_marks(student):
    # Add together all the students marks

    # Divide them by total number of marks
    number = len(student['marks'])
    # What happens if the students have no marks yet?
    if number == 0:
        return 0
    total = sum(student['marks'])
    return total / number

# Test cases
s = create_student()
print(calculate_avg_marks(s))
add_mark(s, 50)
print(calculate_avg_marks(s))
add_mark(s, 100)
print(calculate_avg_marks(s))
