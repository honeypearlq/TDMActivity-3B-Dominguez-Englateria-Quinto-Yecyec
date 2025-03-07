class Employee:
    def __init__(self, salary):
        self.salary = salary
        self.sss_deduction = self.get_sss_deduction()
        self.pagibig_deduction = self.get_pagibig_deduction()
        self.philhealth_deduction = self.compute_philhealth_deduction()
        self.tax_deduction = self.calculate_tax_deduction()
        self.total_deductions = self.compute_total_deductions()
        self.net_salary = self.compute_net_salary()

    def get_sss_deduction(self):
        return 1200  

    def get_pagibig_deduction(self):
        return 100  

    def compute_philhealth_deduction(self):
        return (self.salary * 0.05) / 2  

    def calculate_tax_deduction(self):
        """ Implements progressive tax deduction based on salary brackets. """
        if self.salary <= 20000:
            return self.salary * 0.05  # 5% for lower income
        elif self.salary <= 50000:
            return self.salary * 0.10  # 10% for middle income
        else:
            return self.salary * 0.15  # 15% for higher income

    def compute_total_deductions(self):
        return (
            self.sss_deduction +
            self.pagibig_deduction +
            self.philhealth_deduction +
            self.tax_deduction
        )

    def compute_net_salary(self):
        return self.salary - self.total_deductions

    def get_salary_details(self):
        return {
            "Gross Salary": self.salary,
            "SSS Deduction": self.sss_deduction,
            "Pag-IBIG Deduction": self.pagibig_deduction,
            "PhilHealth Deduction": self.philhealth_deduction,
            "Tax Deduction": self.tax_deduction,
            "Total Deductions": self.total_deductions,
            "Net Salary": self.net_salary
        }

def get_valid_salary():
    while True:
        try:
            salary_input = input("Enter your monthly salary: ").strip()
            salary = float(salary_input)
            if salary <= 0:
                raise ValueError("Salary must be a positive number.")
            return salary
        except ValueError:
            print("Invalid input. Please enter a valid positive number for salary.")

def main():
    salary = get_valid_salary()
    employee = Employee(salary)

    print("\nSalary Breakdown:")
    print("=" * 30)
    for key, value in employee.get_salary_details().items():
        print(f"{key}: ₱{value:,.2f}")

if __name__ == "__main__":
    main()