import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


df = pd.read_csv("F:\Downloads\startup_funding.csv",encoding = 'utf-8')
df.dropna(subset=["city location"],inplace=True)
def separateCity(city):
    return city.split('/')[0].strip()
df['city location'] = df['city location'].apply(separateCity)
df['city location'].replace("Delhi","New Delhi",inplace = True)
df['city location'].replace("bangalore","Bangalore",inplace = True)
df[df["Amount in USD"]=="Undisclosed"]=0.0
df[df["Amount in USD"]=="undisclosed"]=0.0
df[df["Amount in USD"]=="unknown"]=0.0
df[df["Amount in USD"]=="N/A"]=0.0
df['Amount in USD'] = df['Amount in USD'].apply(lambda x: float(str(x).replace(",","") ))
df = df.groupby('city location')['Amount in USD'].sum()
df = df.sort_values(ascending = False)[0:10]
city = df.index
amount = df.values
explode = [0.2,0.2,0.2,0.2,0.1,0.1,0.2,0.2,0.2,0.2]
plt.pie(amount,labels = city,autopct='%0.2f',counterclock=False,startangle=90,explode =explode,radius=1.5)
plt.show()

percent = np.true_divide(amount,amount.sum())*100
for i in range(len(city)):
    print(city[i],format(percent[i],'0.2f'))
