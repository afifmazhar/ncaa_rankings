# ncaa_rankings
Data Analysis Project for NCAA rankings

Data:

Use seasons 1995-2019

CSV that looks like:
  year,round,team1,seed(team1),score1, team2,seed(team2),score2, score differential,SRS(team1),RPI(team1),SRS(team2),RPI(team2)
  
 
  
 Analysis:
 Create an OLS regression model that predicts the weights of different ratings (SRS, RPI) (encoded in the betas) with the LHS variable a difference between the points scored by team1 and the points scored by team2.
 
  pts_team1 - pts_team2 = b0 + b1(SRS1) + b2(SRS2) + b3(RPI1) + b4(RPI2) + e
  
  Then rank teams in linear fashion according to a sum of the weights multiplied by the ranking variable. 
    i.e. rank_team1 = b1(SRS1) + b3(RPI1), rank_team2 = b2(SRS2) + b4(RPI2)
 
 
 
 Visualization:
 Maybe.
 
    
