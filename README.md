# Name

**\[Asti Sojitra\]**

# Project Title

**Employee Management System using Python OOP Concept**

## Project Overview

The **Employee Management System** is a console-based Python project
developed using **Object-Oriented Programming (OOP)** concepts.

The project allows the user to create and manage different types of
objects such as **Person, Employee, Manager, and Developer**. It
demonstrates important Python OOP concepts including **classes, objects,
inheritance, encapsulation, method overriding, constructors,
destructors, getters, setters, and `issubclass()`**.

The system provides a menu-driven interface through which the user can
create objects and display their details.

## Features

-   Create a Person
-   Create an Employee
-   Create a Manager
-   Create a Developer
-   Display details of created objects
-   Check inheritance using `issubclass()`
-   Use inheritance between `Employee`, `Manager`, and `Developer`
-   Use encapsulation for Employee ID and Salary
-   Use method overriding in Manager and Developer
-   Use constructors and destructors
-   Menu-driven console interface

## OOP Concepts Used

### 1. Class and Object

The project defines several classes:

-   `Person`
-   `Employee`
-   `Manager`
-   `Developer`

Objects are created from these classes based on the user's menu
selection.

Example:

``` python
person = Person(name, age)
employee = Employee(name, age, employee_id, salary)
```

### 2. Constructor

The `__init__()` method is used as a constructor to initialize object
data.

For example:

``` python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

The `Employee` class also initializes:

-   Name
-   Age
-   Employee ID
-   Salary

### 3. Inheritance

`Manager` and `Developer` inherit from the `Employee` class.

``` python
class Manager(Employee):
```

``` python
class Developer(Employee):
```

This allows both classes to reuse the properties and methods of
`Employee`.

### 4. Encapsulation

Employee ID and Salary are stored using private attributes:

``` python
self.__employee_id = employee_id
self.__salary = salary
```

Getter and setter methods are provided to access and modify these
values.

``` python
def get_employee_id(self):
    return self.__employee_id

def set_employee_id(self, employee_id):
    self.__employee_id = employee_id
```

``` python
def get_salary(self):
    return self.__salary

def set_salary(self, salary):
    self.__salary = salary
```

### 5. Method Overriding

The `Manager` and `Developer` classes override the `display()` method of
the `Employee` class.

For example:

``` python
def display(self):
    super().display()
    print("Department:", self.department)
```

The `Developer` class similarly displays its programming language.

### 6. `super()`

The `super()` function is used to call the constructor and methods of
the parent class.

Example:

``` python
super().__init__(name, age, employee_id, salary)
```

It is also used inside the overridden `display()` methods:

``` python
super().display()
```

### 7. `issubclass()`

The project checks whether `Manager` and `Developer` are subclasses of
`Employee`.

``` python
print("Is Manager subclass of Employee?", issubclass(Manager, Employee))
print("Is Developer subclass of Employee?", issubclass(Developer, Employee))
```

Expected result:

``` text
Is Manager subclass of Employee? True
Is Developer subclass of Employee? True
```

### 8. Destructor

The classes include a `__del__()` method, which demonstrates the
destructor concept in Python.

Example:

``` python
def __del__(self):
    pass
```

## Program Menu

When the program runs, it displays the following menu:

``` text
Choose an operation:
1. Create an Person
2. Create a Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit
```

### Option 1: Create a Person

The user enters:

-   Name
-   Age

Example:

``` text
Enter your choice: 1
Enter your name: John Doe
Enter your age: 30
Person created with name:John Doe and age:30
```

### Option 2: Create an Employee

The user enters:

-   Name
-   Age
-   Employee ID
-   Salary

The program creates an `Employee` object and displays a confirmation
message.

### Option 3: Create a Manager

The user enters:

-   Name
-   Age
-   Employee ID
-   Salary
-   Department

A `Manager` object is created using the `Employee` parent class.

### Option 4: Create a Developer

The user enters:

-   Name
-   Age
-   Employee ID
-   Salary
-   Programming Language

A `Developer` object is created using the `Employee` parent class.

### Option 5: Show Details

The user can choose which object's details to display:

``` text
Choose details to show:
1. Person
2. Employee
3. Manager
4. Developer
```

The appropriate object's `display()` method is called.

### Option 6: Exit

The program exits the menu loop and displays:

``` text
Goodbye!
```

## Technologies Used

-   **Python 3.14.6**
-   **Object-Oriented Programming**
-   **Command Line / Terminal**
-   **Visual Studio Code**

## Requirements

To run this project, you need:

-   Python 3.14.6 installed on your computer
-   A code editor such as Visual Studio Code
-   A terminal or command prompt

## How to Run

1.  Clone or download this repository.
2.  Open the project folder in Visual Studio Code or another
    Python-supported editor.
3.  Open the terminal.
4.  Run the Python file:

``` bash
python Employee_Management_System.py
```

5.  Select an option from the menu.
6.  Enter the requested information.

## Example Output

``` text
Welcome to Employee Management System....

Inheritance Check:
Is Manager subclass of Employee? True
Is Developer subclass of Employee? True

Choose an operation:
1. Create an Person
2. Create a Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 1
Enter your name: John Doe
Enter your age: 30
Person created with name:John Doe and age:30

Choose an operation:
1. Create an Person
2. Create a Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 2
Enter your name: jane smith
Enter your age: 20
Enter Employee ID: E12
Enter Salary: 40000
Employee created with name:jane smith,age:20,id:E12, and salary:$40000.
```

## Project Purpose

The main purpose of this project is to understand and demonstrate Python
OOP concepts through a practical Employee Management System.

It provides a simple example of how classes can be organized using
inheritance and how different objects can have their own behavior while
sharing common functionality.


## Author

**\[Asti Sojitra\]**

## License

This project is created for learning and educational purposes.
