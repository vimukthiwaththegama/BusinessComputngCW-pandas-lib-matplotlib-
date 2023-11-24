import pandas as pd  # import the pandas library
import matplotlib.pyplot as plt # import matplotlib.pyplot
df=pd.read_csv("recent-grads.csv")

df.plot(kind='scatter',x='Median',y ='Unemployed') # two scatter plots to analyse Median and Unemployment
df.plot(kind='scatter',x='Median',y='Unemployment_rate')
plt.show()

Median_above_60000 = df[df["Median"] > 60000] # bar plot for compare earnings between majors
Median_above_60000.set_index("Major")[["P25th", "Median", "P75th"]].plot(kind="bar", figsize=(12,8))
plt.title("",rotation=0)
plt.ylabel("Earnings")
plt.tight_layout()
plt.show()


