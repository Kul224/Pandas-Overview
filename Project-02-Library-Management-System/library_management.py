import csv
import os

class LibraryManager:

    FILE_NAME = "bookdata_lbms.csv"

    HEADERS = [
        "Book ID",
        "Book Name",
        "Author",
        "Category",
        "Status",
        "Borrower"
    ]

    def __init__(self):
        self.check_file()

    # =========================
    # Check CSV File
    # =========================
    def check_file(self):

        if not os.path.exists(self.FILE_NAME):

            print("\nError: bookdata_lbms.csv not found.")
            print("Please keep the CSV file in the same folder")
            print("as library_management.py.")

    # =========================
    # Read Books
    # =========================
    def read_books(self):

        books = []

        try:

            with open(
                self.FILE_NAME,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    book = {
                        "Book ID": row.get("Book ID", "").strip(),
                        "Book Name": row.get("Book Name", "").strip(),
                        "Author": row.get("Author", "").strip(),
                        "Category": row.get("Category", "").strip(),
                        "Status": row.get(
                            "Status",
                            "Available"
                        ).strip(),
                        "Borrower": row.get(
                            "Borrower",
                            ""
                        ).strip()
                    }

                    if book["Status"] == "":
                        book["Status"] = "Available"

                    books.append(book)

        except FileNotFoundError:

            print("\nbookdata_lbms.csv not found.")

        except Exception as e:

            print("\nError reading CSV:", e)

        return books

    # =========================
    # Save Books
    # =========================
    def save_books(self, books):

        try:

            with open(
                self.FILE_NAME,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=self.HEADERS
                )

                writer.writeheader()
                writer.writerows(books)

            print("\nRecords Saved Successfully.")

        except Exception as e:

            print("\nError saving records:", e)

    # =========================
    # Add Book
    # =========================
    def add_book(self):

        print("\n===== ADD BOOK =====")

        book_id = input("Enter Book ID: ").strip()
        book_name = input("Enter Book Name: ").strip()
        author = input("Enter Author Name: ").strip()
        category = input("Enter Category: ").strip()

        if (
            book_id == ""
            or book_name == ""
            or author == ""
            or category == ""
        ):

            print("\nAll fields are required.")
            return

        books = self.read_books()

        for book in books:

            if book["Book ID"] == book_id:

                print("\nBook ID already exists.")
                return

        new_book = {
            "Book ID": book_id,
            "Book Name": book_name,
            "Author": author,
            "Category": category,
            "Status": "Available",
            "Borrower": ""
        }

        books.append(new_book)

        self.save_books(books)

        print("\nBook Added Successfully.")

    # =========================
    # Search Book
    # =========================
    def search_book(self):

        print("\n===== SEARCH BOOK =====")

        search = input(
            "Enter Book ID or Book Name to Search: "
        ).strip().lower()

        if search == "":
            print("\nPlease enter a search value.")
            return

        books = self.read_books()

        found = False

        for book in books:

            book_id = book["Book ID"].lower()
            book_name = book["Book Name"].lower()

            if (
                search == book_id
                or search in book_name
            ):

                print("\nBook Found")
                print("-" * 40)

                print("Book ID   :", book["Book ID"])
                print("Book Name :", book["Book Name"])
                print("Author    :", book["Author"])
                print("Category  :", book["Category"])
                print("Status    :", book["Status"])

                borrower = book["Borrower"]

                if borrower == "":
                    borrower = "None"

                print("Borrower  :", borrower)

                print("-" * 40)

                found = True

        if not found:

            print("\nBook Not Found.")

    # =========================
    # Issue Book
    # =========================
    def issue_book(self):

        print("\n===== ISSUE BOOK =====")

        book_id = input(
            "Enter Book ID to Issue: "
        ).strip()

        borrower = input(
            "Enter Borrower Name: "
        ).strip()

        if book_id == "" or borrower == "":
            print(
                "\nBook ID and Borrower Name are required."
            )
            return

        books = self.read_books()

        found = False

        for book in books:

            if book["Book ID"] == book_id:

                found = True

                if book["Status"] == "Issued":

                    print("\nBook is already issued.")
                    return

                book["Status"] = "Issued"
                book["Borrower"] = borrower

                self.save_books(books)

                print("\nBook Issued Successfully.")

                return

        if not found:

            print("\nBook Not Found.")

    # =========================
    # Return Book
    # =========================
    def return_book(self):

        print("\n===== RETURN BOOK =====")

        book_id = input(
            "Enter Book ID to Return: "
        ).strip()

        if book_id == "":
            print("\nPlease enter a Book ID.")
            return

        books = self.read_books()

        for book in books:

            if book["Book ID"] == book_id:

                if book["Status"] == "Available":

                    print("\nBook is already available.")
                    return

                book["Status"] = "Available"
                book["Borrower"] = ""

                self.save_books(books)

                print("\nBook Returned Successfully.")

                return

        print("\nBook Not Found.")

    # =========================
    # Display Available Books
    # =========================
    def display_available_books(self):

        print("\n===== AVAILABLE BOOKS =====")
        print("-" * 80)

        books = self.read_books()

        found = False

        for book in books:

            if book["Status"] == "Available":

                print("Book ID   :", book["Book ID"])
                print("Book Name :", book["Book Name"])
                print("Author    :", book["Author"])
                print("Category  :", book["Category"])
                print("-" * 80)

                found = True

        if not found:

            print("No Available Books.")

    # =========================
    # Display All Books
    # =========================
    def display_books(self):

        print("\n===== ALL BOOKS =====")
        print("-" * 80)

        books = self.read_books()

        if len(books) == 0:

            print("No Books Found.")
            return

        for book in books:

            print("Book ID   :", book["Book ID"])
            print("Book Name :", book["Book Name"])
            print("Author    :", book["Author"])
            print("Category  :", book["Category"])
            print("Status    :", book["Status"])

            borrower = book["Borrower"]

            if borrower == "":
                borrower = "None"

            print("Borrower  :", borrower)

            print("-" * 80)

    # =========================
    # Save Records
    # =========================
    def save_records(self):

        books = self.read_books()

        self.save_books(books)

# ========================================
# Create Library Manager
# ========================================

library = LibraryManager()

# ========================================
# Main Menu
# ========================================

while True:

    print("\n========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Display All Books")
    print("7. Save Records")
    print("8. Exit")

    print("========================================")

    choice = input("Enter Choice: ").strip()

    if choice == "1":

        library.add_book()

    elif choice == "2":

        library.search_book()

    elif choice == "3":

        library.issue_book()

    elif choice == "4":

        library.return_book()

    elif choice == "5":

        library.display_available_books()

    elif choice == "6":

        library.display_books()

    elif choice == "7":

        library.save_records()

    elif choice == "8":

        print(
            "\nThank you for using "
            "Library Management System."
        )

        break

    else:

        print("\nInvalid Choice. Please try again.")