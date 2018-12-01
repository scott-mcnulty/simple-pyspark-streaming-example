import sys
import logging
import pickle

from model.app_config import LOGGER_NAME

def create_logger():

	logging_format = u'%(asctime)s - %(name)s - %(levelname)s - %(message)s'

	logging.basicConfig(
		level=logging.DEBUG,
		filename='./logs/{}.log'.format(LOGGER_NAME),
		filemode='w',
		format=logging_format
	)

	logger = logging.getLogger(LOGGER_NAME)

	formatter = logging.Formatter(logging_format)
	stdout = logging.StreamHandler(sys.stdout)
	stdout.setLevel(logging.INFO)
	stdout.setFormatter(formatter)
	logger.addHandler(stdout)

	return logger

def load_pkl(f, mode='rb'):
	return pickle.load(open(f, mode))