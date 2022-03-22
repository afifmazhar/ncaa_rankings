# ncaa_rankings
Data Analysis Project for NCAA rankings

**Goal of the Analysis:**

The goal of this analysis is to create a 2022 March Madness bracket by utilizing multiple publicly avaliable team rating systems.

**Project Description:**

This project utilizes historical team ratings and historical tournament game results to construct a linear regression which weighs the importance of various team ratings and creates a hybrid team ranking system, which we use to predict the outcome of March Madness 2022.

**Reproducing the Analysis:**

The first step in our analysis involves cleaning the raw historical tournament game results by running `python3 code/game_results.py` and cleaning / merging historical SRS ratings data by running `python3 code/clean-merge-srs.py`. This produces two clean .csv files (`data/clean/game_results_clean.csv` and `data/clean/team-ratings.csv`) which contain historical tournament game results from 1994-2019 and historical SRS ratings for all division I NCAA basketball teams over the same period. 

Next, we merge each team's SRS data with our historical tournament game results by running `python3 code/combine-games-with-srs.py`. This appends team1 and team2 SRS data (both offensive and defensive) to the `data/clean/game_results_clean.csv` file. 

We then compute our regression by running `python3 code/regression.py`. This creates a .csv file of our regression coefficients (`data/clean/coefficients.csv`) which feeds into our analysis of the 2022 March Madness bracket. 

Finally, running `python3 code/bracket-read-file.py` creates `data/clean/bracket_data.csv` which combines 2022 SRS data (again, offensive and defensive) with the 2022 tournament bracket. Running `python3 code/build_bracket.py` makes use of this 2022 bracket data (along with our regression coefficients from above) and determines the winners of each tournament matchup. The script creates two output .csv files (`data/clean/matchups.csv` and `data/clean/winners.csv`) which store the predicted tournaments matchups and winners for each game of the 2022 March Madness tournament.

You'll need to install the package, Plotly, from the `Requiements.txt` file via the included pip command.
To re-create the data tables, run `python3 code/visual_code/data-table-matchups.py` to obtain a table for all tournament game matchups.  Likewise, run `python3 code/visual_code/final-data-table.py` to obtain a table for the winners of eery tournament game.

**Data:**

The documentation of the ratings data can be briefly summarized. 
In the SRS data set each team in each year is an obeservation.
The columns are each overservation rated according to several metrics. 
The metric we use is OSRS which is Offensive Simple Rating System and DSRS which is Defensive Simple Rating System.
This system is derived from point differential weighted by strength of opponent. 
Not included in this data is anything about tournnament performance or player stats and injuries.

The ranking data used is SRS Team Ratings team ratings from 1994 to 2019. This data was downloaded from - https://www.sports-reference.com/cbb/seasons/2022-ratings.html

The documentation for the game data can be briefly sumarized.
This data set includes every March Madness tournament game from 1994 to 2019 as observations.
We use the scores by each team to generate a score differential variable and the seeds of each team to generate a seed differential.
Not included in the data set is outside team rankings or player information, necessitating a merge with the SRS data.

The game data used is all March Madness games from 1994 to 2019. This data was downloaded from - https://apps.washingtonpost.com/sports/search/

**Cleaning:**

Data sets are cleaned of erroneous lines, hyperlinks, and superflous columns.
Data frames are then merged, matching team names to their ratings for each historical March Madness game.
The cleaned and merged CSV will follow the format - year,round,team1,seed1,score1,team2,seed2,score2,score_diff,seed_diff,OSRS1,DSRS1,OSRS2,DSRS2

**Analysis & Methodology:**

Once each team in every historical game is associated with its ratings in each year, we use an OLS regression where score differential is regressed on the OSRS, DSRS and seed differential of the teams. We initially included historical RPI ratings in our analysis but decided to drop the variable when it did not add any predictive power alongside SRS. Attempts were made to include BPI (ESPN proprietary rating) and NRtg (avaliable via the same source as SRS) but historical avaliability issues lead to their exclusion.

pts_team1 - pts_team2 = b1(team1_OSRS) + b2(team2_OSRS) + b3(team1_DSRS) + b4(team2_DSRS) + b5(seed_diff) + e

This will give us the proper weighting of OSRS, DSRS, and seed_diff to evaulate matchups in building our bracket.

To evaluate matchups in building the bracket, (b1-b2)/2 * (team1_OSRS) + (b1-b2)/2 * (team2_OSRS) + (b3-b4)/2 * (team1_DSRS) + (b3-b4)/2 * (team2_DSRS) + b5 is evaluated. When the sum is >0, team 1 is predicted to win. The reason we average the absolute values of b1/b2 and b3/b4 is that there is no home field advantage in the tournament and it is arbitrary which team is team1 and which is team2, so we average the coefficients.

Once we have our formula, all 2022 March Madness teams will have their SRSs and seed_diff run through the formula so that we can determine each teams ranking.
We predict that in any given matchup the team with the higher ranking will win and that the team with the highest overall ranking will win the tournament.

**Findings:**

From this project we predict that Gonzaga will win the March Madness tounament.
Our model picked 23/32 round 1 winners correctly and 9/16 of the round 2 winners correctly.
Our predicted bracket is included in our visualizations. We find that the weighting for defensive SRS is slightly higher than coefficient for offensive SRS (lending credence to the idea that defense wins championships).  

**Limitations:**

The primary limitation is the ammount of data included in out model. 
Since we do not have access to detailed data on injuries, game-plans, or player strengths our rankings overly rely on team metrics.
Additionally, our analysis determines a strict ranking for teams instead of modeling win percentage for any given matchup.

Additionally, our data is limited by the fact that it conatains only team metrics.
This data would be more accurate and comprehensive if it included information about individual players and injuries.

**Extensions:**

This project could be extended with the inclusion of more detailed data on teams and players to create a more accurate ranking. 
Another possibility is that this formula could be applied to other sports to see if this ranking systems is valid accross different athletic events.
This analysis could also be extended by generating a probability that a higher ranked team will beat a lower ranked team, rather than a binary outcome.
