import csv
from datetime import datetime

# Reads Tesla stock data from csvs/savedTSLA,
# cleans the data, and returns it as a dictionary 
# with dates as keys and stock prices as values
def tesla_data():
    clean = ["[", "]", "\n", '"', "'"]
    dicT = {}
    with open("csvs/savedTSLA", "r") as f:
        data_entries = f.read().split('], [')
        for i in range(len(data_entries)):
            data_entries[i] = data_entries[i].split(', ')
            for c in clean:
                for j in range(len(data_entries[i])):
                    data_entries[i][j] = data_entries[i][j].replace(c, '')
            dicT[data_entries[i][0]] = data_entries[i][1]
    return dicT

# Reads tweet data from csvs/all_musk_posts.csv,
# cleans the data, and returns it as a dictionary
# with dates as keys and tweet content and like count as values
def tweet_data():
    posts_dict = {}
    with open('csvs/all_musk_posts.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['createdAt']
            post_content = row['fullText']
            like_count = row['likeCount']
            if date and post_content:
                posts_dict[date] = post_content, like_count
    return posts_dict