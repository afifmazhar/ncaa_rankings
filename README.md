# ncaa_rankings
Data Analysis Project for NCAA rankings

**Goal of the Analysis:**

The goal of this analysis is to create a NCAA team ranking system that is more accurate than the ranking systems currently in use.

**Project Description:**

This project uses historical team rankings and historical tournament performance to weight the importance of various team rankings and thereby create a new hybrid team ranking system to predict the outcome of March Madness 2022.

**Data:**

_summarize the documentation of the data, make sure that you understand and document all columns/features that are relevant to your analysis. You should understand and summarize what isn’t in the data too._

The ranking data used is SRS Team Ratings and RPI team ratings from 1994 to 2019. This data was downloaded from - https://www.sports-reference.com/cbb/seasons/2022-ratings.html & 

The game data used is all March Madness games from 1994 to 2019. This data was downloaded from - LINK

**Limitations of Data:**

Our data is limited by the fact that it conatains only team metrics.
This data would be more accurate and comprehensive if it included information about individual players and injuries.

**Cleaning:**

Data sets are cleaned of erroneous lines, hyperlinks, and superflous columns.
Data frames are then merged, matching team names to their ratings for each historical March Madness game.
The cleaned and merged CSV will follow the format - year,round,team1,seed1,score1,team2,seed2,score2,score_diff,SRS1,RPI1,SRS2,RPI2

**Analysis & Methodology:**

Once every team in every historical game is associated with its two ratings in each given year, we use an OLS regression where score differential is regressed on the SRS and RPI of teams one and two.

pts_team1 - pts_team2 = b0 + b1(SRS1) + b2(SRS2) + b3(RPI1) + b4(RPI2) + e

This will give us the proper weighting of SRS and RPI for our own rankings.

The formula for our rating will be as follows: rank_team1 = b1(SRS1) + b3(RPI1)

Once we have our formula, all 2022 March Madness teams will have their SRS and RPI run through the formula so that we can determine each teams ranking.
We predict that in any given matchup the team with the higher ranking will win and that the team with the highest overall ranking will win the tournament.

**Findings:**

From this project we predict that X TEAM will win the March Madness tounament.
Compared to current actual performance our bracket is X% accurate.

**Limitations:**

The primary limitation is the ammount of data included in out model. 
Since we do not have access to detailed data on injuries, game-plans, or player strengths our rankings overly rely on team metrics.
Additionally, our analysis predicts that a higher ranked team will always beat a lower ranked team instead of generating a probability.

**Extensions:**

This project could be extended with the inclusion of more detailed data on teams and players to create a more accurate ranking. 
Another possibility is that this formula could be applied to other sports to see if this ranking systems is valid accross different athletic events.
This analysis could also be extended by generating a ranking system that gives the probability a higher ranked team will beat a lower ranked team, rather than a binary outcome.
