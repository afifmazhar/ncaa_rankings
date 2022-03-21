import pandas as pd
import os

df_full = (
    pd.read_csv("/data/raw/score_seed_data_dirty.csv", encoding="ISO-8859-1")
    .rename(columns=str.lower)
    .rename(columns={"yearê":"year","roundê":"round"})
    .drop(index = range(1684,2251))
)
df_full["score_diff"] = df_full["score1"].sub(df_full["score2"], axis=0)
df_full["seed_diff"] = df_full["seed1"].sub(df_full["seed2"], axis=0)


df_full.to_csv(os.path.join("data", "clean", "game_results_clean.csv"), index = False)

