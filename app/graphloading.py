import csv

def tsla_data():
    data = []
    with open('csvs/app/csvs/tesla_stocks.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    print(data)
    return data

def tweet_data():
    data = []
    with open('csvs/app/csvs/musk_quote_tweets.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    print(data)
    return data