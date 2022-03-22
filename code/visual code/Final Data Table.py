# Install PrettyTable with: pip install PrettyTable.

from prettytable import PrettyTable as pt
import os
import pandas as pd

g_results = pd.read_csv(os.path.join('data', 'clean', 'game_results_clean.csv'))

mmad_tabe = pt(['a', 'b', 'c'])
mmad_tabe.add_row(g_results[])

print(mmad_tabe)


