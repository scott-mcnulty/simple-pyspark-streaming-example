import pandas as pd

from model.app_utils import load_pkl

model = load_pkl('./model/assets/model.pkl')

def parse(data: dict):
	return pd.DataFrame([data])

def predict(data: dict):
	X = parse(data)
	return model.predict(X)[0]