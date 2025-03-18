# List of students with their dictionaries
students = [
    {"name": "nusura niyomukiza", "index": 35435},
    {"name": "Leina bembnen", "index": 35443},
    {"name": "Aleksandra agata", "index": 35453}
]

# Loop through the list and display each student's name and index number
print("Student List:")
for student in students:
    print(f"Name: {student['name']}, Index: {student['index']}")


def add_student(student_list, new_student):
    student_list.append(new_student)
    return student_list
