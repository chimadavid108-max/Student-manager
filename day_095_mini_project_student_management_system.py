from student import Student

students = []

#---------------------------------------------
# ADD STUDENT
#---------------------------------------------
def add_student():
    name = input(" Enter name: ")
    age = input(" Enter age: ")
    score = input(" Enter score: ")
    
    student_info = Student(name, age, score)
    students.append(student_info)
    print(f" Student added successfully!")
    
#---------------------------------------------
# VIEW STUDENTS    
#---------------------------------------------    
def view_students():
    if not students:
        print(" No student Found.")
        return
        
    for i, student in enumerate(students):
        print(f" {i}: {student}")
        
#---------------------------------------------
# UPDATE STUDENT
#---------------------------------------------
def update_student():
    view_students()
    
    index = int(input(" Enter student index: "))
    if index < len(students): 
        students[index].name = input(" New name: ")    
        students[index].age = input(" New age: ")
        students[index].score = input(" New score: ")
        print("  Updated successfully")
    else:
        print(" Invalid index")
        
#---------------------------------------------
# DELETE STUDENT
#---------------------------------------------        
def delete_student():
    view_students()
    
    index = int(input("  Enter student index: "))
    if index < len(students):
        students.pop(index)
        print("  Deleted successfully")
    else:
        print("  Invalid index")


        
 #---------------------------------------------
# INTERACTION
#---------------------------------------------
def menu():    
    while True:
        print("=" * 44)
        print("  🧑🏼‍🎓 Student Management System")
        print("=" * 44)
        print("  1. Add student")
        print("  2. View students")
        print("  3. Update student")
        print("  4. Delete student")
        print("  5. Exit")
        print("=" * 44)
 
        op = input("  Choose: ")
        
        if op == "1":
            add_student()
        elif op == "2":
            view_students()
        elif op == "3":
            update_student()
        elif op == "4":
            delete_student()
        elif op == "5":
            print("  👋 Goodbye")
            break
        else:
            print("  Invalid option")
        input("  Press Enter to continue... ")
            
menu()            
             