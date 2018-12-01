'''
Transform raw data into a complete analytic dataset, for use in later model-training steps.

For the purposes of this example, `create_assets.py` will be fairly simple.
In more complex use cases, you might define one-hot-encoding, imputation, and other
logic in order to transform raw data into your desired analytic dataset.
'''

from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

from utils import save_records_for_testing

if __name__ == '__main__':

	boston_obj = load_boston()

	all_data = np.hstack((boston_obj.data, boston_obj.target.reshape(-1, 1)))

	df = pd.DataFrame(data=all_data, columns=list(boston_obj.feature_names) + ['price'])

	# Rows to exclude for pure testing of the model API
	X_df = df[boston_obj.feature_names]
	random_idxs = save_records_for_testing(X_df)

	df = df[~df.index.isin(random_idxs)]
	
	X_df = df[sorted(boston_obj.feature_names)]
	y_df = df['price']

	X_df.to_csv('./data/X.csv', index=False, header=True)
	y_df.to_csv('./data/y.csv', index=False, header=True)