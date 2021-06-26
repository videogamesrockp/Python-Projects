# mean, median, mode, standard deviation
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("data.csv")
f = plt.figure()
f.set_figwidth(16)
f.set_figheight(12)
print(data, "\n")
print("Outliers:")

for i in range(1, len(data.columns)):
    Q1 = data[data.columns[i]].quantile(0.25)
    Q3 = data[data.columns[i]].quantile(0.75)
    IQR = Q3 - Q1
    Q1outlier = Q1 - 1.5 * IQR
    Q3outlier = Q3 + 1.5 * IQR
    for j in range(len(data["Date"])):
        if data.loc[j, data.columns[i]] > Q3outlier or data.loc[j, data.columns[i]] < Q1outlier:
            print(data["Date"][j] + " | " + data.columns[i] + " | " + str(data.loc[j, data.columns[i]]))
    plt.plot(data["Date"], data[data.columns[i]], label = data.columns[i], marker = "o")

plt.legend(loc="upper right", bbox_to_anchor=(0.15, 1.15), ncol=2)

plt.show()