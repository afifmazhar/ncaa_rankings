import os
import pandas as pd

team_ratings = pd.read_csv(os.path.join("data", "clean", "rpi_clean_1994_2019.csv"))
game_results = pd.read_csv(os.path.join("data", "clean", "game_results_clean.csv"))

## removes several header lines throughout the data that shouldn't be there
team_ratings = team_ratings[team_ratings.team != "School"]

## rpi data is not consitent year to year in team names - lots of mismatches
bad_names = ["Michigan St", "Murray St", "Mississippi St", "Florida St", "UAB", "Oklahoma St", "Saint Louis", "Washington St", "UCF", "Loyola (Maryland)", "Pennsylvania", "New Mexico St", "Boise St", "Coll of Charleston", "Kansas St", "VCU", "Utah St", "Arizona St", "NCCU", "Miami (OH)", "BYU", "UW Green Bay", "Wis-Green Bay", "North Dakota St", "St. Mary's", "Georgia St", "Texas St", "SW Texas St", "Hawai'i", "Tennessee St", "Loyola (Chicago)", "Loyola-Chicago", "MD-Baltimore Co", "UMBC", "Wichita St", "UMass", "UConn", "Miami-Ohio", "Prairie View A&M", "CS Fullerton", "Florida Intl", "Weber St", "Nicholls St", "Miami (FL)", "Miami-Florida", "Middle Tenn St", "SMU", "UNC Charlotte", "Western Michigan", "Wright St", "San Diego St", "South Dakota St", "North Carolina St", "George Wash", "Northern Illinois", "UL Monroe", "LA-Monroe", "Mt St. Mary's", "Ark-Little Rock", "UA Little Rock", "Little Rock", "Oregon St", "Saint Joseph's", "Albany", "Cal Poly", "Colorado St", "Miss Valley St", "TX-San Antonio", "UT San Antonio", "Ark-Pine Bluff", "UA Pine Bluff", "Morehead St", "UW Milwaukee", "Wis-Milwaukee", "Central Mich", "Southern Ill", "Kent", "Kent St", "USC", "Southern Cal", "Missouri St", "SW Missouri St", "Western Mich", "Jacksonville St", "East Tenn St", "Montana St", "San Jose St", "Western Car", "Northern Ill", "Fresno St", "CS Bakersfield", "Southern U", "Northwestern St", "Norfolk St", "Charleston So", "Eastern Mich", "South Carolina St", "Long Beach", "Southern Miss", "Boston U", "Indiana St", "Alabama St", "Morgan St", "Jackson St", "Coppin St", "Illinois St", "Sam Houston", "Cleveland St", "Portland St", "Delaware St", "Central Connecticut", "Central Conn", "McNeese St", "Alcorn St", "Appalachian St", "SE Missouri St", "Arkansas St", "CS-Northridge", "CS Northridge", "Northern Ariz", "Illinois-Chi", "Western Ky", "LA-Lafayette", "UL Lafayette", "UL-Lafayette", "Eastern Ill", "Florida Atl", "Troy St", "Eastern Wash", "SE Louisiana", "TAMU-CC", "UT Arlington"]
good_names = ["Michigan State", "Murray St.", "Mississippi State", "Florida State", "Alabama-Birmingham", "Oklahoma State", "St. Louis", "Washington State", "Central Florida", "Loyola (Md.)", "Penn", "New Mexico State", "Boise State", "College of Charleston", "Kansas State", "Virginia Commonwealth", "Utah State", "Arizona State", "North Carolina Central", "Miami (Ohio)", "Brigham Young", "Green Bay", "Green Bay", "North Dakota State", "St. Mary's (Cal.)", "Georgia State", "Texas State", "Texas State", "Hawaii", "Tennessee State", "Loyola (Ill.)", "Loyola (Ill.)", "Maryland-Baltimore County", "Maryland-Baltimore County", "Wichita State", "Massachusetts", "Connecticut", "Miami (Ohio)", "Prairie View", "Cal State Fullerton", "Florida International", "Weber State", "Nicholls State", "Miami (Fla.)", "Miami (Fla.)", "Middle Tennessee State", "Southern Methodist", "Charlotte", "Western Michigan", "Wright State", "San Diego State", "South Dakota State", "North Carolina State", "George Washington", "Northern Illinois", "Louisiana-Monroe", "Louisiana-Monroe", "Mount St. Mary's", "Arkansas-Little Rock", "Arkansas-Little Rock", "Arkansas-Little Rock", "Oregon State", "St. Joseph's", "Albany (N.Y.)", "Cal-Poly", "Colorado State", "Mississippi Valley State", "Texas-San Antonio", "Texas-San Antonio", "Arkansas-Pine Bluff", "Arkansas-Pine Bluff", "Morehead State", "Milwaukee", "Milwaukee", "Central Michigan", "Southern Illinois", "Kent State", "Kent State", "Southern California", "Southern California", "Missouri State", "Missouri State", "Western Michigan", "Jacksonville State", "East Tennessee State", "Montana State", "San Jose State", "Western Carolina", "Northern Illinois", "Fresno State", "Cal State Bakersfield", "Southern", "Northwestern State", "Norfolk State", "Charleston Southern", "Eastern Michigan", "South Carolina State", "Long Beach State", "Southern Mississippi", "Boston University", "Indiana State", "Alabama State", "Morgan State", "Jackson State", "Coppin State", "Illinois State", "Sam Houston State", "Cleveland State", "Portland State", "Delaware State", "Central Connecticut State", "Central Connecticut State", "McNeese State", "Alcorn State", "Appalachian State", "Southeast Missouri State", "Arkansas State", "Cal State Northridge", "Cal State Northridge", "Northern Arizona", "Illinois-Chicago", "Western Kentucky", "Louisiana-Lafayette", "Louisiana-Lafayette", "Louisiana-Lafayette", "Eastern Illinois", "Florida Atlantic", "Troy", "Eastern Washington", "Southeastern Louisiana", "Texas A&M-Corpus Christi", "Texas-Arlington"]

for bad in bad_names:
    team_ratings.loc[team_ratings["team"] == bad, "team"] = good_names[bad_names.index(bad)]

## create same index for each dataframe in order to add columns to games data
team_ratings = team_ratings.set_index(["team", "year"])
game_results = game_results.set_index(["team1", "year"])

game_results = game_results.assign(team1_rpi = team_ratings["rpi"])

## reset and do the same for team 2
game_results = game_results.reset_index()
game_results = game_results.set_index(["team2", "year"])

game_results = game_results.assign(team2_rpi = team_ratings["rpi"])

## rearrange the columns before saving updated csv
game_results = game_results.reset_index()
game_results = game_results[["year", "round", "team1", "team2", "score1", "score2", "score_diff", "seed1", "seed2", "seed_diff", "team1_sos", "team1_osrs", "team1_dsrs", "team1_srs", "team1_rpi", "team2_sos", "team2_osrs", "team2_dsrs", "team2_srs", "team2_rpi"]]

game_results.to_csv(os.path.join("data", "clean", "game_results_clean.csv"), index = False)