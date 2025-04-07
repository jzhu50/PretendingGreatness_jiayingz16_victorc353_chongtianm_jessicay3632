import csv
#import pandas as pd
from datetime import datetime
#import matplotlib.pyplot as plt

def aaaaa():
    ass = ["[", "]", "\n", '"', "'"]
    dicT = {}
    with open("csvs/savedTSLA") as f:
        bruh = f.read().split('], [')
        for i in range(len(bruh)):
            bruh[i] = bruh[i].split(', ')
            for c in ass:
                for j in range(len(bruh[i])):
                    bruh[i][j] = bruh[i][j].replace(c, '')
            dicT[bruh[i][0]] = bruh[i][1]
            # bruh[i][0] = datetime.strptime(bruh[i][0], "%Y-%m-%d %H:%M:%S")
            #tmp = bruh[i][1]
            #bruh[i][1] = bruh[i][0]
            #bruh[i][0] = tmp
    return dicT
   

"""
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
"""
