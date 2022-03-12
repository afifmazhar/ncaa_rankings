import os
import pandas as pd

team_ratings = pd.read_csv(os.path.join("data", "clean", "team-ratings.csv"))
game_results = pd.read_csv(os.path.join("data", "clean", "game_results_clean.csv"))

bad_names = ["Louisiana State", "Murray State", "Loyola (IL)", "Miami (FL)", "Miami (OH)", "Pennsylvania", "UAB", "Saint Louis", "Saint Joseph's", "Loyola (MD)", "Louisiana", "St. John's (NY)", "Saint Mary's (CA)", "Long Island University", "Middle Tennessee", "Little Rock", "NC State", "Albany (NY)", "Cal Poly", "Nevada-Las Vegas", "UTSA", "Detroit Mercy", "Cal State Long Beach", "Saint Peter's", "UT Arlington"]
good_names = ["LSU", "Murray St.", "Loyola (Ill.)", "Miami (Fla.)", "Miami (Ohio)", "Penn", "Alabama-Birmingham", "St. Louis", "St. Joseph's", "Loyola (Md.)", "Louisiana-Lafayette", "St. John's", "St. Mary's (Cal.)", "Long Island", "Middle Tennessee State", "Arkansas-Little Rock", "North Carolina State", "Albany (N.Y.)", "Cal-Poly", "UNLV", "Texas-San Antonio", "Detroit", "Long Beach State", "St. Peter's", "Texas-Arlington"]

for bad in bad_names:
    team_ratings.loc[team_ratings["team"] == bad, "team"] = good_names[bad_names.index(bad)]

team_ratings = team_ratings.set_index(["team", "year"])
game_results = game_results.set_index(["team1", "year"])

game_results = game_results.assign(
    team1_sos = team_ratings["sos"],
    team1_osrs = team_ratings["osrs"],
    team1_dsrs = team_ratings["dsrs"],
    team1_srs = team_ratings["srs"]
)

game_results = game_results.reset_index()
game_results = game_results.set_index(["team2", "year"])

game_results = game_results.assign(
    team2_sos = team_ratings["sos"],
    team2_osrs = team_ratings["osrs"],
    team2_dsrs = team_ratings["dsrs"],
    team2_srs = team_ratings["srs"]
)

game_results = game_results.reset_index()

game_results.to_csv(os.path.join("data", "clean", "game_results_clean.csv"), index = False)