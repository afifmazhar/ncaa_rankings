import matplotlib.pyplot as plt
import pandas as pd
import os

#os.chdir("../..")
IN_PATH = os.path.join("data/clean", "team-ratings.csv")
df = pd.read_csv(IN_PATH)
s_plot = plt.scatter(x = df.osrs, y = df.dsrs, c = df.conference.astype('category').cat.codes)
plt.xlabel("osrs")
plt.ylabel("dsrs")
plt.title("srs by conference")

#conferences not organized
"""plt.legend(handles = scatter.legend_elements()[0],
           labels = con_names,
           title = "conference")"""
plt.show()
