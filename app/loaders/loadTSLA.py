import pandas as pd

def load():
	df = pd.read_csv('./csvs/tesla_stocks.csv')
	return df

