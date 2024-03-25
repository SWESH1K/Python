class Loan:
    def __init__(self,principal_amount: int,intrest_rate: float,no_years: int):
        self._principal_amount = principal_amount
        self._intrest_rate = intrest_rate
        self._no_years = no_years

    def get_principal_amount(self):
        return self._principal_amount

    def get_interest_rate(self):
        return self._intrest_rate
    
    def get_total_amount(self):
        return self._principal_amount + (self._intrest_rate/100 * self._principal_amount)*self._no_years
    
    def get_monthly_payment(self):
        total_amount = self.get_total_amount()
        monthly_amount = total_amount/(self._no_years*12)
        return round(monthly_amount,2)
    
    def get_analysis(self):
        return {
            "Principal Amount $":self.get_principal_amount(),
            "Interest Rate %":self.get_interest_rate(),
            "Total amount to be paid":self.get_total_amount(),
            "Monthly amount":self.get_monthly_payment(),
        }

def main():
    user = Loan(1_00_000, 3, 3)
    details = user.get_analysis()
    for key,value in details.items():
        print(f"{key}:{value}")

if __name__ == "__main__":
    main()