from LoanCase import *

class Profit_Outcome(Outcome):
    def __init__(self, mrev, mexp, Loan, rev_growth_years, exp_growth_years, times_years,equity):
        super().__init__(mrev, mexp, Loan, rev_growth_years, exp_growth_years, times_years)
        self.equity = equity

    def Result(self):
        Total_rev = 0
        Total_exp = 0 
        Total_loan = self.loan
        yearly_rev = self.mrev*12
        yearly_exp = self.mexp*12
        Len = len(self.times)
        for i in range(Len):
            for j in range(self.times[i]):
                yearly_rev = yearly_rev*(1 + ((self.rev_growth[i])/100))
                yearly_exp = yearly_exp*(1 + ((self.exp_growth[i])/100))
                Total_rev = Total_rev + yearly_rev
                Total_exp = Total_exp + yearly_exp


        Profit = Total_rev - Total_exp - Total_loan
        Net_Profit = Profit*(1 - ((self.equity)/100))

        print(f"Initial Monthly Revenue = {self.mrev:.2f}")
        print(f"Initial Monthly Expense = {self.mexp:.2f}")
        print("Time, Revenue Growth Rate, Expense Growth Rate matrix below:")
        print(self.times)
        print(self.rev_growth)
        print(self.exp_growth)
        print(f"Total revenue = {Total_rev:.2f}")
        print(f"Total expenses = {Total_exp:.2f}")
        print(f"Total loan = {Total_loan:.2f}")
        E = (1 - ((self.equity)/100))*100
        print(f"Equity Held = {E:.2f}")
        print(f"Profit = {Profit:.2f}")
        print(f"Net Profit = {Net_Profit:.2f}")
        print("\n")


