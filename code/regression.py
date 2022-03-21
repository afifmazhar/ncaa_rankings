import pandas as pd
import sklearn as sk
import os
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

game_results = pd.read_csv("../data/clean/game_results_clean.csv", encoding="ISO-8859-1")

## linear regression with score_diff being the y variable and the others being x variables
x = game_results[['team1_osrs','team1_dsrs','team2_osrs','team2_dsrs','seed_diff']]
y = game_results['score_diff']

## creates the regression
regr = LinearRegression(fit_intercept=False).fit(x,y)

##create averages
osrs_avg = (regr.coef_[0] - regr.coef_[2])/2
dsrs_avg = (regr.coef_[1] - regr.coef_[3])/2
seed_diff = regr.coef_[4]

##export coefficients
coefficients = {'seed_diff':[seed_diff], 'osrs_avg':[osrs_avg],'dsrs_avg':[dsrs_avg]}
df = pd.DataFrame(data=coefficients)

df.to_csv(os.path.join("..","data", "clean", "coefficients.csv"), index = False)