print("Welcome to Employee Management System....")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
        
    
class Employee(Person):
    def __init__(self, employee_id, name, age, salary):
        super().__init__(name, age)
        self.__employee_id=employee_id
        self.__salary=salary
        
    def get_employee_id(self):
        self.__employee_id
    
    def get_salary(self):
        self.__salary
        
    def set_employee_id(self,salary):
        self.__salary=salary
        
    def display(self):
        print("Emloyee Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.__employee_id)
        print("Salary:",self.__salary)
        
        
        
class Manager(Employee):
    def __init__(self,employee_id,name,age,salary,department):
        super().__init__(employee_id,name,age,salary)
        self.department=department
    
    def display(self):
        super().display()
        print("Department:",self.department)
        
        
    
              
while True:
    print("Choose an operation:")
    print("1.Create a Person")
    print("2.Create an Employee")
    print("3.Create a Manager")
    print("4.Show Details")
    print("5.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
       name=input("Enter your name:")
       age=int(input("Enter your age:"))
       
       person = Person(name, age)
       
       print("person created with name:",name,"and age:",age)


    if choice==2:
        name=input("Enter name:")
        age=int(input("Enter age:"))
        employee_id=input("Enter Employee ID:")
        salary=input("Enter Salary:")
        
        employee = Employee(employee_id, name, age, salary)
        
        print(f"Employee created with name: {name}, age: {age}, ID: {employee_id}, and salary:")
        print(f"${salary}.")
        
    if choice==3:
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        employee_id=input("Enter Employee ID:")
        salary=input("Enter Salary:")
        Department=input("Enter Department:")
        
        manager = Manager(employee_id, name, age, salary, Department)
        
        print(f"Manager created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and department: {Department}.")      
        
    if choice==4:
        while True:
            print("Choose details to show:")
            print("1.Person")
            print("2.Employee")
            print("3.Manager")
            
            detail_choice=int(input("Enter your choice:"))
            if detail_choice==1:
                person.display()
                
            
            elif detail_choice==2:
                employee.display()
                
            
            elif detail_choice==3:
                manager.display()
            
            else:
                print("invalid choice")
            
            break
                  
            
    if choice==5:
        print("Thank you for using Employee Management System")
        break



 