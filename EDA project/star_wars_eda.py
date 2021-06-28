# import libraries
import pandas as pd
from matplotlib import pyplot as plt
import math

# variables
data = pd.read_csv("star_wars.csv")
f = plt.figure()
f.set_figwidth(16)
f.set_figheight(12)
list = []

# For loop for each column of the csv file
for i in range(1, len(data.columns)):
    # Resetting variables
    Q1 = data[data.columns[i]].quantile(0.25)
    Q3 = data[data.columns[i]].quantile(0.75)
    median = data[data.columns[i]].quantile(0.5)
    total = 0
    variance = 0
    IQR = Q3 - Q1
    Q1outlier = Q1 - 1.5 * IQR
    Q3outlier = Q3 + 1.5 * IQR
    print("Outliers for " + data.columns[i] + ":")
    # Add title and axis names
    plt.title("Star Wars Character Searches by Month")
    plt.xlabel("Date")
    plt.ylabel("Topic's search proportion to all topics on Google")
    for j in range(len(data["Date"])): #For loop going through each date in the columns
        list.append(data.loc[j, data.columns[i]])
        total+=data.loc[j, data.columns[i]] # Calculating total for mean
        #Printing outliers
        if data.loc[j, data.columns[i]] > Q3outlier or data.loc[j, data.columns[i]] < Q1outlier:
            print(data["Date"][j] + " | " + data.columns[i] + " | " + str(data.loc[j, data.columns[i]]))
    #Printing stats and additional calculating
    print("Median for " + data.columns[i] + " is " + str(median))
    mean=total/len(data["Date"])
    print("Mean for " + data.columns[i] + " is " + str(mean))
    for j in range(len(data["Date"])):
        variance += (data.loc[j, data.columns[i]] - mean) ** 2
    standarddeviation = math.sqrt(variance/len(data["Date"]))
    print("The standard deviation for " + data.columns[i] + " is " + str(standarddeviation) + "\n")
    #Plotting the data!
    plt.plot(data["Date"], data[data.columns[i]], label = data.columns[i], marker = "o")

#Printing the table
print(data, "\n")
# Setting legends for the lines
plt.legend(loc="upper right", bbox_to_anchor=(0.15, 1.15), ncol=2)


#Creating plot figure
fig = plt.figure(figsize=(16, 12))

# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
ax = plt.subplot()
ax.set_title("Star Wars Character Searches Boxplot")
ax.set_ylabel("Topic's search proportion to all topics on Google")
ax.boxplot(list)

# show plot
plt.show()
