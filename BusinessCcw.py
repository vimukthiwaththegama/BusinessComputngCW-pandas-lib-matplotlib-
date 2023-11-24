import pandas as pd  # import the pandas library
import matplotlib.pyplot as plt # import matplotlib.pyplot

df = pd.read_csv("anscombe.csv")  # import/load the anscombe.csv file

df1 = df[["x1", "y1"]]  # four data frames (df1, df2, df3, df4) to
df2 = df[["x2", "y2"]]  # store the four data sets in anscombe.csv file
df3 = df[["x3", "y3"]]
df4 = df[["x4", "y4"]]

df1dEscrptive_statistics = df1.describe()  # basic descriptive statistics
df2dEscrptive_statistics = df2.describe()  # of df1,df2,df3 and df4
df3dEscrptive_statistics = df3.describe()
df4dEscrptive_statistics = df4.describe()

print("\n",df1dEscrptive_statistics)  # display above those created basic descriptive statistics
print("\n",df2dEscrptive_statistics)
print("\n",df3dEscrptive_statistics)
print("\n",df4dEscrptive_statistics)

df1.plot(kind='scatter',x='x1',y ='y1') # scatter plot for each data set(df1,df2,df3,df4)
df2.plot(kind='scatter',x='x2',y ='y2')
df3.plot(kind='scatter',x='x3',y ='y3')
df4.plot(kind='scatter',x='x4',y ='y4')

plt.show()