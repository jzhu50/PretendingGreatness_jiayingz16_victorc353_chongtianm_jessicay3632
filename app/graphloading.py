import csv
#import pandas as pd
#from datetime import datetime
#import matplotlib.pyplot as plt

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
    posts_dict = {}
    with open('app/csvs/all_musk_posts.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['createdAt']
            post_content = row['fullText']
            if date and post_content:  # only include if both exist
                posts_dict[date] = post_content
    return posts_dict

if __name__ == '__main__': 
    print(tweet_data())