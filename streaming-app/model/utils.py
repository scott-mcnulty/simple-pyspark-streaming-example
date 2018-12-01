import json
import pickle
import random

import pandas as pd

def load_Xy():
	X = pd.read_csv('./data/X.csv')
	y = pd.read_csv('./data/y.csv')
	return X, y

def save_pkl(obj, f, mode='wb'):
	with open(f, mode) as f:
		pickle.dump(obj, f)

def save_json(obj, fname, mode: str = 'w'):
	with open(fname, mode) as f:
		json.dump(obj, f)

def save_records_for_testing(X_df, n=5):
	random_idxs = random.sample(set(X_df.index), n)
	random_X_df = X_df.ix[random_idxs]
	for idx, row in random_X_df.iterrows():
		save_json([row.to_dict()], './test_http_requests/record_{}.json'.format(idx))
	return random_idxs