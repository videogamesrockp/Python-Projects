import pandas as pd
import matplotlib.pyplot as plt
import math

data=pd.read_csv("student_grades.csv")
Q1=data[data.columns[0]].quantile(0.25)
Q3=data[data.columns[0]].quantile(0.75)
IQR = Q3-Q1
total=0
variance = 0
dict={}
for i in range(len(data[data.columns[0]])):
    dict[data.loc[i, data.columns[0]] - (data.loc[i, data.columns[0]] % 10)] = 0
    total+=data.loc[i,data.columns[0]]
print("The mean is: " + str(total/len(data[data.columns[0]])))
print("The median is: " + str(data[data.columns[0]].quantile(0.5)))
print("The mode is: " + str(data[data.columns[0]].mode().iat[0]))
for i in range(len(data[data.columns[0]])):
    variance += (data.loc[i, data.columns[0]] - total/len(data[data.columns[0]])) ** 2
print("The standard deviation is: " + str(math.sqrt(variance/len(data[data.columns[0]]))))
print("Outliers:")
for i in range(len(data[data.columns[0]])):
    if data.loc[i,data.columns[0]] > Q3 + 1.5 * IQR or data.loc[i,data.columns[0]] < Q1 - 1.5 * IQR:
        print(data.loc[i,data.columns[0]], end = ",")
    for j in dict:
        if data.loc[i, data.columns[0]] >= j and data.loc[i, data.columns[0]] <= j+10:
            dict[j]=dict[j]+1
list=list(dict)
list.sort()
for i in list:
    plt.bar(str(i)+"-"+str(i+10), dict[i])

plt.xlabel("Grade ranges")
plt.ylabel("Number of students")
plt.title("Student grade ranges")

plt.show()
