#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
df = pd.read_csv('Test graph.csv')

#All Variable
x = df['Country']
y = df['Percentage of popularity']

#Bar Chart
plt.xlabel('Country', fontsize=10)
plt.ylabel('Percentage', fontsize=10)
plt.bar(x, y)

plt.show()