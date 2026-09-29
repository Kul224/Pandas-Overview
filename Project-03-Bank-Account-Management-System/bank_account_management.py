import csv
import os
from abc import ABC, abstractmethod
from datetime import datetime

class Person(ABC):
    """Abstract base class for a bank customer."""

    def __init__(self, name):
        self.__name = name.strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.strip()
        if value:
            self.__name = value

    @abstractmethod
    def display_details(self):
        """Display customer details."""
        pass

class BankAccount(Person):
    """Base bank account class."""

    def __init__(
        self,
        account_number,
        name,
        account_type="Savings",
        balance=0.0,
        country=""
    ):
        super().__init__(name)

        self.__account_number = str(account_number).strip()
        self.__account_type = account_type.strip()
        self.__balance = float(balance)
        self.__country = country.strip()

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_type(self):
        return self.__account_type

    @property
    def balance(self):
        return self.__balance

    @property
    def country(self):
        return self.__country

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount

    def display_details(self):
        print("\n----------------------------------------")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.name)
        print("Account Type   :", self.account_type)
        print("Country        :", self.country or "Not Available")
        print("Balance        : {:.2f}".format(self.balance))
        print("----------------------------------------")


class SavingsAccount(BankAccount):
    """Derived class representing a savings account."""

    def __init__(
        self,
        account_number,
        name,
        balance=0.0,
        country=""
    ):
        super().__init__(
            account_number,
            name,
            "Savings",
            balance,
            country
        )

    def display_details(self):
        print("\n===== SAVINGS ACCOUNT =====")
        super().display_details()


class CurrentAccount(BankAccount):
    """Derived class representing a current account."""

    def __init__(
        self,
        account_number,
        name,
        balance=0.0,
        country=""
    ):
        super().__init__(
            account_number,
            name,
            "Current",
            balance,
            country
        )

    def display_details(self):
        print("\n===== CURRENT ACCOUNT =====")
        super().display_details()

class BankManager:
    """Manages accounts and transaction records."""

    SOURCE_FILE = "Bank Customer Churn Prediction.csv"
    ACCOUNT_FILE = "bank_accounts.csv"
    TRANSACTION_FILE = "transactions.csv"

    ACCOUNT_HEADERS = [
        "Account Number",
        "Account Holder",
        "Account Type",
        "Country",
        "Balance"
    ]

    TRANSACTION_HEADERS = [
        "Transaction ID",
        "Account Number",
        "Date",
        "Transaction Type",
        "Amount",
        "Balance"
    ]

    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    # ==========================================
    # Create Account Object
    # ==========================================
    def create_account_object(
        self,
        account_number,
        name,
        account_type,
        balance,
        country=""
    ):
        if account_type.lower() == "current":
            return CurrentAccount(
                account_number,
                name,
                balance,
                country
            )

        return SavingsAccount(
            account_number,
            name,
            balance,
            country
        )

    # ==========================================
    # Load Accounts
    # ==========================================
    def load_accounts(self):
        """
        Load bank_accounts.csv if it exists.

        On the first run, convert the supplied Kaggle
        customer dataset into bank_accounts.csv.
        """

        if os.path.exists(self.ACCOUNT_FILE):
            self.load_bank_accounts()
            return

        if os.path.exists(self.SOURCE_FILE):
            self.import_kaggle_dataset()
            return

        print("\nError: No account data file was found.")
        print("Please keep the Kaggle CSV in the same folder.")

    # ==========================================
    # Import Kaggle Dataset
    # ==========================================
    def import_kaggle_dataset(self):
        """
        Convert the Kaggle dataset into a bank account file.

        Dataset columns used:
        customer_id, country, balance
        """

        try:
            with open(
                self.SOURCE_FILE,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                required = {
                    "customer_id",
                    "country",
                    "balance"
                }

                if not required.issubset(set(reader.fieldnames or [])):
                    print("\nError: Required dataset columns are missing.")
                    return

                for row in reader:
                    account_number = row["customer_id"].strip()

                    if not account_number:
                        continue

                    balance_text = row.get("balance", "0").strip()

                    try:
                        balance = float(balance_text or 0)
                    except ValueError:
                        balance = 0.0

                    country = row.get("country", "").strip()

                    # The Kaggle dataset does not contain a customer name.
                    # Therefore a simple display name is generated.
                    name = "Customer " + account_number

                    account = self.create_account_object(
                        account_number,
                        name,
                        "Savings",
                        balance,
                        country
                    )

                    self.accounts[account_number] = account

            self.save_accounts()

            print("\nKaggle customer dataset imported successfully.")
            print(
                "Initial accounts loaded:",
                len(self.accounts)
            )

        except FileNotFoundError:
            print("\nKaggle dataset not found.")

        except Exception as error:
            print("\nError importing dataset:", error)

    # ==========================================
    # Load Saved Bank Accounts
    # ==========================================
    def load_bank_accounts(self):
        try:
            with open(
                self.ACCOUNT_FILE,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:
                    account_number = row.get(
                        "Account Number",
                        ""
                    ).strip()

                    if not account_number:
                        continue

                    try:
                        balance = float(
                            row.get("Balance", "0") or 0
                        )
                    except ValueError:
                        balance = 0.0

                    account = self.create_account_object(
                        account_number,
                        row.get(
                            "Account Holder",
                            "Unknown Customer"
                        ),
                        row.get(
                            "Account Type",
                            "Savings"
                        ),
                        balance,
                        row.get("Country", "")
                    )

                    self.accounts[account_number] = account

        except FileNotFoundError:
            print("\nAccount file not found.")

        except Exception as error:
            print("\nError loading accounts:", error)

    # ==========================================
    # Save Accounts
    # ==========================================
    def save_accounts(self):
        try:
            with open(
                self.ACCOUNT_FILE,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=self.ACCOUNT_HEADERS
                )

                writer.writeheader()

                for account in self.accounts.values():
                    writer.writerow({
                        "Account Number": account.account_number,
                        "Account Holder": account.name,
                        "Account Type": account.account_type,
                        "Country": account.country,
                        "Balance": "{:.2f}".format(
                            account.balance
                        )
                    })

        except Exception as error:
            print("\nError saving accounts:", error)

    # ==========================================
    # Create New Account
    # ==========================================
    def create_account(self):
        print("\n===== CREATE ACCOUNT =====")

        account_number = input(
            "Enter Account Number: "
        ).strip()

        if not account_number:
            print("\nAccount Number is required.")
            return

        if account_number in self.accounts:
            print("\nAccount Number already exists.")
            return

        name = input(
            "Enter Account Holder Name: "
        ).strip()

        if not name:
            print("\nAccount Holder Name is required.")
            return

        account_type = input(
            "Enter Account Type (Savings/Current): "
        ).strip().lower()

        if account_type not in ["savings", "current"]:
            print("\nInvalid account type.")
            print("Please enter Savings or Current.")
            return

        balance_text = input(
            "Enter Initial Deposit: "
        ).strip()

        try:
            initial_balance = float(balance_text)

            if initial_balance < 0:
                print("\nInitial deposit cannot be negative.")
                return

        except ValueError:
            print("\nPlease enter a valid amount.")
            return

        country = input(
            "Enter Country (optional): "
        ).strip()

        if account_type == "current":
            account = CurrentAccount(
                account_number,
                name,
                initial_balance,
                country
            )
        else:
            account = SavingsAccount(
                account_number,
                name,
                initial_balance,
                country
            )

        self.accounts[account_number] = account

        if initial_balance > 0:
            self.record_transaction(
                account,
                "Initial Deposit",
                initial_balance
            )

        self.save_accounts()

        print("\nAccount Created Successfully.")
        account.display_details()

    # ==========================================
    # Find Account
    # ==========================================
    def find_account(self):
        account_number = input(
            "Enter Account Number: "
        ).strip()

        if account_number not in self.accounts:
            print("\nAccount Not Found.")
            return None

        return self.accounts[account_number]

    # ==========================================
    # Deposit Money
    # ==========================================
    def deposit_money(self):
        print("\n===== DEPOSIT MONEY =====")

        account = self.find_account()

        if account is None:
            return

        amount_text = input(
            "Enter Deposit Amount: "
        ).strip()

        try:
            amount = float(amount_text)
            account.deposit(amount)

            self.record_transaction(
                account,
                "Deposit",
                amount
            )

            self.save_accounts()

            print("\nDeposit Successful.")
            print(
                "Current Balance: {:.2f}".format(
                    account.balance
                )
            )

        except ValueError as error:
            print("\nError:", error)

    # ==========================================
    # Withdraw Money
    # ==========================================
    def withdraw_money(self):
        print("\n===== WITHDRAW MONEY =====")

        account = self.find_account()

        if account is None:
            return

        amount_text = input(
            "Enter Withdrawal Amount: "
        ).strip()

        try:
            amount = float(amount_text)
            account.withdraw(amount)

            self.record_transaction(
                account,
                "Withdrawal",
                amount
            )

            self.save_accounts()

            print("\nWithdrawal Successful.")
            print(
                "Current Balance: {:.2f}".format(
                    account.balance
                )
            )

        except ValueError as error:
            print("\nError:", error)

    # ==========================================
    # Check Balance
    # ==========================================
    def check_balance(self):
        print("\n===== CHECK BALANCE =====")

        account = self.find_account()

        if account is None:
            return

        account.display_details()

    # ==========================================
    # Generate Transaction ID
    # ==========================================
    def generate_transaction_id(self):
        count = 0

        if os.path.exists(self.TRANSACTION_FILE):
            try:
                with open(
                    self.TRANSACTION_FILE,
                    "r",
                    newline="",
                    encoding="utf-8-sig"
                ) as file:

                    reader = csv.DictReader(file)

                    for _ in reader:
                        count += 1

            except Exception:
                count = 0

        return "T{:05d}".format(count + 1)

    # ==========================================
    # Record Transaction
    # ==========================================
    def record_transaction(
        self,
        account,
        transaction_type,
        amount
    ):
        try:
            file_exists = os.path.exists(
                self.TRANSACTION_FILE
            )

            with open(
                self.TRANSACTION_FILE,
                "a",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=self.TRANSACTION_HEADERS
                )

                if not file_exists or os.path.getsize(
                    self.TRANSACTION_FILE
                ) == 0:
                    writer.writeheader()

                writer.writerow({
                    "Transaction ID":
                        self.generate_transaction_id(),
                    "Account Number":
                        account.account_number,
                    "Date":
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                    "Transaction Type":
                        transaction_type,
                    "Amount":
                        "{:.2f}".format(amount),
                    "Balance":
                        "{:.2f}".format(account.balance)
                })

        except Exception as error:
            print("\nError recording transaction:", error)

    # ==========================================
    # Transaction History
    # ==========================================
    def transaction_history(self):
        print("\n===== TRANSACTION HISTORY =====")

        account_number = input(
            "Enter Account Number: "
        ).strip()

        if account_number not in self.accounts:
            print("\nAccount Not Found.")
            return

        if not os.path.exists(self.TRANSACTION_FILE):
            print("\nNo transaction history found.")
            return

        found = False

        try:
            with open(
                self.TRANSACTION_FILE,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    if row.get(
                        "Account Number",
                        ""
                    ).strip() == account_number:

                        found = True

                        print("\n----------------------------------------")
                        print(
                            "Transaction ID :",
                            row.get("Transaction ID", "")
                        )
                        print(
                            "Date           :",
                            row.get("Date", "")
                        )
                        print(
                            "Type           :",
                            row.get("Transaction Type", "")
                        )
                        print(
                            "Amount         :",
                            row.get("Amount", "")
                        )
                        print(
                            "Balance        :",
                            row.get("Balance", "")
                        )
                        print("----------------------------------------")

        except Exception as error:
            print("\nError reading transactions:", error)

            return

        if not found:
            print("\nNo transactions found for this account.")

    # ==========================================
    # Save Data
    # ==========================================
    def save_data(self):
        self.save_accounts()
        print("\nAccount Data Saved Successfully.")

        if os.path.exists(self.TRANSACTION_FILE):
            print("Transaction Data Saved Successfully.")
        else:
            print(
                "No transaction file exists yet."
            )

    # ==========================================
    # Display All Accounts
    # ==========================================
    def display_accounts(self):
        print("\n===== ALL BANK ACCOUNTS =====")

        if not self.accounts:
            print("\nNo accounts found.")
            return

        for account in self.accounts.values():
            account.display_details()

# ==============================================
# Main Program
# ==============================================

def main():
    bank = BankManager()

    while True:

        print("\n========================================")
        print("    BANK ACCOUNT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Display All Accounts")
        print("7. Save Data")
        print("8. Exit")
        print("========================================")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            bank.deposit_money()

        elif choice == "3":
            bank.withdraw_money()

        elif choice == "4":
            bank.check_balance()

        elif choice == "5":
            bank.transaction_history()

        elif choice == "6":
            bank.display_accounts()

        elif choice == "7":
            bank.save_data()

        elif choice == "8":
            bank.save_data()
            print(
                "\nThank you for using "
                "Bank Account Management System."
            )
            break

        else:
            print("\nInvalid Choice. Please enter 1 to 8.")

if __name__ == "__main__":
    main()