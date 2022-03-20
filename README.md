# ncaa_rankings
Data Analysis Project for NCAA rankings

Project Description:
This project uses historical team rankings and tournament performance
 to create a new team ranking to predict the outcome of march madness 2022.

Data:
The ranking data used is SRS Team Ratings and RPI team ratings from 1994 to 2019.
The game data used is all March Madness games from 1994 to 2019.

Cleaning:
Data sets are cleaned and combined, matching team names to their ratings for each historical
 March Madness game.

Final CSV format:
year,round,team1,seed1,score1,team2,seed2,score2,score_diff,SRS1,RPI1,SRS2,RPI2

Analysis:
Once every team in every historical game is associated with its two ratings in each given year,
 we use an OLS regression where score differential is regressed on the SRS and RPI of teams one
 and two.

pts_team1 - pts_team2 = b0 + b1(SRS1) + b2(SRS2) + b3(RPI1) + b4(RPI2) + e

This will give us the proper weighting of SRS and RPI for our own rankings.
The formula for our rating will be as follows: rank_team1 = b1(SRS1) + b3(RPI1)

Once we have our formula, all 2022 March Madness teams will have their SRS and RPI run through
 the formula so that we can determine each teams ranking.

We predict that in any given matchup the team with the higher ranking will win and that the team
 with the highest overall ranking will win the tournament.
