import pandas as pd

def load():
	df = pd.read_csv('./csvs/musk_quote_tweets.csv')
	return df
