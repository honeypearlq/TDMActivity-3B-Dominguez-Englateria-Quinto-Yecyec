#use of modular functions for individual calculations
def get_sss_deduction():
    return 1200  

def get_pagibig_deduction():
    return 100  

def compute_philhealth_deduction(salary):
    return (salary * 0.05) / 2  

def compute_tax_deduction():
    return 1875  

def compute_total_deductions(salary):
    sss = get_sss_deduction()
    pagibig = get_pagibig_deduction()
    philhealth = compute_philhealth_deduction(salary)
    tax = compute_tax_deduction()

    total = sss + pagibig + philhealth + tax
    return total, sss, pagibig, philhealth, tax

#improved naming
def compute_net_salary(salary):
    deductions, sss, pagibig, philhealth, tax = compute_total_deductions(salary)
    net_salary = salary - deductions

    return {
        "Gross Salary": salary,
        "SSS Deduction": sss,
        "Pag-IBIG Deduction": pagibig,
        "PhilHealth Deduction": philhealth,
        "Tax Deduction": tax,
        "Total Deductions": deductions,
        "Net Salary": net_salary
    }

def main():
    try:
        salary = float(input("Enter your monthly salary: "))
        if salary <= 0:
            raise ValueError("Salary must be a positive number.")

        salary_details = compute_net_salary(salary)
        for key, value in salary_details.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print("Invalid input:", e)

if _name_ == "_main_":
    main()