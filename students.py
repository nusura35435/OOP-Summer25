# List of students
students = ["nusura niyomukiza: 35434", "Leina Bengnen: 35443", "Alenksandra Agata: 35543"]

# Loop through the list and display each student's index and name
print("Student List:")
for name, index in enumerate(students):
    print(f"{name}: {index}")

def add_student(student_list, new_student):
    student_list.append(new_student)
    return student_list
