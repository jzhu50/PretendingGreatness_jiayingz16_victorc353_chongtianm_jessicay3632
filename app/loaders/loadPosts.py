import pandas as pd

def load():
	df = pd.read_csv('./csvs/all_musk_posts.csv')
	return df
