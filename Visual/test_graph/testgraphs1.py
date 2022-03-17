import os
from tkinter import font as ft
import pandas as pd
import matplotlib.pyplot as plt


"""cd ~/ncaa_rankings"""

g_results = pd.read_csv(os.path.join('data', 'clean', 'game_results_clean.csv'))

print(g_results)

srscorr = plt.scatter(g_results.team1_srs, g_results.team2_srs, color = 'brown')
plt.xlabel('Team1 SRS')
plt.ylabel('Team2 SRS')
plt.title('SRS Correlation')
plt.show()


rpicorr = plt.scatter(g_results.team1_rpi, g_results.team1_rpi, color = 'blue')
plt.xlabel('Team1 RPI')
plt.ylabel('Team2 RPI')
plt.title('RPI Correlation')
plt.show()
