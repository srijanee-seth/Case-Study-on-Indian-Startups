# Open and read data file as specified in the question
# Print the required output in given format
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("F:\Downloads\startup_funding.csv",encoding = 'utf-8')
df['Investment Type'].replace('Seed Funding','Seed Funding',inplace = True)
df['Investment Type'].replace('Private Equity','Private Equity',inplace = True)
df['Investment Type'].replace('Debt Funding','Debt Funding',inplace = True)
df['Investment Type'].replace('Crowd funding','Crowd Funding',inplace = True)
df['Amount in USD'] = df['Amount in USD'].apply(lambda x: float(str(x).replace(",","")))

df = df.groupby('Investment Type')['Amount in USD'].sum()
df = df.sort_values(ascending = False)[:10]
investment = df.index
amount = df.values

plt.pie(amount,labels = investment,autopct='%0.2f',counterclock=False,startangle=110)
plt.show()

percent = np.true_divide(amount,amount.sum())*100
for i in range(len(investment)):
    print(investment[i],format(percent[i],'0.2f'))
