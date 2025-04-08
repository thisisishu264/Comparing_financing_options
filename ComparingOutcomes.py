from LoanCase import *
from NetProfit import *

L1 = Loan(100000,5,5)
L2 = Loan(50000,5,5)

O1 = Profit_Outcome(5000,3000,L1.total,[0],[0],[10],0)
O1.Result()

O2 = Profit_Outcome(5000,3000,0,[0],[0],[10],20)
O2.Result()

O3 = Profit_Outcome(5000,3000,L2.total,[0],[0],[10],10)
O3.Result()

O4 = Profit_Outcome(5000,3000,L1.total,[10,7.5,5],[12,6,2.5],[2,3,5],0)
O4.Result()

O5 = Profit_Outcome(5000,3000,0,[10,7.5,5],[15,6,2.5],[2,3,5],20)
O5.Result()

O6 = Profit_Outcome(5000,3000,L2.total,[10,7.5,5],[12,6,2.5],[2,3,5],10)
O6.Result()

O7 = Profit_Outcome(5000,3000,L1.total,[12,5,0],[12,8,2],[2,3,5],0)
O7.Result()

O8 = Profit_Outcome(5000,3000,0,[12,5,0],[12,8,2],[2,3,5],20)
O8.Result()

O9 = Profit_Outcome(5000,3000,L2.total,[12,5,0],[12,8,2],[2,3,5],10)
O9.Result()

O10 = Profit_Outcome(5000,3000,L1.total,[0],[0],[20],0)
O10.Result()

O11 = Profit_Outcome(5000,3000,0,[0],[0],[20],20)
O11.Result()

O12 = Profit_Outcome(5000,3000,L2.total,[0],[0],[20],10)
O12.Result()

O13 = Profit_Outcome(5000,3000,L1.total,[10,7.5,5,4],[12,6,2.5,1.5],[2,3,5,10],0)
O13.Result()

O14 = Profit_Outcome(5000,3000,0,[10,7.5,5,4],[12,6,2.5,1.5],[2,3,5,10],20)
O14.Result()

O15 = Profit_Outcome(5000,3000,L2.total,[10,7.5,5,4],[12,6,2.5,1],[2,3,5,10],10)
O15.Result()

O16 = Profit_Outcome(5000,3000,L1.total,[12,5,0,-0.25],[12,8,2,0.5],[2,3,5,10],0)
O16.Result()

O17 = Profit_Outcome(5000,3000,0,[12,5,0,-0.25],[12,8,2,0.5],[2,3,5,10],20)
O17.Result()

O18 = Profit_Outcome(5000,3000,L2.total,[12,5,0,-0.25],[12,8,2,0.5],[2,3,5,10],10)
O18.Result()
