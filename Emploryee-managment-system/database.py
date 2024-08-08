import json

DATABASE_FILE = 'employees.json'

def load_employees():
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_employees(employees):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(employees,file,indent=4)
