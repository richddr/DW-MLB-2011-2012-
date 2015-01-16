# DW-MLB-2011-2012-
Data-warehousing project using real data from MLB seasons 2011 and 2012

Project for a DB class. Purpose of this project was perform ETL (Extract Transform Load) on MLB data acquired from basebal-reference.com from seasons 2011 and 2012. Based on this data, analyse it and retrieve certain interesting patterns. 
Three processes modeled were: team batting, team pitching, team fielding
They three processes had a high grain, yet very detailed.
Operational Enviroment: PostgreSQL, a RDBM
Tables:
  -League
  -Players
  -Teams
  -Batting-Team-Player
  -Fielding-Team-Player
  -Pitching-Team-Player
Dimensional Enviroment (Star Model): MySQL
  -Players Dimension
  -Teams Dimension
  -Pitching Fact
  -Fielding Fact
  -Batting Fact
ETL process:
Extract the data from the operational enviroment, Transform such data for it to be inserted into the Dimensional enviroment, Load data into the Dimensional enviroment along with all previous data.

To analyze the data, Pentaho was used.
A few of the many analisis discovered after the process:
-The batter with the most homeruns per team
-the player who has the most strikeouts per year
-The most feared player in the game
-Best pitcher of the year
-The team with the biggest win/lose percentage from its pitchers. Based on this one can assume the probability of a team winning a game
-The pitcher who has faced the most batters per year
-player who has committed the most errors per team
-the player who has the highest percentage of taking another player out

and many others. They are located in the 'Analisis' folder.
PD: Project is in spanish

Created by Richard Garcia (richddr), Michael Romano (mike809), Michael Gaillard (mpgaillard)
