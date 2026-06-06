from student import Student

students = []

#---------------------------------------------
# ADD STUDENT
#---------------------------------------------
def add_student():
    name = input("\n  Name: ").strip().capitalize()
    age = int(input("  Age: "))
    score = int(input("  Score: "))
    
    student = Student(name, age, score)
    students.append(student)
    print(f"  {student.name} added successfully!")
    
#---------------------------------------------
# VIEW STUDENTS    
#---------------------------------------------
def view_students():
    print("\n" + "=" * 44)
    print(f"  📜 ALL STUDENTS ({len(students)})")
    print("=" * 44)
    if not students:
        print("  No student Found.")
    else:
        for i, s in enumerate(students):
            print(f"  {i}. {s}")
    print("=" * 44)
    
#---------------------------------------------
# UPDATE STUDENT
#---------------------------------------------
def update_student():
    index = int(input("\n  Student index: "))
    if index < len(students): 
        students[index].name = input("  New name: ")    
        students[index].age = input("  New age: ")
        students[index].score = input("  New score: ")
        print("  ✅ Updated successfully")
        view_students()
    else:
        print("  ❌ Index not found.")
        
#---------------------------------------------
# DELETE STUDENT
#---------------------------------------------
def delete_student():
    index = int(input("\n  Enter student index: "))
    if index < len(students):
        students.pop(index)
        print("  🗑️ Deleted successfully.")
    else:
        print("  ❌  Index not found.")

def menu():
    print("\n" + "=" * 44)
    print("  🧑🏼‍🎓 STUDENT MANAGEMENT SYSTEM")
    print("=" * 44)
    print("  👤 1. Add student")
    print("  📜 2. View students")
    print("  📋 3. Update student")
    print("  🗑️ 4. Delete student")
    print("  👋 5. Exit")
    print("=" * 44)
    
#--------------------------------------------
# INTERACTION
#---------------------------------------------
def run():    
    while True:
        try:
            menu()
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
                print("  ❌ Invalid option")
                
        except ValueError:
            print("  ❌ Enter an integer.")
            
        input("\n  Press Enter to continue... ")
            
run()            
             