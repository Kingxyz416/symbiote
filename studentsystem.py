students = []
 
def add_student():
    roll = int(input("Enter Roll Number: "))
 
    for s in students:
        if s["roll"] == roll:
            print("Student already exists with this roll number!")
            return
 
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))
 
    student = {"roll": roll, "name": name, "age": age, "marks": marks}
    students.append(student)
    print("Student added successfully!")
 
 
def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
 
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return
 
    print("Student not found!")
 
 
def search_student():
    roll = int(input("Enter Roll Number to search: "))
 
    for s in students:
        if s["roll"] == roll:
            print("Roll:", s["roll"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Marks:", s["marks"])
            return
 
    print("Student not found!")
 
 
def update_student():
    roll = int(input("Enter Roll Number to update: "))
 
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new Name: ")
            s["age"] = int(input("Enter new Age: "))
            s["marks"] = float(input("Enter new Marks: "))
            print("Student updated successfully!")
            return
 
    print("Student not found!")
 
 
def display_students():
    if len(students) == 0:
        print("No records to display.")
        return
 
    print("\nRoll\tName\t\tAge\tMarks")
    for s in students:
        print(s["roll"], "\t", s["name"], "\t\t", s["age"], "\t", s["marks"])
 
 
def main():
    while True:
        print("\n1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Display All Students")
        print("6. Exit")
 
        choice = int(input("Enter your choice: "))
 
        if choice == 1:
            add_student()
        elif choice == 2:
            delete_student()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            display_students()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
 
 
main()