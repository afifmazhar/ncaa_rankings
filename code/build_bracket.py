import pandas as pd

df = pd.dataframe()


def rating(team):
    """This function takes a string team name as an argument and returns the rating of that team by looking it up in the
    dataframe. The dataframe is must be properly scoped so that the function can access it."""

    rating = df.loc[team, "rating"]
    return rating


def pick_winner(matchup):
    """This function picks the winner of one game by calling rating() on both teams in the matchup. The projected
    winning team is returned. The dataframe reference is hard-coded into the rating() function."""

    if rating(matchup[0]) > rating(matchup[1]):
        return_value = matchup[0]
    else:
        return_value = matchup[1]
    return return_value


def pick_round(game_lower, game_upper):
    """This function picks one round of games by looping over matchup_dict. The upper and lower bounds of game numbers
    for a given round are used as arguments. The winner_dict dictionary is updated to reflect the projected winners of
    the round. There is no return value. The dataframe reference is hard-coded into the rating() function."""

    for i in range(game_lower, game_upper):
        matchup_dict[i] = [winner_dict[(2 * i) - 69], winner_dict[(2 * i) - 68]]

    for i in range(game_lower, game_upper):
        winner_dict[i] = pick_winner(matchup_dict[i])


def pick_bracket():
    """This function generates the entire bracket with successive calls to pick_round. It must be called after the
    play-in games have been picked using pick_round(). There is no argument or return value. The dataframe reference is
    hard-coded into the rating() function."""

    pick_round(5, 37)
    pick_round(37, 53)
    pick_round(53, 61)
    pick_round(61, 65)
    pick_round(65, 67)
    pick_round(67, 68)


if __name__ == '__main__':

    matchup_dict = {}
    winner_dict = {}

    matchup_dict[1] = ["", ""]
    matchup_dict[2] = ["", ""]
    matchup_dict[3] = ["", ""]
    matchup_dict[4] = ["", ""]

    pick_round(1, 5)

    matchup_dict[5] = ["", ""]
    matchup_dict[6] = ["", ""]
    matchup_dict[7] = ["", ""]
    matchup_dict[8] = ["", ""]
    matchup_dict[9] = ["", ""]
    matchup_dict[10] = ["", ""]
    matchup_dict[11] = ["", ""]
    matchup_dict[12] = ["", ""]
    matchup_dict[13] = ["", ""]
    matchup_dict[14] = ["", ""]
    matchup_dict[15] = ["", ""]
    matchup_dict[16] = ["", ""]
    matchup_dict[17] = ["", ""]
    matchup_dict[18] = ["", ""]
    matchup_dict[19] = ["", ""]
    matchup_dict[20] = ["", ""]
    matchup_dict[21] = ["", ""]
    matchup_dict[22] = ["", ""]
    matchup_dict[23] = ["", ""]
    matchup_dict[24] = ["", ""]
    matchup_dict[25] = ["", ""]
    matchup_dict[26] = ["", ""]
    matchup_dict[27] = ["", ""]
    matchup_dict[28] = ["", ""]
    matchup_dict[29] = ["", ""]
    matchup_dict[30] = ["", ""]
    matchup_dict[31] = ["", ""]
    matchup_dict[32] = ["", ""]
    matchup_dict[33] = ["", ""]
    matchup_dict[34] = ["", ""]
    matchup_dict[35] = ["", ""]
    matchup_dict[36] = ["", ""]

    pick_bracket()
