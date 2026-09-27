print("Welcome to Employee Management System....")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(f"pereson detail")
        print(f"Enter your name:{self.name}")
        print(f"Enter your age:{self.age}")
        
    def __del__(self):
        pass
    
# Base Class
class Employee:

    # Constructor / Method Overloading using default arguments
    def __init__(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter for employee_id
    def get_employee_id(self):
        self.__employee_id

    # Setter for employee_id
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for salary
    def get_salary(self):
        self.__salary

    # Setter for salary
    def set_salary(self, salary):
        self.__salary = salary

    # Display method
    def display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    # Destructor
    def __del__(self):
        pass


# Derived Class - Manager
class Manager(Employee):

    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print("Department:", self.department)


# Derived Class - Developer
class Developer(Employee):

    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)


# Checking Inheritance using issubclass()
print("\nInheritance Check:")
print("Is Manager subclass of Employee?", issubclass(Manager, Employee))
print("Is Developer subclass of Employee?", issubclass(Developer, Employee))


# Main Menu
while True:

    print("\nChoose an operation:")
    print("1. Create an Person")
    print("2. Create a Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    #Create Person
    if choice ==1:
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        person=Person(name,age)
        
        print(f"Person created with name:{name} and age:{age}")
        
    # Create Employee
    elif choice == 2:

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        employee_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")

        employee = Employee(name, age, employee_id, salary)

        print(f"Employee created with name:{name},age:{age},id:{employee_id},and salary:${salary}.")
            

    # Create Manager
    elif choice == 3:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        department = input("Enter Department: ")

        manager = Manager(
            employee_id,
            name,
            age,
            salary,
            department
        )

        print(f"Manager created with name: {name}, age: {age}, ID: {employee_id},salary:${salary}, and department:{department}")

    # Create Developer
    elif choice == 4:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        programming_language = input("Enter Programming Language: ")

        developer = Developer(
            employee_id,
            name,
            age,
            salary,
            programming_language
        )

        print(f"Developer created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and programming language: {programming_language}.") 

    # Show Details
    elif choice == 5:

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")

        detail_choice = int(input("Enter your choice: "))

        if detail_choice == 1:
            person.display()
            
        elif detail_choice==2:
            employee.display()
            

        elif detail_choice == 3:
            manager.display()
            
        elif detail_choice == 4:
            developer.display()
            
        else:
            print("Invalid choice.")

    # Exit
    elif choice == 6:

        print("Existing the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")