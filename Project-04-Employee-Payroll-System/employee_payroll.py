import csv
import os
from abc import ABC, abstractmethod

# ============================================================
# Abstract Base Class
# ============================================================
class EmployeeBase(ABC):

    @abstractmethod
    def display(self):
        pass

# ============================================================
# Employee Class
# Demonstrates encapsulation using private attributes
# ============================================================
class Employee(EmployeeBase):

    def __init__(
        self,
        employee_id,
        name,
        department,
        experience_years,
        education_level,
        age,
        gender,
        city,
        monthly_salary
    ):
        self.__employee_id = employee_id
        self.__name = name
        self.__department = department
        self.__experience_years = experience_years
        self.__education_level = education_level
        self.__age = age
        self.__gender = gender
        self.__city = city
        self.__monthly_salary = monthly_salary

    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_experience_years(self):
        return self.__experience_years

    def get_education_level(self):
        return self.__education_level

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_city(self):
        return self.__city

    def get_monthly_salary(self):
        return self.__monthly_salary

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_monthly_salary(self, monthly_salary):
        self.__monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.__monthly_salary * 12

    def display(self):
        print(
            self.__employee_id,
            "|",
            self.__name,
            "|",
            self.__department,
            "|",
            self.__monthly_salary
        )

# ============================================================
# Payroll Employee
# Demonstrates inheritance
# ============================================================
class PayrollEmployee(Employee):

    def calculate_annual_salary(self):
        return self.get_monthly_salary() * 12

    def generate_payslip(self):
        print("\n========================================")
        print("             EMPLOYEE PAYSLIP")
        print("========================================")
        print("Employee ID       :", self.get_employee_id())
        print("Name              :", self.get_name())
        print("Department        :", self.get_department())
        print("Experience        :", self.get_experience_years(), "years")
        print("Education Level   :", self.get_education_level())
        print("Age               :", self.get_age())
        print("Gender            :", self.get_gender())
        print("City              :", self.get_city())
        print("----------------------------------------")
        print("Monthly Salary    : ₹{:.2f}".format(
            self.get_monthly_salary()
        ))
        print("Annual Salary     : ₹{:.2f}".format(
            self.calculate_annual_salary()
        ))
        print("========================================")

# ============================================================
# Payroll Manager
# ============================================================
class PayrollManager:

    FILE_NAME = "employee_salary_dataset.csv"

    # Exact columns from the CSV dataset.
    HEADERS = ['EmployeeID', 'Name', 'Department', 'Experience_Years', 'Education_Level', 'Age', 'Gender', 'City', 'Monthly_Salary']

    def __init__(self):
        self.check_file()

    def check_file(self):

        if not os.path.exists(self.FILE_NAME):
            print("\nError: employee_salary_dataset.csv not found.")
            print(
                "Please keep the CSV file in the same folder "
                "as employee_payroll.py."
            )

    def salary_value(self, value):

        try:
            return float(
                str(value).replace(",", "").replace("₹", "").strip()
            )
        except (ValueError, TypeError):
            return 0.0

    def read_employees(self):

        employees = []

        try:
            with open(
                self.FILE_NAME,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    employee = PayrollEmployee(
                        row.get("EmployeeID", "").strip(),
                        row.get("Name", "").strip(),
                        row.get("Department", "").strip(),
                        row.get("Experience_Years", "").strip(),
                        row.get("Education_Level", "").strip(),
                        row.get("Age", "").strip(),
                        row.get("Gender", "").strip(),
                        row.get("City", "").strip(),
                        self.salary_value(
                            row.get("Monthly_Salary", "")
                        )
                    )

                    employees.append(employee)

        except FileNotFoundError:
            print("\nemployee_salary_dataset.csv not found.")

        except Exception as e:
            print("\nError reading employee data:", e)

        return employees

    def save_employees(self, employees):

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

                for employee in employees:

                    writer.writerow({
                        "EmployeeID": employee.get_employee_id(),
                        "Name": employee.get_name(),
                        "Department": employee.get_department(),
                        "Experience_Years": employee.get_experience_years(),
                        "Education_Level": employee.get_education_level(),
                        "Age": employee.get_age(),
                        "Gender": employee.get_gender(),
                        "City": employee.get_city(),
                        "Monthly_Salary": employee.get_monthly_salary()
                    })

            print("\nPayroll Data Saved Successfully.")

        except Exception as e:
            print("\nError saving payroll data:", e)

    def add_employee(self):

        print("\n===== ADD EMPLOYEE =====")

        employee_id = input("Enter Employee ID: ").strip()
        name = input("Enter Employee Name: ").strip()
        department = input("Enter Department: ").strip()
        experience = input("Enter Experience (Years): ").strip()
        education = input("Enter Education Level: ").strip()
        age = input("Enter Age: ").strip()
        gender = input("Enter Gender: ").strip()
        city = input("Enter City: ").strip()
        salary_text = input("Enter Monthly Salary: ").strip()

        if not all([
            employee_id,
            name,
            department,
            experience,
            education,
            age,
            gender,
            city,
            salary_text
        ]):
            print("\nAll fields are required.")
            return

        try:
            experience_value = float(experience)
            age_value = int(age)
            monthly_salary = self.salary_value(salary_text)

            if experience_value < 0 or age_value <= 0 or monthly_salary < 0:
                raise ValueError

        except ValueError:
            print(
                "\nPlease enter valid numeric values for "
                "experience, age, and salary."
            )
            return

        employees = self.read_employees()

        for employee in employees:
            if employee.get_employee_id() == employee_id:
                print("\nEmployee ID already exists.")
                return

        new_employee = PayrollEmployee(
            employee_id,
            name,
            department,
            experience,
            education,
            str(age_value),
            gender,
            city,
            monthly_salary
        )

        employees.append(new_employee)
        self.save_employees(employees)

        print("\nEmployee Added Successfully.")

    def calculate_salary(self):

        print("\n===== CALCULATE SALARY =====")

        employee_id = input("Enter Employee ID: ").strip()

        if employee_id == "":
            print("\nPlease enter an Employee ID.")
            return

        employees = self.read_employees()

        for employee in employees:

            if employee.get_employee_id() == employee_id:

                monthly = employee.get_monthly_salary()
                annual = employee.calculate_annual_salary()

                print("\nEmployee Found")
                print("-" * 40)
                print("Employee ID    :", employee.get_employee_id())
                print("Name           :", employee.get_name())
                print("Department     :", employee.get_department())
                print("Monthly Salary : ₹{:.2f}".format(monthly))
                print("Annual Salary  : ₹{:.2f}".format(annual))
                print("-" * 40)

                return

        print("\nEmployee Not Found.")

    def generate_payslip(self):

        print("\n===== GENERATE PAYSLIP =====")

        employee_id = input("Enter Employee ID: ").strip()

        if employee_id == "":
            print("\nPlease enter an Employee ID.")
            return

        employees = self.read_employees()

        for employee in employees:

            if employee.get_employee_id() == employee_id:
                employee.generate_payslip()
                return

        print("\nEmployee Not Found.")

    def search_employee(self):

        print("\n===== SEARCH EMPLOYEE =====")

        search = input(
            "Enter Employee ID or Name to Search: "
        ).strip().lower()

        if search == "":
            print("\nPlease enter a search value.")
            return

        employees = self.read_employees()
        found = False

        for employee in employees:

            employee_id = employee.get_employee_id().lower()
            name = employee.get_name().lower()

            if search == employee_id or search in name:

                print("\nEmployee Found")
                print("-" * 45)
                print("Employee ID    :", employee.get_employee_id())
                print("Name           :", employee.get_name())
                print("Department     :", employee.get_department())
                print("Experience     :", employee.get_experience_years())
                print("Education      :", employee.get_education_level())
                print("Age            :", employee.get_age())
                print("Gender         :", employee.get_gender())
                print("City           :", employee.get_city())
                print("Monthly Salary : ₹{:.2f}".format(
                    employee.get_monthly_salary()
                ))
                print("-" * 45)

                found = True

        if not found:
            print("\nEmployee Not Found.")

    def display_employees(self):

        print("\n===== ALL EMPLOYEES =====")
        print("-" * 100)

        employees = self.read_employees()

        if not employees:
            print("No Employees Found.")
            return

        for employee in employees:

            print(
                employee.get_employee_id(),
                "|",
                employee.get_name(),
                "|",
                employee.get_department(),
                "|",
                employee.get_experience_years(),
                "|",
                employee.get_city(),
                "| ₹{:.2f}".format(
                    employee.get_monthly_salary()
                )
            )

        print("-" * 100)

    def save_payroll_data(self):

        employees = self.read_employees()
        self.save_employees(employees)

# ============================================================
# Create Payroll Manager
# ============================================================
payroll = PayrollManager()


# ============================================================
# Main Menu
# ============================================================
while True:

    print("\n========================================")
    print("        EMPLOYEE PAYROLL SYSTEM")
    print("========================================")
    print("1. Add Employee")
    print("2. Calculate Salary")
    print("3. Generate Payslip")
    print("4. Search Employee")
    print("5. Display Employees")
    print("6. Save Payroll Data")
    print("7. Exit")
    print("========================================")

    choice = input("Enter Choice: ").strip()

    try:

        if choice == "1":
            payroll.add_employee()

        elif choice == "2":
            payroll.calculate_salary()

        elif choice == "3":
            payroll.generate_payslip()

        elif choice == "4":
            payroll.search_employee()

        elif choice == "5":
            payroll.display_employees()

        elif choice == "6":
            payroll.save_payroll_data()

        elif choice == "7":
            print("\nThank you for using Employee Payroll System.")
            break

        else:
            print("\nInvalid Choice. Please try again.")

    except KeyboardInterrupt:
        print("\n\nProgram stopped by user.")
        break

    except Exception as e:
        print("\nAn unexpected error occurred:", e)