#Growth only at end of year
#Revenue Constant throughtout year

class Loan: 
    def __init__(self,principal_amount,interest_rate,time_in_years):
        self.principal = principal_amount
        self.ir = interest_rate
        self.time = time_in_years
        self.per_month = (principal_amount*((1 + (interest_rate/100))**time_in_years))/(time_in_years*12)
        self.total = ((self.per_month)*(time_in_years)*12)

class Outcome:
    def __init__(self,mrev,mexp,Loan,rev_growth_years,exp_growth_years,times_years):
        self.mrev = mrev
        self.mexp = mexp
        self.loan = Loan
        self.rev_growth = rev_growth_years
        self.exp_growth = exp_growth_years
        self.times = times_years

    def Calculating(self):
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

        print(Total_rev)
        print(Total_exp)
        print(Total_loan)
        print(Profit)
        print("\n")
    




        



    