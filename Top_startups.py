# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("F:\Downloads\startup_funding.csv",encoding = 'utf-8')
df['Startup Name'].replace('Oyorooms','Oyo',inplace = True)
df['Startup Name'].replace('OyoRooms','Oyo',inplace = True)
df['Startup Name'].replace('Oyo Rooms','Oyo',inplace = True)
df['Startup Name'].replace('OYO Rooms','Oyo',inplace = True)
df['Startup Name'].replace('Olacabs','Ola',inplace = True)
df['Startup Name'].replace('Ola Cabs','Ola',inplace = True)
df['Startup Name'].replace('Olacabs','Ola',inplace = True)
df['Startup Name'].replace('Flipkart.com','Flipkart',inplace = True)
df['Startup Name'].replace('Paytm Marketplace','Paytm',inplace = True)
df["Amount in USD"]=df["Amount in USD"].apply(lambda x : float(str(x).replace(",","")))

df=df.groupby("Startup Name")["Amount in USD"].sum()
df=df.sort_values(ascending=False)[:5]
startup=df.index
for i in range(5):
    print(startup[i])
