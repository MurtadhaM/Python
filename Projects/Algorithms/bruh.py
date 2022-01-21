
# Author: Murtadha Marzouq
# Date:   12/10/2021
# Time:   12:00 PM
# Assignment: Social Media Analysis
import  pandas as pd
import matplotlib as plt
import seaborn as sns


# Part 1: Loading Data 
dataframe = pd.read_csv('DataSet.csv')
# for sanity check
table = dataframe.head(1)

# selectivly load the data

sns.pairplot(table, hue='RegionName', size=2.5); 
plt.show()
print(table)
