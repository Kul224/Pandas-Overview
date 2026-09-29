# Student Management System

## Overview

The **Student Management System** is a Python-based console application for managing student records stored in a CSV file.

The project demonstrates important Python programming concepts such as:

- Object-Oriented Programming (OOP)
- Abstract classes
- Inheritance
- Encapsulation
- File handling
- CSV file handling
- CRUD operations
- Exception handling
- Menu-driven programming

Student records are stored in `student_data.csv`, while the main application is implemented in `student_management.py`.

---

## Project Structure

```text
Student-Management/
│
├── student_management.py
├── student_data.csv
└── README.md
```

### Files

| File | Description |
|------|-------------|
| `student_management.py` | Main Python program |
| `student_data.csv` | Student data stored in CSV format |
| `README.md` | Project documentation |

---

## Features

The application provides the following options:

```text
1. Display Students
2. Add Student
3. Search Student
4. Average Marks
5. Update Student
6. Delete Student
7. Save Records
8. Exit
```

### 1. Display Students

Displays all student records currently loaded from the CSV file.

Example:

```text
===== STUDENT RECORDS =====
1. ['GP', 'F', '18', ...]
2. ['GP', 'F', '17', ...]
3. ['GP', 'M', '18', ...]
```

### 2. Add Student

Allows the user to add a new student record.

The program asks for:

- School
- Sex
- Age
- G1 marks
- G2 marks
- G3 marks

Example:

```text
===== ADD STUDENT =====
Enter School: GP
Enter Sex: M
Enter Age: 18
Enter G1 Marks: 12
Enter G2 Marks: 13
Enter G3 Marks: 14

Student Added Successfully.
```

The new record is initially stored in memory.

### 3. Search Student

Searches for students using the school field.

Example:

```text
===== SEARCH STUDENT =====
Enter School to Search: GP

Student Found:
['GP', 'F', '18', ...]
```

If no matching record is found:

```text
Student Not Found.
```

### 4. Average Marks

Calculates the average of the **G3 marks** from the available student records.

Example:

```text
===== AVERAGE MARKS =====
Average G3 Marks: 10.42
```

The displayed value depends on the data in `student_data.csv`.

### 5. Update Student

Allows the user to select a student record and update:

- School
- Sex
- Age
- G1 marks
- G2 marks
- G3 marks

Example:

```text
===== UPDATE STUDENT =====

Enter Record Number to Update: 2

Current Record:
['GP', 'F', '17', ...]

Enter New School: GP
Enter New Sex: F
Enter New Age: 18
Enter New G1 Marks: 10
Enter New G2 Marks: 12
Enter New G3 Marks: 13

Student Updated Successfully.
```

### 6. Delete Student

Allows the user to select and delete a student record.

The program asks for confirmation before deleting.

Example:

```text
===== DELETE STUDENT =====

Enter Record Number to Delete: 2

Selected Record:
['GP', 'F', '17', ...]

Are you sure you want to delete this record? (yes/no): yes

Student Deleted Successfully.
```

If the user enters `no`:

```text
Delete Operation Cancelled.
```

### 7. Save Records

Saves the current records to `student_data.csv`.

Example:

```text
===== SAVE RECORDS =====
Records Saved Successfully.
```

**Important:** Changes made using Add, Update, and Delete are initially made in memory. Use **Save Records** to write those changes to the CSV file.

### 8. Exit

Closes the Student Management System.

Example:

```text
Enter Choice: 8

Exiting Student Management System...
```

---

## OOP Concepts Used

### Abstract Class

The project contains an abstract `Person` class.

```python
class Person(ABC):

    @abstractmethod
    def display(self):
        pass
```

This demonstrates abstraction.

### Inheritance

The `Student` class inherits from `Person`.

```python
class Student(Person):
```

### Encapsulation

Student attributes are defined as private attributes:

```python
self.__roll_no
self.__name
self.__marks
```

Getter methods are used to access these attributes.

```python
def get_roll_no(self):
    return self.__roll_no
```

---

## CSV Data

The project uses a CSV file named:

```text
student_data.csv
```

The application reads the CSV file when the program starts.

The program uses these important columns:

| Column | Meaning |
|--------|---------|
| 0 | School |
| 1 | Sex |
| 2 | Age |
| 30 | G1 |
| 31 | G2 |
| 32 | G3 |

The remaining columns contain other student-related information from the dataset.

---

## Requirements

You need:

- Python 3.x
- `student_data.csv`

The project uses Python's built-in modules:

```python
from abc import ABC, abstractmethod
import csv
```

No external Python packages are required.

---

## How to Run

### Step 1: Open the Project Folder

Make sure these files are in the same folder:

```text
student_management.py
student_data.csv
```

### Step 2: Open a Terminal

Navigate to the project folder.

### Step 3: Run the Program

```bash
python student_management.py
```

On some systems:

```bash
python3 student_management.py
```

---

## Main Menu

When the program starts, the following menu is displayed:

```text
================================
     STUDENT MANAGEMENT SYSTEM
================================
1. Display Students
2. Add Student
3. Search Student
4. Average Marks
5. Update Student
6. Delete Student
7. Save Records
8. Exit
================================
Enter Choice:
```

Enter the number corresponding to the operation you want to perform.

---

## Data Saving

The program loads records from `student_data.csv` when it starts.

Changes made using:

- Add Student
- Update Student
- Delete Student

are made in memory first.

To permanently save the changes, select:

```text
7. Save Records
```

The updated records are then written to:

```text
student_data.csv
```

---

## Error Handling

The program handles several common errors.

### CSV File Not Found

```text
CSV file not found.
```

### Invalid Record Number

```text
Invalid Record Number.
```

### Invalid Number Input

```text
Please enter a valid number.
```

### Empty Records

```text
No student records available.
```

---

## Example Workflow

A typical workflow is:

```text
1. Display Students
2. Add Student
3. Search Student
4. Average Marks
5. Update Student
6. Delete Student
7. Save Records
8. Exit
```

For example, add a student:

```text
Enter Choice: 2
```

Update a record:

```text
Enter Choice: 5
```

Delete a record:

```text
Enter Choice: 6
```

Save the changes:

```text
Enter Choice: 7
```

Exit the program:

```text
Enter Choice: 8
```

---

## Project Objectives

The main objectives of this project are to:

1. Create a menu-driven Python application.
2. Manage student records using CSV files.
3. Demonstrate Object-Oriented Programming concepts.
4. Implement student record operations.
5. Practice file handling and exception handling.
6. Provide functionality to add, search, update, delete, display, and save student records.

---

## Technologies Used

- **Programming Language:** Python
- **Data Storage:** CSV
- **Programming Concepts:** OOP, Abstraction, Inheritance, Encapsulation, File Handling
- **Interface:** Command Line / Console

---

## Author

**Student Management System Project**

Developed as a Python programming project.