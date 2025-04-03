import csv
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

<<<<<<< HEAD
def tsla_data():
    data = []
    with open('csvs/tesla_stocks.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    print(data)
    return data

def tweet_data():
    data = []
    with open('csvs/musk_quote_tweets.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    print(data)
    return data

if __name__ == '__main__':
    tsla_data()
    #tweet_data()
=======
df = pd.read_csv('./csvs/tesla_stocks.csv')
# datetime.strptime('', '%Y-%m-%d')
df['Date'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
print(df['Date'].head)
df.plot(kind = 'scatter', x = 'Date', y = 'Open')
plt.show()
>>>>>>> 30cb22e2859cc886056dc4215c0bed9003910a8d
