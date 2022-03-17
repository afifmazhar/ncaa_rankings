import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir("../../")
IN_PATH = os.path.join("data/clean", "game_results_clean.csv")

df = pd.read_csv(IN_PATH)
info = df.loc[:, ["year", "team1", "candidate", "candidatevotes"]]
s_plot = df.plt.scatter(pop, life_exp)
plt.show()
