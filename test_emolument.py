
import unittest
from emolument import MyEmolument

class TestEmolument(unittest.TestCase):
    def test_ssnit(self):
        emol = MyEmolument(2000, 300)
        self.assertAlmostEqual(emol.SSNIT(), 70.0)

    def test_taxable_income(self):
        emol = MyEmolument(2000, 300)
        self.assertAlmostEqual(emol.taxableIncome(), 1630.0)

    def test_income_tax(self):
        emol = MyEmolument(2000, 300)
        self.assertAlmostEqual(emol.incomeTax(), 212.75)

    def test_total_deduction(self):
        emol = MyEmolument(2000, 300)
        self.assertAlmostEqual(emol.totalDeduction(), 282.75)

    def test_net_salary(self):
        emol = MyEmolument(2000, 300)
        self.assertAlmostEqual(emol.netSalary(), 1717.25)

if __name__ == "__main__":
    unittest.main()
