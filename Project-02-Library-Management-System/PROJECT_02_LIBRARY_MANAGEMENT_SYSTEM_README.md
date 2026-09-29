# PROJECT 02 - LIBRARY MANAGEMENT SYSTEM

## 1. Project Overview

The **Library Management System** is a Python console-based application developed to manage library book records.

The system allows the user to add books, search for books, issue books, return books, display available books, display all books, and save records using a CSV file.

The project demonstrates basic **Object-Oriented Programming**, **File Handling**, and **Exception Handling** concepts in Python.

---

## 2. Features

The Library Management System provides the following options:

1. Add Book
2. Search Book
3. Issue Book
4. Return Book
5. Display Available Books
6. Display All Books
7. Save Records
8. Exit

---

## 3. Technologies Used

- Python 3
- CSV File Handling
- Object-Oriented Programming
- Classes and Objects
- Methods
- Exception Handling

---

## 4. Project Structure

```text
PROJECT 02 - LIBRARY MANAGEMENT SYSTEM/
│
├── library_management.py
├── bookdata_lbms.csv
└── README.md
```

### Files Description

| File | Description |
|---|---|
| `library_management.py` | Main Python program |
| `bookdata_lbms.csv` | Stores the library book records |
| `README.md` | Project documentation |

---

## 5. CSV Dataset

The project uses the file:

```text
bookdata_lbms.csv
```

The original dataset contains the following columns:

```text
Book ID, Book Name, Author, Category
```

The program uses two additional fields to manage book issue and return information:

```text
Status, Borrower
```

Therefore, after records are saved, the CSV file can contain:

```text
Book ID, Book Name, Author, Category, Status, Borrower
```

### Status Values

A book can have one of these statuses:

```text
Available
Issued
```

When a book is issued, the borrower's name is stored in the `Borrower` field.

When a book is returned, its status becomes `Available` and the borrower field is cleared.

---

## 6. Main Class

The project contains the following main class:

```python
class LibraryManager:
```

The `LibraryManager` class contains the methods required to manage the library records.

Important methods include:

```text
check_file()
read_books()
save_books()
add_book()
search_book()
issue_book()
return_book()
display_available_books()
display_books()
save_records()
```

---

## 7. Menu Options

### Option 1 - Add Book

This option allows the user to add a new book.

The user enters:

- Book ID
- Book Name
- Author Name
- Category

Example:

```text
===== ADD BOOK =====
Enter Book ID: 101
Enter Book Name: Python Programming
Enter Author Name: John Smith
Enter Category: Programming

Records Saved Successfully.

Book Added Successfully.
```

The newly added book is given the status:

```text
Available
```

The program also checks whether the Book ID already exists.

---

### Option 2 - Search Book

This option searches for a book using:

- Book ID
- Book Name

Example:

```text
===== SEARCH BOOK =====
Enter Book ID or Book Name to Search: 101

Book Found
----------------------------------------
Book ID   : 101
Book Name : Python Programming
Author    : John Smith
Category  : Programming
Status    : Available
Borrower  : None
----------------------------------------
```

The search for book names is case-insensitive.

---

### Option 3 - Issue Book

This option allows the user to issue an available book.

The user enters:

- Book ID
- Borrower Name

Example:

```text
===== ISSUE BOOK =====
Enter Book ID to Issue: 101
Enter Borrower Name: Jadeja

Records Saved Successfully.

Book Issued Successfully.
```

After issuing:

```text
Status   : Issued
Borrower : Jadeja
```

The program does not allow an already issued book to be issued again.

---

### Option 4 - Return Book

This option allows the user to return an issued book.

Example:

```text
===== RETURN BOOK =====
Enter Book ID to Return: 101

Records Saved Successfully.

Book Returned Successfully.
```

After returning:

```text
Status   : Available
Borrower : 
```

---

### Option 5 - Display Available Books

This option displays only books whose status is:

```text
Available
```

Example:

```text
===== AVAILABLE BOOKS =====
--------------------------------------------------------------------------------
Book ID   : 101
Book Name : Python Programming
Author    : John Smith
Category  : Programming
--------------------------------------------------------------------------------
```

---

### Option 6 - Display All Books

This option displays all books stored in the CSV file.

Example:

```text
===== ALL BOOKS =====
--------------------------------------------------------------------------------
Book ID   : 101
Book Name : Python Programming
Author    : John Smith
Category  : Programming
Status    : Available
Borrower  : None
--------------------------------------------------------------------------------
```

---

### Option 7 - Save Records

This option saves the current book records to:

```text
bookdata_lbms.csv
```

Example:

```text
Records Saved Successfully.
```

The program also saves records automatically when a book is added, issued, or returned.

---

### Option 8 - Exit

This option closes the application.

Example:

```text
Thank you for using Library Management System.
```

---

## 8. Program Flow

The basic working flow of the application is:

```text
              START
                │
                ▼
        Read CSV Records
                │
                ▼
          Display Menu
                │
       ┌────────┼─────────┐
       │        │         │
       ▼        ▼         ▼
     Add      Search    Issue
       │        │         │
       └────────┼─────────┘
                │
                ▼
             Return
                │
                ▼
       Display Available
                │
                ▼
         Display All Books
                │
                ▼
          Save Records
                │
                ▼
              Exit
```

---

## 9. Object-Oriented Programming Concepts

### Class

The project uses the `LibraryManager` class to organize library operations.

### Objects

An object of the class is created using:

```python
library = LibraryManager()
```

### Methods

Different methods are used to perform individual operations such as adding, searching, issuing, returning, and displaying books.

### Encapsulation

The library management operations are grouped inside the `LibraryManager` class.

---

## 10. File Handling

The project uses Python's built-in `csv` module.

The CSV file is opened using:

```python
with open(...)
```

`csv.DictReader` is used to read records.

`csv.DictWriter` is used to write records.

This allows the application to store data permanently in:

```text
bookdata_lbms.csv
```

---

## 11. Exception Handling

The program uses `try` and `except` blocks to handle possible file-related errors.

Examples include:

- CSV file not found
- Error while reading the CSV file
- Error while saving records

This prevents the program from terminating unexpectedly because of common file errors.

---

## 12. Validation

The program performs several validations:

- Required fields cannot be empty when adding a book.
- Duplicate Book IDs are not allowed.
- A book must exist before it can be issued.
- A book must exist before it can be returned.
- An already issued book cannot be issued again.
- An already available book cannot be returned.
- Invalid menu choices display an error message.

---

## 13. Sample Menu

When the program starts, the following menu is displayed:

```text
========================================
       LIBRARY MANAGEMENT SYSTEM
========================================

1. Add Book
2. Search Book
3. Issue Book
4. Return Book
5. Display Available Books
6. Display All Books
7. Save Records
8. Exit

========================================
Enter Choice:
```

---

## 14. How to Run the Project

### Step 1

Make sure Python 3 is installed.

### Step 2

Keep the following files in the same folder:

```text
library_management.py
bookdata_lbms.csv
```

### Step 3

Open `library_management.py` in a Python editor such as:

- Spyder
- IDLE
- VS Code
- PyCharm

### Step 4

Run the Python file.

### Step 5

Enter a menu choice from `1` to `8`.

---

## 15. Important Note

The program expects:

```text
bookdata_lbms.csv
```

to be in the same folder as:

```text
library_management.py
```

If the CSV initially contains only:

```text
Book ID, Book Name, Author, Category
```

the program treats the books as `Available` when reading them.

When the records are saved, the program writes the additional:

```text
Status
Borrower
```

columns required for library management.

---

## 16. Expected Outcome

After running the program, the user can:

- Add new books
- Search for books
- Issue available books
- Return issued books
- View available books
- View all books
- Save library records
- Exit the system

The records are stored in the CSV file so that they can be used again when the program is run.

---

## 17. Conclusion

The **Library Management System** is a simple Python console application designed to manage book records using a CSV file.

The project demonstrates practical use of:

- Python programming
- Classes and Objects
- Encapsulation
- Methods
- CSV File Handling
- Exception Handling
- User Input and Menu-Based Programming

It provides a basic and easy-to-use system for managing books and their availability.