class Employee:
    def __init__(self,emp_id,name,position,salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"