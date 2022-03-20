import pandas as pd

df = pd.dataframe()
matchup_dict = {}
winner_dict = {}
region_dict = {1: "west", 2: "east", 3: "midwest", 4: "south"}


def rating(team):
    """This function takes a string team name as an argument and returns the rating of that team by looking it up in the
    dataframe. The dataframe is must be properly scoped so that the function can access it."""

    rating = df.loc[team, "rating"]
    return rating


def pick_winner(matchup):
    """This function picks the winner of one game by calling rating() on both teams in the matchup. The projected
    winning team is returned."""

    if rating(matchup[0]) > rating(matchup[1]):
        return_value = matchup[0]
    else:
        return_value = matchup[1]
    return return_value


def pick_round(game_lower, game_upper):
    """This function picks one round of games by looping over matchup_dict. The upper and lower bounds of game numbers
    for a given round are used as arguments. The winner_dict dictionary is updated to reflect the projected winners of
    the round. There is no return value."""

    for i in range(game_lower, game_upper):
        matchup_dict[i] = [winner_dict[(2 * i) - 69], winner_dict[(2 * i) - 68]]

    for i in range(game_lower, game_upper):
        winner_dict[i] = pick_winner(matchup_dict[i])


def build_bracket():
    """This function builds up the play-in bracket, picks the play-in winners using pick_round, and builds up the main
    bracket. There is no argument or return value. The dataframe is must be properly scoped so that the function can
    access it."""

    matchup_dict[1] = df.index[(df["region" == region_dict[1]]) & (df["seed" == 11])].tolist()
    matchup_dict[2] = df.index[(df["region" == region_dict[2]]) & (df["seed" == 12])].tolist()
    matchup_dict[3] = df.index[(df["region" == region_dict[3]]) & (df["seed" == 16])].tolist()
    matchup_dict[4] = df.index[(df["region" == region_dict[4]]) & (df["seed" == 16])].tolist()

    pick_round(1, 5)

    matchup_dict[9] = [df.index[(df["region" == region_dict[1]]) & (df["seed" == 6])], winner_dict[1]]
    matchup_dict[15] = [df.index[(df["region" == region_dict[2]]) & (df["seed" == 5])], winner_dict[2]]
    matchup_dict[21] = [df.index[(df["region" == region_dict[3]]) & (df["seed" == 1])], winner_dict[3]]
    matchup_dict[29] = [df.index[(df["region" == region_dict[4]]) & (df["seed" == 1])], winner_dict[4]]

    list1 = [1, 8, 5, 4, 6, 3, 7, 2]

    for i in list1:
        for n in range(1, 5):
            if (n == 1 and i == 6) or (n == 2 and i == 5) or (n == 3 and i == 1) or (n == 4 and i == 1):
                continue
            else:
                matchup_dict[list1.index(i) + 5 + ((n - 1) * 8)] = \
                    [df.index[(df["region" == region_dict[n]]) & (df["seed" == i])],
                     df.index[(df["region" == region_dict[n]]) & (df["seed" == (17 - i)])]]


def pick_bracket():
    """This function fills out entire bracket with successive calls to pick_round. It must be called after
    build_bracket. There is no argument or return value."""

    pick_round(5, 37)
    pick_round(37, 53)
    pick_round(53, 61)
    pick_round(61, 65)
    pick_round(65, 67)
    pick_round(67, 68)


if __name__ == '__main__':

    build_bracket()
    pick_bracket()
