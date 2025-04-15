from LoanCase import *
from NetProfit import *
import pandas as pd
import matplotlib.pyplot as plt

L1 = Loan(100000,5,5)
L2 = Loan(50000,5,5)

#Three cases, no profit nor loss, profit and loss

O1 = Profit_Outcome(5000,3000,L1.total,[0],[0],[10],0)
O1T = O1.Total()

O2 = Profit_Outcome(5000,3000,0,[0],[0],[10],20)
O2T = O2.Total()

O3 = Profit_Outcome(5000,3000,L2.total,[0],[0],[10],10)
O3T = O3.Total()

Profit_1 = Profit_Outcome(5000,3000,L1.total,[10,7.5,5],[12,6,2.5],[2,3,5],0)
Profit_1T = Profit_1.Total()

Profit_2 = Profit_Outcome(5000,3000,0,[10,7.5,5],[15,6,2.5],[2,3,5],20)
Profit_2T = Profit_2.Total()

Profit_3 = Profit_Outcome(5000,3000,L2.total,[10,7.5,5],[12,6,2.5],[2,3,5],10)
Profit_3T = Profit_3.Total()

Loss_1 = Profit_Outcome(5000,3000,L1.total,[12,5,0],[12,8,2],[2,3,5],0)
Loss_1T = Loss_1.Total()

Loss_2 = Profit_Outcome(5000,3000,0,[12,5,0],[12,8,2],[2,3,5],20)
Loss_2T = Loss_2.Total()

Loss_3 = Profit_Outcome(5000,3000,L2.total,[12,5,0],[12,8,2],[2,3,5],10)
Loss_3T = Loss_3.Total()

data3 = {
    "Cases" : ["Loss_Loan","Loss_Equity","Loss_Both"],
    "Initial_Monthly_Revenue": [5000,5000,5000],
    "Initial_Monthly_ Expenses" : [3000,3000,3000],
    "Loan_Incurred" : [L1.total,0,L2.total],
    "RevGR - 2":[12,12,12],
    "ExpGR - 2":[12,12,12],
    "RevGR - 3":[5,5,5],
    "ExpGR - 3":[8,8,8],
    "RevGR - 5":[0,0,0],
    "ExpGR - 5":[2,2,2],
    "Total Revenue":[Loss_1T[0],Loss_2T[0],Loss_3T[0]],
    "Net Revenue": [Loss_1T[1],Loss_2T[1],Loss_3T[1]]
}

data2 = {
    "Cases" : ["Profit_Loan","Profit_Equity","profit_Both"],
    "Initial_Monthly_Revenue": [5000,5000,5000],
    "Initial_Monthly_ Expenses" : [3000,3000,3000],
    "Loan_Incurred" : [L1.total,0,L2.total],
    "RevGR - 2":[10,10,10],
    "ExpGR - 2":[12,12,12],
    "RevGR - 3":[7.5,7.5,7.5],
    "ExpGR - 3":[6,6,6],
    "RevGR - 5":[5,5,5],
    "ExpGR - 5":[2.5,2.5,2.5],
    "Total Revenue":[Profit_1T[0],Profit_2T[0],Profit_3T[0]],
    "Net Revenue": [Profit_1T[1],Profit_2T[1],Profit_3T[1]]
}

data1 = {
    "Cases" : ["Constant_Loan","Constant_Equity","Constant_Both"],
    "Initial_Monthly_Revenue": [5000,5000,5000],
    "Initial_Monthly_ Expenses" : [3000,3000,3000],
    "Loan_Incurred" : [L1.total,0,L2.total],
    "RevGR - 2":[0,0,0],
    "ExpGR - 2":[0,0,0],
    "RevGR - 3":[0,0,0],
    "ExpGR - 3":[0,0,0],
    "RevGR - 5":[0,0,0],
    "ExpGR - 5":[0,0,0],
    "Total Revenue":[O1T[0],O2T[0],O3T[0]],
    "Net Revenue": [O1T[1],O2T[1],O3T[1]]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
dfList = [df1,df2,df3]
df = pd.concat(dfList)
df = df.sort_values(by = ["Net Revenue"] , ascending = False)
print(df)
df.to_csv("Financeoptions_10years.csv" , index = False)
print(df.describe())

df.set_index("Cases")[["Total Revenue", "Net Revenue"]].plot(kind="bar", title="Revenue Comparison for 10 Years")
plt.ylabel("Amount in Thousands")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
