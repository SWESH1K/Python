
# Function to calculate tax.
def tax_calculator(actual_salary):
    print("Original salary",actual_salary)
    temp = actual_salary
    tax_amount, tax_percent = 0, 0 # The tax amount of user and initial tax percent will be 0
    tax_base = 3_00_000 # The base tax bound will be  3 lakhs since below three lakhs is taxfree!
    while(temp > 0):
        if(temp >= tax_base):
            tax_amount += tax_base * tax_percent/100
            temp -= tax_base
            tax_percent+=5
            tax_base+=3_00_000
        else:
            tax_amount += temp * tax_percent/100
            temp -= tax_base
    print("Tax Amount =",tax_amount)
    return actual_salary-tax_amount ## Atlast we will return the original salary - tax amount.

# Class for Pay-roll system
class PayRollSystem:
    print("Calculating Payroll")
    print("===================")
    def get_salary(self, employees):
        for employee in employees:
            print(f"Employee id:{employee.id}\nEmployee name:{employee.name}")
            print("The salary of employee:",employee.get_salary(),"\n")
    def get_annual_salary(self, employees):
        for employee in employees:
            print(f"Employee id:{employee.id}\nEmployee name:{employee.name}")
            print("The final annual salary of employee:",employee.get_annual_salary(),"\n")

# Parent class for Employee
class Employee:
    def __init__(self,id,name) -> None:
        self.name = name
        self.id = id

class MonthlyEmployee(Employee):
    def __init__(self,id,name,monthly_salary):
        super().__init__(id,name)
        self.monthly_salary = monthly_salary

    def get_salary(self):
        return self.monthly_salary
    
    def get_annual_salary(self):
        actual_salary = self.monthly_salary * 12
        return tax_calculator(actual_salary)
    
class HourlyEmployee(Employee):
    def __init__(self, id, name, per_hour, no_hour):
        super().__init__(id, name)
        self.per_hour = per_hour
        self.no_hour = no_hour

    def get_salary(self):
        return self.per_hour * self.no_hour
    
    def get_annual_salary(self):
        actual_salary = self.per_hour * 24 * 365
        return tax_calculator(actual_salary)

class CommissionEmployee(MonthlyEmployee):
    def __init__(self, id, name, monthly_salary, commision):
        super().__init__(id, name, monthly_salary)
        self.commision = commision

    def get_salary(self):
        return self.monthly_salary + self.commision
    
    def get_annual_salary(self):
        actual_salary = (self.monthly_salary + self.commision) * 12
        return tax_calculator(actual_salary)