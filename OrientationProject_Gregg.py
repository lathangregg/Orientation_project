import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_excel('Orientation_project/MSDS-Orientation-Computer-Survey.xlsx')
print(df)
#drop rows where ram is above 64
df = df[df['RAM (in GB)'] <= 64]
#create a histogram of RAM with bin size of 8
df['RAM (in GB)'].plot.hist(bins=8)
plt.Color = 'red'
#add an x label
plt.xlabel('RAM (in GB)')
#add a title
plt.title('RAM (in GB) Histogram')
plt.show()