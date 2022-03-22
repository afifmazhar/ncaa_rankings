# Install Plotly with: pip install plotly==5.6.0

import plotly.graph_objects as pt
import os
import pandas as pd

m_results = pd.read_csv(os.path.join("data", "clean", "matchups.csv"), names = ["Game_Num", "Matched_Teams1", "Matched_Teams2"])

winner_table = pt.Figure(data = [pt.Table(header = dict(values = list(m_results.columns), fill_color = "cyan", align = "center", font = dict(size = 16)),
cells=dict(values = [m_results["Game_Num"], m_results["Matched_Teams1"], m_results["Matched_Teams2"]], fill_color = "lavender", font = dict(size = 11)))])

winner_table.show()
