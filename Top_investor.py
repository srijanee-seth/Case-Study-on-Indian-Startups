# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np

df=pd.read_csv("F:\Downloads\startup_funding.csv", encoding='utf-8')
df.dropna(subset=['Investors Name'],inplace=True)

d={}

def investor_name(invest):
    l=invest.split(',')
    for i in l:
        i=i.strip()
        d[i]=d.get(i,0)+1
    return l

df['Investors Name'].apply(investor_name)

key=np.array(list(d.keys()))
values=np.array(list(d.values()))

ind=values.argmax()
print(key[ind],values[ind])

 
