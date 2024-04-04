# Open and read data file as specified in the question
# Print the required output in given format
import csv
import pandas as pd
import matplotlib.pyplot as plt
import collections
with open("F:\Downloads\startup_funding.csv") as file_obj:
    file_data=csv.DictReader(file_obj,skipinitialspace=True)
    dct={}
    for row in file_data:
        year=row["Date dd/mm/yyyy"][-4:]
        if year in dct:
            dct[year]+=1
        else:
            dct[year]=1
    ord_dct=collections.OrderedDict(sorted(dct.items()))
    plt.plot(list(ord_dct.keys()),list(ord_dct.values()))
    plt.xlabel("Year")
    plt.ylabel("Number of Fundings")
    plt.title("Year vs Number of Fundings")
    plt.show
    for i in ord_dct.keys():
        print(i,end=' ')
        print(ord_dct[i])
