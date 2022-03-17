import os
import pandas as pd
import matplotlib.pyplot as plt


"""cd ~/ncaa_rankings"""

g_results = pd.read_csv(os.path.join('data', 'clean', 'game_results_clean.csv'))

print(g_results)

plt.scatter(g_results.team1_srs, g_results.team2_srs)
plt.xlabel('Team1 SRS')
plt.ylabel('Team2 SRS')
plt.title('SRS Correlation')
plt.show()


