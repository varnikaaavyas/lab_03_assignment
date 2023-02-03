# print('HELLO WORLD')
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name == name]
        return result

    def search_by_salary(self, operator, salary):
        if operator == ">":
            result = [emp for emp in self.employees if emp.salary > salary]
        elif operator == "<":
            result = [emp for emp in self.employees if emp.salary < salary]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= salary]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= salary]
        else:
            result = []
        return result

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000),
]

employee_table = EmployeeTable(employees)

while True:
    print("\nSelect a search parameter:")
    print("[1. Age, 2. Name, 3. Salary (>, <, <=, >=)]")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        age = int(input("Enter the age: "))
        result = employee_table.search_by_age(age)
    elif choice == 2:
        name = input("Enter the name: ")
        result = employee_table.search_by_name(name)
    elif choice == 3:
        operator = input("Enter the operator (>, <, <=, >=): ")
        salary = int(input("Enter the salary: "))
        result = employee_table.search_by_salary(operator, salary)
    else:
        print("Invalid choice. Try again.")
        continue
    if result:
        print("\nResult:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No result found.")