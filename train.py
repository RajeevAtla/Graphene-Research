import pandas as pd
import numpy as np

import xgboost as xgb
from xgboost import DMatrix

import sklearn
from sklearn.model_selection import train_test_split

import data_import
exec(open('data_analyze_prelim.py').read())

train_data, test_data = train_test_split(data)

dtrain = DMatrix(train_data, train_data["Superconductivity Type"])
dtest = DMatrix(test_data, test_data["Superconductivity Type"])

param = {'max_depth': 10, 'eta': 0.1, 'objective': 'reg:squarederror'}

param['eval_metric'] = 'error'

epochs = 100

evallist = [(dtrain, 'eval'), (dtest, 'train')]

bst = xgb.train(param, dtrain, epochs, evallist)
