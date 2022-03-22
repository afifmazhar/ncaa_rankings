import os
import pandas as pd

df1 = pd.read_csv(os.path.join("data/clean", "2022_teams.csv"))
df2 = pd.read_csv(os.path.join("data/clean", "team-ratings.csv"))
df2 = df2[df2.year == 2022]
w_names = ["Saint Mary's (CA)", "Louisiana State", "Miami (FL)", "Loyola (IL)", "UAB"]
c_names = ["St. Mary's (Cal.)", "LSU", "Miami (Fla.)", "Loyola (Ill.)", "Alabama-Birmingham"]
for w in w_names:
    df2.loc[df2["team"] == w, "team"] = c_names[w_names.index(w)]
bracket_data = pd.merge(df1, df2[["team", "osrs", "dsrs"]], on = "team",
                        how = "left")
bracket_data.rename(columns = {"osrs_y": "osrs", "dsrs_y": "dsrs"}, inplace = True)
bracket_data.to_csv(os.path.join("data/clean", "bracket_data.csv"), index = False)