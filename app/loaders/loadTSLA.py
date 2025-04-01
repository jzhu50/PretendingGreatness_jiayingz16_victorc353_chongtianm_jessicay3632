import pandas as pd

def load():
	df = pd.read_csv('./csvs/tsla_2025.csv')
	return df

