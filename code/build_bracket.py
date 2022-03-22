import pandas as pd
import csv
import os

INPUT_DIR = os.path.join("data", "clean")
OUTPUT_DIR = os.path.join("data", "clean")


df = pd.read_csv(os.path.join(INPUT_DIR, "bracket_data.csv"), index_col="team")
matchup_dict = {}
winner_dict = {}
region_dict = {1: "west", 2: "east", 3: "midwest", 4: "south"}


with open(os.path.join(INPUT_DIR, "coefficients.csv"), 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        coef_dict = dict(row)


def pick_winner(matchup):
    """This function picks the winner of one game by applying the coefficients from the regression to each team's ratings. The projected
    winning team is returned as a string."""

    if (df.at[matchup[1], "seed"] - df.at[matchup[0], "seed"]) * float(coef_dict['seed_diff']) + \
            df.at[matchup[0], "osrs"] * float(coef_dict["osrs_avg"]) - \
            df.at[matchup[1], "osrs"] * float(coef_dict["osrs_avg"]) + \
            df.at[matchup[0], "dsrs"] * float(coef_dict["dsrs_avg"]) - \
            df.at[matchup[1], "dsrs"] * float(coef_dict["dsrs_avg"]) > 0:
        return_value = matchup[0]
    else:
        return_value = matchup[1]
    return return_value


def build_round(game_lower, game_upper):
    """This function builds up matchups for a given round based on the upper and lower bounds of game numbers for a
    given round are used as arguments. There is no return value."""

    for i in range(game_lower, game_upper):
        matchup_dict[i] = [winner_dict[(2 * i) - 69], winner_dict[(2 * i) - 68]]


def pick_round(game_lower, game_upper):
    """This function picks one round of games by looping over matchup_dict. The upper and lower bounds of game numbers
    for a given round are used as arguments. The winner_dict dictionary is updated to reflect the projected winners of
    the round. There is no return value."""

    for i in range(game_lower, game_upper):
        winner_dict[i] = pick_winner(matchup_dict[i])


def build_bracket():
    """This function builds up the play-in bracket, picks the play-in winners using pick_round, and builds up the main
    bracket. There is no argument or return value. The dataframe is must be properly scoped so that the function can
    access it."""

    matchup_dict[1] = [df.index[(df["region"] == region_dict[1]) & (df['seed'] == 11)].values[0],
                       df.index[(df["region"] == region_dict[1]) & (df['seed'] == 11)].values[1]]
    matchup_dict[2] = [df.index[(df["region"] == region_dict[2]) & (df['seed'] == 12)].values[0],
                       df.index[(df["region"] == region_dict[2]) & (df['seed'] == 12)].values[1]]
    matchup_dict[3] = [df.index[(df["region"] == region_dict[3]) & (df['seed'] == 16)].values[0],
                       df.index[(df["region"] == region_dict[3]) & (df['seed'] == 16)].values[1]]
    matchup_dict[4] = [df.index[(df["region"] == region_dict[4]) & (df['seed'] == 16)].values[0],
                       df.index[(df["region"] == region_dict[4]) & (df['seed'] == 16)].values[1]]

    pick_round(1, 5)

    matchup_dict[9] = [df.index[(df["region"] == region_dict[1]) & (df['seed'] == 6)].values[0], winner_dict[1]]
    matchup_dict[15] = [df.index[(df["region"] == region_dict[2]) & (df['seed'] == 5)].values[0], winner_dict[2]]
    matchup_dict[21] = [df.index[(df["region"] == region_dict[3]) & (df['seed'] == 1)].values[0], winner_dict[3]]
    matchup_dict[29] = [df.index[(df["region"] == region_dict[4]) & (df['seed'] == 1)].values[0], winner_dict[4]]

    list1 = [1, 8, 5, 4, 6, 3, 7, 2]

    for i in list1:
        for n in range(1, 5):
            if not ((n == 1 and i == 6) or (n == 2 and i == 5) or (n == 3 and i == 1) or (n == 4 and i == 1)):
                matchup_dict[list1.index(i) + 5 + ((n - 1) * 8)] = \
                    [df.index[(df["region"] == region_dict[n]) & (df['seed'] == i)].values[0],
                     df.index[(df["region"] == region_dict[n]) & (df['seed'] == (17 - i))].values[0]]


def pick_bracket():
    """This function fills out entire bracket with successive calls to pick_round. It must be called after
    build_bracket. There is no argument or return value."""

    pick_round(5, 37)
    build_round(37, 53)
    pick_round(37, 53)
    build_round(53, 61)
    pick_round(53, 61)
    build_round(61, 65)
    pick_round(61, 65)
    build_round(65, 67)
    pick_round(65, 67)
    build_round(67, 68)
    pick_round(67, 68)


if __name__ == '__main__':

    build_bracket()
    pick_bracket()

    with open(os.path.join(OUTPUT_DIR, "winners.csv"), 'w') as file:
        for key in winner_dict.keys():
            file.write("%s, %s\n" % (key, winner_dict[key]))

    with open(os.path.join(OUTPUT_DIR, "matchups.csv"), 'w') as file:
        for key in matchup_dict.keys():
            file.write("%s, %s\n" % (key, matchup_dict[key]))
