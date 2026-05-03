# name project (string)
project_name = 'Students Management System'
version = '1.0.0'
author = 'Zahra Parsa'

# integer, float, for calculations
min_passing_grade = 50
average_target = 50.7
max_grade = 100

# list of students 
students_list = ['Ali', 'Sara', 'Reza', 'Maryam', 'Hassan', 'Fatema']

# grade
project_name = 'Students Management System'
min_passing_grade = 20
student_grades = {
    'Ali': 85, 'Sara': 90, 'Reza': 75, 
    'Maryam': 95, 'Hassan': 80, 'Fatema': 88
}


# tuple, for course information
course_info = ('Math', 'History', 'Physics', 'English', 'Chemistry')

# dictionary, for student grades
student_grades = {
    'Ali': 85,
    'Sara': 90, 
    'Reza': 75, 
    'Maryam': 95,
    'Hassan': 30,
    'Fatema': 88 
}

# set, for unique departments
unique_departments = {'Computer Science', 'Mathematics', 'Physics', 'Chemistry', 'Biology'}

# bool, for active status
is_active = True

# --- output ---
print(f"Welcome to {project_name} version {version} by {author}!")

# second part 
print("n\--- the inquiry system is now active ---")

while True:
    search_name = input("\n Enter student's name ('exit'):")

    # Third part
    command = input("Enter command (search/add?exit): ")

    if command.lower() == 'exit':
        break

    elif command.lower() == 'all':
        print("\n--- All students and their grades ---")
        for student, grade in student_grades.items():
            status = "passed" if grade >= min_passing_grade else "failed"
            print(f"student: {student} | grade: {grade} | status: {status}")
    elif command.lower() == 'average':
        avg = sum(student_grades.values()) / len(student_grades)
        print(f"\n--- Average grade of all students: {avg:.2f} ---")

    elif command in student_grades:
            grade = student_grades[command]
            status ="passed" if grade >= min_passing_grade else "faild"



    elif command in student_grades:
        grade = student_grades[command]
        status = "passed" if grade >= min_passing_grade else "faild"
        print(f"result: {command} | grade: {grade} | status: {status}")

    else:
        print(f"student {command} not found in the system. please try again later.")
        confirm = input("Do you want to add this student to the system?")
        if confirm.lower() == 'yes':
            try:
                new_grade = float(input(f"Enter grade for {command}: "))
                studnet_grades[command] = new_grade
                print(F"student {command} added successfully with grade {new_grade}.")

            except ValueError:
                print("Invalid grade. please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")

                print("Goodbye! the program closed successfully.")




    if search_name.lower() == 'exit':
        print("The programm closed successfuly")
        break

    if search_name in student_grades:
        grade = student_grades[search_name]
        status = "passed" if grade >= min_passing_grade else "failed"
        print(f"result: {search_name} | grade: {grade} | status: {status}")
    else:
            print(f"student {search_name} not found in the system. please try again ")
            answer = input("Do you want to add this student to the system? (yes/no):")
            if answer.lower() == 'yes':
                try:
                    new_grade = int(input(f"Enter grade for {search_name}: "))
                    student_grades[search_name] = new_grade
                    print(f"Student {search_name} added to the system with grade {new_grade}.")
                except ValueError:
                    print("Invalid grade. Please enter a valid integer.")
                except Exception as e:
                    print(f"An error occurred: {e}")

# about grades
print(f"The minimum passing grade is {min_passing_grade}, the average target is {average_target}, and the maximum grade is {max_grade}.")

for student in students_list:
    # result of student grade
    grade = student_grades[student] 
    
    passed = grade >= min_passing_grade
    status = "passed" if passed else "failed"
    
    
    print(f"student: {student} | grade: {grade} | status: {status}")

# print course information
print(f"Active departments: {unique_departments}")
