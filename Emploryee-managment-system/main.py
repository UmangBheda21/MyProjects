from employee import Employee
import database

def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = float(input("Enter Salary: "))

    new_employee = Employee(emp_id,name,position,salary)
    employees.append(new_employee.__dict__)
    database.save_employees(employees)
    print("Employee Aded Successfully")

def view_employees(employees):
    if not employees:
        print("No Employees Found.")
        return
    for emp_data in employees:
        emp = Employee(**emp_data)
        print(emp)

def update_employee(employees):
    emp_id = input("Enter Employee ID to Update: ")
    for emp_data in employees:
        if emp_data['emp_id'] == emp_id:
            emp_data['name'] = input("Enter new Name: ")
            emp_data['position'] = input("Enter new position: ")
            emp_data['salary'] = float(input("Enter new salary: "))
            database.save_employees(employees)
            print("Employee Updated Successfully")
            return
        print("Employee not found.")

def delete_employee(employees):
    emp_id = input("Enter employee ID to delete: ")
    for i, emp_data in enumerate(employees):
        if emp_data['emp_id'] == emp_id:
            employees.pop(i)
            database.save_employees(employees)
            print("Employee Deleted Successfully")
            return
        print("Employee not found.")


def main():
    employees = database.load_employees()

    while True:
        print("\nEmployee Managment System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            update_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            break
        else:
            print("Invalid choice. please try again")

    if __name__ == "__main__":
            main()