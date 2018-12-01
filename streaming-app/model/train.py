from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from utils import load_Xy, save_pkl
from model_utils import rmse

RANDOM_STATE = 100

if __name__ == '__main__':

	X, y = load_Xy()
	y = y.values.ravel()
	X = X.values

	Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=RANDOM_STATE)

	model = RandomForestRegressor(random_state=RANDOM_STATE)

	model.fit(Xtrain, ytrain)

	yhat = model.predict(Xtest)

	print('Test - Root Mean Square Error: {}'.format(rmse(ytest, yhat)))

	save_pkl(model, './assets/model.pkl')