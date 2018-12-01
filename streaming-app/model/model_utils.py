import numpy as np

def rmse(ytrue, yhat):
	return np.sqrt(np.mean((ytrue - yhat) ** 2))