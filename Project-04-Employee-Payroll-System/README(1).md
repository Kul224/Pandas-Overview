# PROJECT 04 — EMPLOYEE PAYROLL SYSTEM

## Project Overview

The **Employee Payroll System** is a Python-based application designed to manage employee information and payroll records using a CSV dataset.

The project demonstrates Object-Oriented Programming (OOP), CSV file handling, salary calculation, payslip generation, employee searching, and saving payroll data.

## Project Features

The system provides the following features:

1. **Add Employees**
2. **Calculate Salary**
3. **Generate Payslips**
4. **Search Employees**
5. **Display Employees**
6. **Save Payroll Data**
7. **Exit**

## Dataset

The project uses the following Kaggle dataset:

```text
employee_salary_dataset.csv
```

### Dataset Headers

The CSV file contains these fields:

```text
EmployeeID
Name
Department
Experience_Years
Education_Level
Age
Gender
City
Monthly Salary
```

In the Python program, the salary column is handled as:

```text
Monthly_Salary
```

The CSV dataset and `employee_payroll.py` should be kept in the same folder.

## Technologies Used

- Python 3
- CSV file handling
- Object-Oriented Programming
- Abstract classes
- Inheritance
- Encapsulation
- Exception handling

## OOP Concepts Used

### 1. Abstraction

An abstract base class is used to define the common employee structure and required methods.

### 2. Encapsulation

Employee information is managed through class attributes and getter/setter methods where required.

### 3. Inheritance

The payroll employee class inherits common employee functionality from the base employee class.

### 4. Polymorphism

Employee-related methods can be implemented or overridden by the appropriate class.

## Project Structure

```text
PROJECT 04/
│
├── employee_payroll.py
├── employee_salary_dataset.csv
└── README.md
```

## How to Run

### Using Command Prompt / Terminal

Open the project folder and run:

```bash
python employee_payroll.py
```

If your system uses `python3`, run:

```bash
python3 employee_payroll.py
```

### Using Jupyter Notebook / IPython / Spyder

Run:

```python
%run employee_payroll.py
```

## Main Menu

When the program starts, the following menu is displayed:

```text
========================================
        EMPLOYEE PAYROLL SYSTEM
========================================
1. Add Employee
2. Calculate Salary
3. Generate Payslip
4. Search Employee
5. Display Employees
6. Save Payroll Data
7. Exit
========================================
Enter Choice:
```

## Feature Details

### 1. Add Employee

Allows the user to enter a new employee's details, including:

- Employee ID
- Name
- Department
- Experience
- Education Level
- Age
- Gender
- City
- Monthly Salary

The employee record is saved to the CSV file.

### 2. Calculate Salary

The program calculates the annual salary from the employee's monthly salary.

```text
Annual Salary = Monthly Salary × 12
```

Example:

```text
Monthly Salary : ₹50000.00
Annual Salary  : ₹600000.00
```

### 3. Generate Payslip

Generates a formatted payslip containing employee information and salary details.

Example:

```text
========================================
             EMPLOYEE PAYSLIP
========================================
Employee ID       : E1001
Name              : Kuldeep
Department        : IT
Experience        : 3 years
Education Level   : Bachelors
Age               : 25
Gender            : Male
City              : Chennai
----------------------------------------
Monthly Salary    : ₹50000.00
Annual Salary     : ₹600000.00
========================================
```

### 4. Search Employee

Employees can be searched using their:

- Employee ID
- Employee Name

The matching employee information is displayed.

### 5. Display Employees

Displays employee records stored in the payroll dataset.

### 6. Save Payroll Data

Saves the current employee/payroll records to:

```text
employee_salary_dataset.csv
```

The program displays:

```text
Records Saved Successfully.
```

### 7. Exit

Closes the Employee Payroll System.

The program displays:

```text
Thank you for using Employee Payroll System.
```

## Example Commands

### Run the program

```bash
python employee_payroll.py
```

### Run in Jupyter/IPython

```python
%run employee_payroll.py
```

## Example Test Sequence

### Add an employee

```text
Enter Choice: 1

Enter Employee ID: E1001
Enter Employee Name: Kuldeep
Enter Department: IT
Enter Experience (Years): 3
Enter Education Level: Bachelors
Enter Age: 25
Enter Gender: Male
Enter City: Chennai
Enter Monthly Salary: 50000
```

### Calculate salary

```text
Enter Choice: 2
Enter Employee ID: E1001
```

### Generate payslip

```text
Enter Choice: 3
Enter Employee ID: E1001
```

### Search employee

```text
Enter Choice: 4
Enter Employee ID or Name to Search: Rahul
```

### Display employees

```text
Enter Choice: 5
```

### Save payroll data

```text
Enter Choice: 6
```

### Exit

```text
Enter Choice: 7
```

## File Handling

The application uses Python's built-in `csv` module to read and write employee payroll records.

The main data file is:

```text
employee_salary_dataset.csv
```

The program saves changes while preserving the payroll records in CSV format.

## Error Handling

The program handles common situations such as:

- Missing CSV file
- Invalid employee ID
- Invalid numeric input
- Empty required fields
- Employee not found
- Duplicate employee ID
- CSV read/write errors

## Requirements

Python 3.x is recommended.

No external Python packages are required for the basic application because it uses Python standard-library functionality.

## Project Objective

The objective of this project is to create a simple Employee Payroll System while demonstrating:

- Python programming
- OOP concepts
- CSV data management
- Salary calculation
- Payslip generation
- Searching employee records
- File handling
- Exception handling

## Author

**PROJECT 04 — EMPLOYEE PAYROLL SYSTEM**

Developed as a Python project for practicing Object-Oriented Programming and file handling.