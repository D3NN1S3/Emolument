
class Emolument:
    def __init__(self, basic_salary, tax_relief):
        self.__basic_salary = basic_salary
        self.__tax_relief = tax_relief

    def getBasicSalary(self):
        return self.__basic_salary

    def getTaxRelief(self):
        return self.__tax_relief

    def SSNIT(self):
        return self.__basic_salary * 0.035

    def taxableIncome(self):
        return self.__basic_salary - (self.__tax_relief + self.SSNIT())

class MyEmolument(Emolument):
    def __init__(self, basic_salary=0, tax_relief=0):
        super().__init__(basic_salary, tax_relief)

    def incomeTax(self):
        taxable_income = self.taxableIncome()
        if taxable_income <= 500:
            return taxable_income * 0.05
        elif taxable_income <= 1000:
            return (500 * 0.05) + ((taxable_income - 500) * 0.125)
        else:
            return (500 * 0.05) + (500 * 0.125) + ((taxable_income - 1000) * 0.175)

    def totalDeduction(self):
        return self.SSNIT() + self.incomeTax()

    def netSalary(self):
        return self.getBasicSalary() - self.totalDeduction()
