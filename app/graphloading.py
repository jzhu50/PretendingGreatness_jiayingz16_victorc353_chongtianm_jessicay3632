import csv
from datetime import datetime

def tesla_data():
    clean = ["[", "]", "\n", '"', "'"]
    dicT = {}
    with open("app/csvs/savedTSLA", "r") as f:
        bruh = f.read().split('], [')
        for i in range(len(bruh)):
            bruh[i] = bruh[i].split(', ')
            for c in clean:
                for j in range(len(bruh[i])):
                    bruh[i][j] = bruh[i][j].replace(c, '')
            dicT[bruh[i][0]] = bruh[i][1]
    return dicT
   
def tweet_data():
    posts_dict = {}
    with open('app/csvs/all_musk_posts.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['createdAt']
            post_content = row['fullText']
            like_count = row['likeCount']
            if date and post_content:
                posts_dict[date] = post_content, like_count
    return posts_dict