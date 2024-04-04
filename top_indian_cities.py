# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
df = pd.read_csv("F:\Downloads\startup_funding.csv")
df.dropna(subset=["city location"], inplace=True)
def seperateCity(city):
    return city.split("/")[0].strip()
df["city location"]=df["city location"].apply(seperateCity)
df[df["city location"]=="bangalore"] = "Bangalore"
df[df["city location"]=="Delhi"]="New Delhi"
city=df["city location"]
city=city.value_counts()[:10]
city_name=city.index
no_of_fund=city.values
plt.pie(no_of_fund,labels=city_name,autopct="%.2f%%",counterclock=False)
plt.title("Number of startup in city")
plt.axis("equal")
plt.show()
for i in range(city_name.shape[0]):
    print(city_name[i],no_of_fund[i])
