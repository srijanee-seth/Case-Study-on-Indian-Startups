# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("F:\Downloads\startup_funding.csv",encoding = 'utf-8')
df['Industry Vertical'].replace('ECommerce','Ecommerce',inplace = True)
df['Industry Vertical'].replace('eCommerce','Ecommerce',inplace = True)
df['Industry Vertical'].replace('ecommerce','Ecommerce',inplace = True)
df['Amount in USD'] = df['Amount in USD'].apply(lambda x: float(str(x).replace(",","")))
df = df.groupby('Industry Vertical')['Amount in USD'].sum()
df = df.sort_values(ascending = False)[:5]
industry = df.index
amount = df.values

plt.pie(amount,labels = industry,autopct='%0.2f',counterclock=False,startangle=100)
plt.show()
percent = np.true_divide(amount,amount.sum())*100
for i in range(len(industry)):
    print(industry[i],format(percent[i],'0.2f'))
