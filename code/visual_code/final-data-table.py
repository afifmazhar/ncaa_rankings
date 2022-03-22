# Install Plotly with: pip install plotly==5.6.0

import plotly.graph_objects as pt
import os
import pandas as pd

g_results = pd.read_csv(os.path.join("data", "clean", "winners.csv"), names = ["Game_Num", "Winning_Team"])

winner_table = pt.Figure(data = [pt.Table(header = dict(values = list(g_results.columns), fill_color = "coral", align = "center", font = dict(size = 16)),
cells = dict(values = [g_results["Game_Num"], g_results["Winning_Team"]], fill_color = "lavender", font = dict(size = 11)))]) 

winner_table.show()








