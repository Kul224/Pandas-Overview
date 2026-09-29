# PROJECT 03 — BANK ACCOUNT MANAGEMENT SYSTEM

## 1. Project Overview

The **Bank Account Management System** is a Python console-based application designed to manage bank accounts and basic banking transactions.

The system allows users to create accounts, deposit money, withdraw money, check account balances, maintain transaction history, display accounts, and save data using CSV files.

The project uses Object-Oriented Programming concepts along with file handling and exception handling.

---

## 2. Suggested Features Implemented

The project implements the required banking features:

- Create accounts
- Deposit money
- Withdraw money
- Check balance
- Maintain transaction history
- Save data

Additional functionality:

- Display all bank accounts
- Input validation
- Duplicate account checking
- Insufficient balance checking
- Automatic transaction recording
- CSV-based permanent storage

---

## 3. Technologies Used

- Python 3
- CSV file handling
- Object-Oriented Programming
- Abstract Base Classes (`abc`)
- Encapsulation
- Inheritance
- Exception Handling
- Date and time handling

---

## 4. Project Structure

```text
PROJECT 03 - BANK ACCOUNT MANAGEMENT SYSTEM/
│
├── bank_account_management.py
├── Bank Customer Churn Prediction.csv
├── bank_accounts.csv
├── transactions.csv
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `bank_account_management.py` | Main Python application |
| `Bank Customer Churn Prediction.csv` | Original Kaggle customer dataset |
| `bank_accounts.csv` | Stores account information used by the application |
| `transactions.csv` | Stores transaction history |
| `README.md` | Project documentation |

---

## 5. Dataset Used

The project uses the Kaggle dataset:

```text
Bank Customer Churn Prediction.csv
```

The dataset contains the following columns:

```text
customer_id
credit_score
country
gender
age
tenure
balance
products_number
credit_card
active_member
estimated_salary
churn
```

The program uses relevant customer information from the dataset to create the initial bank account records.

### Dataset Field Mapping

The application uses:

```text
customer_id → Account Number
country     → Country
balance     → Initial Balance
```

Since the source dataset does not contain an account-holder name or account type, the application generates an account holder name such as:

```text
Customer 15634602
```

and initially uses:

```text
Savings
```

as the account type.

The remaining dataset fields are retained in the original Kaggle CSV but are not required for the core banking operations.

---

## 6. Generated Data Files

### bank_accounts.csv

The application creates a separate account file with:

```text
Account Number,Account Holder,Account Type,Country,Balance
```

Example:

```text
Account Number,Account Holder,Account Type,Country,Balance
15634602,Customer 15634602,Savings,France,0.00
15647311,Customer 15647311,Savings,Spain,83807.86
90000001,Rahul Kumar,Savings,India,5500.00
```

### transactions.csv

The application maintains transaction history using:

```text
Transaction ID,Account Number,Date,Transaction Type,Amount,Balance
```

Example:

```text
Transaction ID,Account Number,Date,Transaction Type,Amount,Balance
T00001,90000001,2026-09-29 18:30:00,Initial Deposit,5000.00,5000.00
T00002,90000001,2026-09-29 18:31:00,Deposit,2000.00,7000.00
T00003,90000001,2026-09-29 18:32:00,Withdrawal,1500.00,5500.00
```

The actual date and time will depend on when the transaction is performed.

---

## 7. Object-Oriented Programming Concepts

The project is designed to demonstrate the required OOP concepts.

### 7.1 Classes and Objects

The project contains multiple classes:

```python
Person
BankAccount
SavingsAccount
CurrentAccount
BankManager
```

An instance of `BankManager` controls the application:

```python
bank = BankManager()
```

---

### 7.2 Abstraction

The project uses the `ABC` module.

The abstract base class is:

```python
class Person(ABC):
```

It contains the abstract method:

```python
@abstractmethod
def display_details(self):
    pass
```

This provides an abstraction for displaying customer/account details.

---

### 7.3 Encapsulation

Private attributes are used inside the classes.

For example:

```python
self.__balance
self.__account_number
self.__account_type
```

Properties are used to access these values safely.

Example:

```python
@property
def balance(self):
    return self.__balance
```

---

### 7.4 Inheritance

The project uses inheritance.

The relationship is:

```text
Person
  │
  ▼
BankAccount
  │
  ├── SavingsAccount
  │
  └── CurrentAccount
```

`SavingsAccount` and `CurrentAccount` inherit from `BankAccount`.

---

### 7.5 File Handling

The program uses Python's `csv` module to read and write data.

The following files are used:

```text
Bank Customer Churn Prediction.csv
bank_accounts.csv
transactions.csv
```

---

### 7.6 Exception Handling

The program handles common errors such as:

- Invalid numerical input
- Negative deposit amounts
- Negative withdrawal amounts
- Withdrawal greater than available balance
- Missing account numbers
- Missing CSV files
- CSV reading errors
- CSV writing errors

---

## 8. Main Menu

When the program starts, the following menu is displayed:

```text
========================================
    BANK ACCOUNT MANAGEMENT SYSTEM
========================================
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transaction History
6. Display All Accounts
7. Save Data
8. Exit
========================================
Enter Choice:
```

---

# 9. Features and Operations

## 9.1 Create Account

Option:

```text
1. Create Account
```

The user enters:

- Account Number
- Account Holder Name
- Account Type
- Initial Deposit
- Country

Example:

```text
===== CREATE ACCOUNT =====
Enter Account Number: 90000001
Enter Account Holder Name: Karnam Kuldeep
Enter Account Type (Savings/Current): Savings
Enter Initial Deposit: 5000
Enter Country (optional): India

Account Created Successfully.
```

The program checks whether the account number already exists.

---

## 9.2 Deposit Money

Option:

```text
2. Deposit Money
```

The user enters the account number and deposit amount.

Example:

```text
===== DEPOSIT MONEY =====
Enter Account Number: 90000001
Enter Deposit Amount: 2000

Deposit Successful.
Current Balance: 7000.00
```

The deposit is added to the account balance and recorded in the transaction history.

---

## 9.3 Withdraw Money

Option:

```text
3. Withdraw Money
```

The user enters the account number and withdrawal amount.

Example:

```text
===== WITHDRAW MONEY =====
Enter Account Number: 90000001
Enter Withdrawal Amount: 1500

Withdrawal Successful.
Current Balance: 5500.00
```

The program checks that:

- The amount is greater than zero.
- The account has sufficient balance.

---

## 9.4 Check Balance

Option:

```text
4. Check Balance
```

Example:

```text
===== CHECK BALANCE =====
Enter Account Number: 90000001

===== SAVINGS ACCOUNT =====

----------------------------------------
Account Number : 90000001
Account Holder : Karnam Kuldeep
Account Type   : Savings
Country        : India
Balance        : 5500.00
----------------------------------------
```

---

## 9.5 Transaction History

Option:

```text
5. Transaction History
```

The user enters an account number.

Example:

```text
===== TRANSACTION HISTORY =====
Enter Account Number: 90000001

----------------------------------------
Transaction ID : T00002
Date           : 2026-09-29 18:31:00
Type           : Deposit
Amount         : 2000.00
Balance        : 7000.00
----------------------------------------

----------------------------------------
Transaction ID : T00003
Date           : 2026-09-29 18:32:00
Type           : Withdrawal
Amount         : 1500.00
Balance        : 5500.00
----------------------------------------
```

The transaction history is stored in:

```text
transactions.csv
```

---

## 9.6 Display All Accounts

Option:

```text
6. Display All Accounts
```

This displays the account records currently loaded by the program.

Example:

```text
===== ALL BANK ACCOUNTS =====

===== SAVINGS ACCOUNT =====

----------------------------------------
Account Number : 90000001
Account Holder : Karnam Kuldeep
Account Type   : Savings
Country        : India
Balance        : 5500.00
----------------------------------------
```

The original Kaggle dataset contains many records, so this option can produce a large amount of console output.

---

## 9.7 Save Data

Option:

```text
7. Save Data
```

Example:

```text
Account Data Saved Successfully.
Transaction Data Saved Successfully.
```

The program saves account information to:

```text
bank_accounts.csv
```

and transaction information to:

```text
transactions.csv
```

---

## 9.8 Exit

Option:

```text
8. Exit
```

Example:

```text
Account Data Saved Successfully.
Transaction Data Saved Successfully.

Thank you for using Bank Account Management System.
```

The program saves account data before exiting.

---

# 10. Program Flow

```text
             START
               │
               ▼
     Load Customer Dataset
               │
               ▼
       Load Bank Accounts
               │
               ▼
         Display Menu
               │
     ┌─────────┼─────────┐
     ▼         ▼         ▼
 Create      Deposit   Withdraw
 Account      Money      Money
     │         │         │
     └─────────┼─────────┘
               │
               ▼
        Check Balance
               │
               ▼
      Transaction History
               │
               ▼
      Display All Accounts
               │
               ▼
          Save Data
               │
               ▼
             Exit
```

---

# 11. How to Run

## Step 1 — Open the Project Folder

Keep the Python program and Kaggle dataset in the same folder.

```text
PROJECT 03 - BANK ACCOUNT MANAGEMENT SYSTEM/
```

## Step 2 — Check the Files

Make sure this file exists:

```text
bank_account_management.py
```

and the Kaggle dataset is:

```text
Bank Customer Churn Prediction.csv
```

## Step 3 — Run the Program

### In Jupyter Notebook

Use:

```python
%run bank_account_management.py
```

### In a terminal

Use:

```text
python bank_account_management.py
```

or, depending on your Python installation:

```text
python3 bank_account_management.py
```

---

# 12. Sample Demonstration

A simple demonstration can use a new account:

```text
Account Number: 90000001
Account Holder: Karnam Kuldeep
Account Type: Savings
Initial Deposit: 5000
Country: India
```

Then perform:

```text
Deposit: 2000
Withdrawal: 1500
```

The final balance will be:

```text
5000 + 2000 - 1500 = 5500
```

The transaction history will contain the corresponding initial deposit, deposit, and withdrawal records.

---

# 13. Error Handling Examples

### Duplicate Account

```text
Account Number already exists.
```

### Account Not Found

```text
Account Not Found.
```

### Invalid Amount

```text
Please enter a valid amount.
```

### Negative Deposit

```text
Error: Deposit amount must be greater than zero.
```

### Insufficient Balance

```text
Error: Insufficient balance.
```

### Invalid Account Type

```text
Invalid account type.
Please enter Savings or Current.
```

---

# 14. Data Flow

```text
Bank Customer Churn Prediction.csv
              │
              ▼
        Import Customer Data
              │
              ▼
        BankAccount Objects
              │
              ▼
        BankManager Class
              │
       ┌──────┼─────────┐
       ▼      ▼         ▼
    Deposit Withdraw  Balance
       │      │         │
       └──────┼─────────┘
              ▼
      Transaction History
              │
              ▼
       transactions.csv

Bank Account Data
       │
       ▼
bank_accounts.csv
```

---

# 15. Data Persistence

The application separates the original Kaggle dataset from the application's working data.

The original file:

```text
Bank Customer Churn Prediction.csv
```

is used as the initial customer/account source.

The application maintains:

```text
bank_accounts.csv
```

for current account balances.

Transaction records are maintained separately in:

```text
transactions.csv
```

This allows deposits and withdrawals to be recorded without modifying the original Kaggle dataset.

---

# 16. Testing

The following operations should be tested before submission:

```text
✓ Create a new account
✓ Try creating a duplicate account
✓ Deposit money
✓ Try depositing an invalid amount
✓ Withdraw money
✓ Try withdrawing more than the balance
✓ Check balance
✓ View transaction history
✓ Display accounts
✓ Save data
✓ Exit the program
```

---

# 17. Expected Outcome

After successful execution, the system should allow the user to:

- Create and manage bank accounts
- Maintain account balances
- Deposit money
- Withdraw money
- Check account balances
- View transaction history
- Store account data permanently
- Store transaction data permanently
- Handle invalid input and common file errors

---

# 18. Conclusion

The **Bank Account Management System** is a Python console application that demonstrates how Object-Oriented Programming and CSV file handling can be used to create a basic banking application.

The project combines:

- Classes and Objects
- Encapsulation
- Inheritance
- Abstraction
- File Handling
- Exception Handling
- User Input
- Menu-Driven Programming
- Transaction Management

The application provides a practical demonstration of how to manage bank accounts and maintain transaction records using Python.