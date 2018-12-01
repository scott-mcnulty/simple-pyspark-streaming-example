# model

## Create an analytic dataset, train a random forest regression model, and save the model for later use

Run `python3 create_assets.py` to create an analytic dataset and leave out a small, random sample of records for testing the scoring/prediction API. After you've created your dataset, run `python3 train.py` to train and save a simple `sklearn.ensemble.RandomForestRegressor` model.