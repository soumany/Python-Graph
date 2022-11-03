import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
df = pd.read_csv('Test graph.csv')

#All Variable
x = df['Country']
x_indexes = np.arange(len(x))
width = 0.25

y = df['Percentage of popularity']
plt.bar(x_indexes - width  ,y, width = width ,  color="#e5ae38", label ="Popularity")

safe_y = df['Percentage of safty']
plt.bar(x_indexes ,safe_y, width = width,  color="#008fd5", label ="Safety")

#Bar Chart
plt.legend()

plt.xticks(ticks = x_indexes, labels = x)
plt.title('Top 10 countries of Quality of Life', fontsize=13)
plt.xlabel('Country', fontsize=13)
plt.ylabel('Percentage', fontsize=13)
#plt.bar(x, y)

plt.tight_layout()
plt.show()