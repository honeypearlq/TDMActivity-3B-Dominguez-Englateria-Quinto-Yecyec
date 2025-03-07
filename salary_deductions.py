def compute_salary_deductions(gross_salary):
    """Calculates salary deductions and net salary."""
    sss_deduction = 1200
    philhealth_deduction = (gross_salary * 0.05) / 2
    pagibig_deduction = 100
    tax_deduction = 1875  

    total_deductions = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
    net_salary = gross_salary - total_deductions

    print("\n=== Salary Breakdown ===")
    print(f"Gross Salary: {gross_salary:.2f}")
    print(f"SSS Deduction: {sss_deduction:.2f}")
    print(f"PhilHealth Deduction: {philhealth_deduction:.2f}")
    print(f"Pag-IBIG Deduction: {pagibig_deduction:.2f}")
    print(f"Tax Deduction: {tax_deduction:.2f}")
    print(f"Total Deductions: {total_deductions:.2f}")
    print(f"Net Salary: {net_salary:.2f}")



try:
    user_salary = float(input("Enter your monthly salary: "))
    if user_salary <= 0:
        raise ValueError("Salary must be a positive number.")
    
    compute_salary_deductions(user_salary)

except ValueError as e:
    print("Invalid input:", e)