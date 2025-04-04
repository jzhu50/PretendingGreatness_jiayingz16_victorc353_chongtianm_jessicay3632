import csv
#import pandas as pd
#from datetime import datetime
#import matplotlib.pyplot as plt

"""returns a dictionary of dates and tesla stock prices"""
def tsla_data():
    data = {}
    with open('csvs/tesla_stocks.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['Date']
            stock_price = row['Close']
            data[date] = stock_price
    return data

def tweet_data():
    data = {}
    with open('csvs/all_musk_posts.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['Date']
            # we need to filter the data by date
            tweet = row['Tweet']
            data[date] = tweet
    print(data)
    return data

'''
df = pd.read_csv('./csvs/tesla_stocks.csv')
# datetime.strptime('', '%Y-%m-%d')
df['Date'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
print(df['Date'].head)
df.plot(kind = 'scatter', x = 'Date', y = 'Open')
plt.show()
'''