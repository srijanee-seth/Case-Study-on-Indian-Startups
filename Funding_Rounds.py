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

totalfunding = df['Startup Name'].value_counts()[:5]
startupname = totalfunding.index
count = totalfunding.values
for i in range(5):
    print(startupname[i],count[i])
