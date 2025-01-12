
from emolument import MyEmolument
from tabulate import tabulate

def displayResults(emolument):
    data = [
        ["Basic Salary", f"{emolument.getBasicSalary():.2f}"],
        ["Tax Relief", f"{emolument.getTaxRelief():.2f}"],
        ["SSNIT Contribution", f"{emolument.SSNIT():.2f}"],
        ["Taxable Income", f"{emolument.taxableIncome():.2f}"],
        ["Income Tax", f"{emolument.incomeTax():.2f}"],
        ["Total Deduction", f"{emolument.totalDeduction():.2f}"],
        ["Net Salary", f"{emolument.netSalary():.2f}"],
    ]
    print(tabulate(data, headers=["Description", "Amount"], tablefmt="grid"))

def main():
    print("Enter the following details:")
    basic_salary = float(input("Basic Salary: "))
    tax_relief = float(input("Tax Relief: "))

    staff_salary = MyEmolument(basic_salary, tax_relief)
    print("\n--- Staff Salary Details ---")
    displayResults(staff_salary)

if __name__ == "__main__":
    main()
