import csv
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('./csvs/tesla_stocks.csv')
# datetime.strptime('', '%Y-%m-%d')
df['Date'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
print(df['Date'].head)
df.plot(kind = 'scatter', x = 'Date', y = 'Open')
plt.show()
