from abc import ABC, abstractmethod
import csv

# =========================
# Person Abstract Class
# =========================
class Person(ABC):

    @abstractmethod
    def display(self):
        pass

# =========================
# Student Class
# =========================
class Student(Person):

    def __init__(self, roll_no, name, marks):
        self.__roll_no = roll_no
        self.__name = name
        self.__marks = marks

    # Getter methods
    def get_roll_no(self):
        return self.__roll_no

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    # Display student
    def display(self):
        print("Roll No :", self.__roll_no)
        print("Name    :", self.__name)
        print("Marks   :", self.__marks)

# =========================
# Student Manager Class
# =========================
class StudentManager:

    def __init__(self, filename):
        self.filename = filename
        self.students = []

        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.reader(file)
                self.students = list(reader)

        except FileNotFoundError:
            print("CSV file not found.")
            self.students = []

    # =========================
    # 1. Display Students
    # =========================
    def display_students(self):

        if not self.students:
            print("\nNo student records available.")
            return

        print("\n===== STUDENT RECORDS =====")

        for i, row in enumerate(self.students):
            print(f"{i + 1}. {row}")

    # =========================
    # 2. Add Student
    # =========================
    def add_student(self):

        print("\n===== ADD STUDENT =====")

        school = input("Enter School: ")
        sex = input("Enter Sex: ")
        age = input("Enter Age: ")
        g1 = input("Enter G1 Marks: ")
        g2 = input("Enter G2 Marks: ")
        g3 = input("Enter G3 Marks: ")

        # Create a record with 33 columns
        new_student = [""] * 33

        new_student[0] = school
        new_student[1] = sex
        new_student[2] = age
        new_student[30] = g1
        new_student[31] = g2
        new_student[32] = g3

        self.students.append(new_student)

        print("\nStudent Added Successfully.")

    # =========================
    # 3. Search Student
    # =========================
    def search_student(self):

        print("\n===== SEARCH STUDENT =====")

        school = input("Enter School to Search: ")

        found = False

        for row in self.students:

            if len(row) > 0 and row[0].lower() == school.lower():

                print("\nStudent Found:")
                print(row)

                found = True

        if not found:
            print("\nStudent Not Found.")

    # =========================
    # 4. Average Marks
    # =========================
    def average_marks(self):

        print("\n===== AVERAGE MARKS =====")

        total = 0
        count = 0

        for row in self.students:

            try:
                if len(row) > 32:
                    marks = float(row[32])

                    total += marks
                    count += 1

            except ValueError:
                continue

        if count == 0:
            print("No valid marks available.")
        else:
            average = total / count
            print(f"Average G3 Marks: {average:.2f}")

    # =========================
    # 5. Update Student
    # =========================
    def update_student(self):

        print("\n===== UPDATE STUDENT =====")

        if not self.students:
            print("No student records available.")
            return

        for i, row in enumerate(self.students):
            print(f"{i + 1}. {row}")

        try:
            record_no = int(input("\nEnter Record Number to Update: "))

            if record_no < 1 or record_no > len(self.students):
                print("Invalid Record Number.")
                return

            index = record_no - 1

            print("\nCurrent Record:")
            print(self.students[index])

            school = input("Enter New School: ")
            sex = input("Enter New Sex: ")
            age = input("Enter New Age: ")
            g1 = input("Enter New G1 Marks: ")
            g2 = input("Enter New G2 Marks: ")
            g3 = input("Enter New G3 Marks: ")

            self.students[index][0] = school
            self.students[index][1] = sex
            self.students[index][2] = age
            self.students[index][30] = g1
            self.students[index][31] = g2
            self.students[index][32] = g3

            print("\nStudent Updated Successfully.")

        except ValueError:
            print("Please enter a valid number.")

    # =========================
    # 6. Delete Student
    # =========================
    def delete_student(self):

        print("\n===== DELETE STUDENT =====")

        if not self.students:
            print("No student records available.")
            return

        for i, row in enumerate(self.students):
            print(f"{i + 1}. {row}")

        try:
            record_no = int(input("\nEnter Record Number to Delete: "))

            if record_no < 1 or record_no > len(self.students):
                print("Invalid Record Number.")
                return

            index = record_no - 1

            print("\nSelected Record:")
            print(self.students[index])

            confirm = input("\nAre you sure you want to delete this record? (yes/no): ")

            if confirm.lower() == "yes":

                self.students.pop(index)

                print("\nStudent Deleted Successfully.")

            else:
                print("\nDelete Operation Cancelled.")

        except ValueError:
            print("Please enter a valid number.")

    # =========================
    # 7. Save Records
    # =========================
    def save_records(self):

        print("\n===== SAVE RECORDS =====")

        try:

            with open(self.filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerows(self.students)

            print("Records Saved Successfully.")

        except Exception as e:

            print("Error while saving records:", e)

# =========================
# Main Program
# =========================
def main():

    filename = "student_data.csv"

    manager = StudentManager(filename)

    while True:

        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Display Students")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Average Marks")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Save Records")
        print("8. Exit")
        print("================================")

        choice = input("Enter Choice: ")

        if choice == "1":
            manager.display_students()

        elif choice == "2":
            manager.add_student()

        elif choice == "3":
            manager.search_student()

        elif choice == "4":
            manager.average_marks()

        elif choice == "5":
            manager.update_student()

        elif choice == "6":
            manager.delete_student()

        elif choice == "7":
            manager.save_records()

        elif choice == "8":
            print("\nExiting Student Management System...")
            break

        else:
            print("\nInvalid Choice. Please try again.")

# =========================
# Program Start
# =========================
if __name__ == "__main__":
    main()